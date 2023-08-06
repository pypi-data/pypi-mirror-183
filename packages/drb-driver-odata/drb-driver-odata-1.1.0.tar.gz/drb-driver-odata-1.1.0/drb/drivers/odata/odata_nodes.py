from __future__ import annotations

import io
import json
import time
from multiprocessing import Process

from typing import Any, Dict, \
    List, Optional, Tuple, Union

from drb.core import ParsedPath, DrbNode
from drb.exceptions.core import DrbException
from drb.nodes.abstract_node import AbstractNode

from .odata_node import OdataNode
from .odata_utils import ODataUtils, ODataServiceType
from ...exceptions.odata import OdataRequestException

process = None


class ODataProductNode(OdataNode):
    def __init__(self, source: Union[str, OdataNode],
                 product_uuid: str = None,
                 data: Dict = None,
                 **kwargs):
        self._type = ODataServiceType.UNKNOWN

        if isinstance(source, OdataNode):
            super(ODataProductNode, self).__init__(source.get_service_url(),
                                                   source.get_auth())
            self._type = source.type_service
            self.__parent = source
            self.__uuid = product_uuid
        elif isinstance(data, Dict):
            self.__parent = None
            auth = kwargs['auth'] if 'auth' in kwargs.keys() else None
            super(ODataProductNode, self).__init__(
                source.split('/Products')[0],
                auth
            )
            self._type = ODataUtils.get_type_odata_svc(
                source.split('/Products')[0], auth)
            self.__uuid = data.get('id') if \
                self._type == ODataServiceType.ONDA_DIAS.value \
                else data.get('Id')
        else:
            auth = kwargs['auth'] if 'auth' in kwargs.keys() else None
            super(ODataProductNode, self).__init__(
                source.split('/Products')[0],
                auth
            )
            self._type = ODataUtils.get_type_odata_svc(
                source.split('/Products')[0], auth)
            self.__parent = None
            self.__uuid = product_uuid

        self.__path = ParsedPath(
            f'{self.get_service_url()}/Products({self.__uuid})')
        self.__product = data
        self.__attr = None

    def format_product(self, uuid: str):
        if self.parent is not None:
            return self.parent.format_product(self.__uuid)
        if self.type_service == ODataServiceType.DHUS:
            return "Products('{0}')".format(uuid)
        return "Products({0})".format(uuid)

    @property
    def type_service(self) -> ODataServiceType:
        return self._type

    def __load_product(self):
        if self.__product is None:
            self.__product = ODataUtils.req_product_by_uuid(
                self,
                self.format_product(self.__uuid))

    @property
    def name(self) -> str:
        self.__load_product()
        if self._type == ODataServiceType.ONDA_DIAS:
            return self.__product['name']
        else:
            return self.__product['Name']

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def path(self) -> ParsedPath:
        return self.__path

    @property
    def parent(self) -> Optional[DrbNode]:
        return self.__parent

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        self.__load_product()
        if self.__attr is None:
            self.__attr = {(k, None): v for k, v in self.__product.items()}
        return self.__attr

    @property
    def children(self) -> List[DrbNode]:
        return [ODataProductAttributeNode(self, self.__uuid)]

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        self.__load_product()
        if namespace_uri is None:
            try:
                return self.__product[name]
            except KeyError:
                pass
        raise DrbException(f'No attribute found: ({name}, {namespace_uri})')

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        if namespace is None:
            if name is not None:
                return name == self.children[0].name
            return True
        return False

    def order(self):
        if self.type_service in [
            ODataServiceType.CSC, ODataServiceType.ONDA_DIAS] and \
                self.is_online is False:
            resp = ODataUtils.launch_order(self.parent,
                                           self.get_attribute(self.parent.id),
                                           self.parent.order)
            order = ODataOrderNode(self.__parent, json.loads(
                resp.value.decode()))

            return order
        else:
            raise NotImplemented()

    def close(self) -> None:
        pass

    def has_impl(self, impl: type) -> bool:
        if impl == ODataProductNode:
            return True
        if self.type_service == ODataServiceType.ONDA_DIAS:
            online = not self.get_attribute('offline')
        else:
            online = self.get_attribute('Online')
        return online and (impl == io.BufferedIOBase or impl == io.BytesIO)

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            if impl == ODataProductNode:
                return self
            return ODataUtils.req_product_download(self, self.format_product(
                self.__uuid),
                                                   kwargs.get('start', None),
                                                   kwargs.get('end', None))
        raise DrbException(f'Not supported implementation: {impl}')

    def __eq__(self, other):
        if isinstance(other, ODataProductNode):
            return super().__eq__(other) and other.__uuid == self.__uuid
        return False

    def __hash__(self):
        return hash(self._service_url)

    @property
    def is_online(self):
        if self._type == ODataServiceType.DHUS or \
                self._type == ODataServiceType.CSC:
            return self.get_attribute('Online')
        elif self._type == ODataServiceType.ONDA_DIAS:
            return not self.get_attribute('offline')
        return None


class ODataProductAttributeNode(OdataNode):
    __name = 'Attributes'

    def __init__(self, source: ODataProductNode, prd_uuid: str):
        super().__init__(source.get_service_url(), source.get_auth())
        self.__uuid = prd_uuid
        self.__parent = source
        self.__attr = None
        self._type = source.type_service

    @property
    def type_service(self) -> ODataServiceType:
        return self._type

    def __load_attributes(self) -> None:
        if self.__attr is None:
            self.__attr = ODataUtils.req_product_attributes(
                self,
                self.parent.parent.format_product(self.__uuid),
                self.parent.parent.format_attributes()
            )

    @property
    def name(self) -> str:
        return self.__name

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    @property
    def path(self) -> ParsedPath:
        return self.__parent.path / self.__name

    @property
    def parent(self) -> Optional[DrbNode]:
        return self.__parent

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return {}

    @property
    def children(self) -> List[DrbNode]:
        self.__load_attributes()
        return [ODataAttributeNode(self, data=x) for x in self.__attr]

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        raise DrbException(f'No attribute found: ({name}, {namespace_uri})')

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        if namespace is None:
            if name is not None:
                for x in self.__attr:
                    if name in x.keys():
                        return True
                return False
            return len(self.__attr) > 0
        return False

    def close(self) -> None:
        pass

    def has_impl(self, impl: type) -> bool:
        return False

    def get_impl(self, impl: type, **kwargs) -> Any:
        raise DrbException(f'Do not support implementation: {impl}')


class ODataAttributeNode(OdataNode):
    def __init__(self, source: Union[str, ODataProductAttributeNode],
                 **kwargs):
        if isinstance(source, ODataProductAttributeNode):
            super().__init__(source.get_service_url(), source.get_auth())
            self.__parent = source
            self._type = source.type_service
        elif isinstance(source, str):
            auth = kwargs['auth'] if 'auth' in kwargs.keys() else None
            super().__init__(source, auth)
            self.__parent = None
            self._type = ODataServiceType.UNKNOWN
        else:
            raise OdataRequestException(f'Unsupported source: {type(source)}')
        self.__path = None
        self.__data = kwargs['data'] if 'data' in kwargs.keys() else None

    @property
    def type_service(self) -> ODataServiceType:
        return self._type

    @property
    def name(self) -> str:
        if self._type == ODataServiceType.ONDA_DIAS:
            return self.__data['name']
        else:
            return self.__data['Name']

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def value(self) -> Optional[Any]:
        if self._type == ODataServiceType.ONDA_DIAS:
            return self.__data['value']
        else:
            return self.__data['Value']

    @property
    def path(self) -> ParsedPath:
        if self.__path is None:
            if self.__parent is None:
                self.__path = ParsedPath(self.name)
            else:
                self.__path = self.__parent.path / self.name
        return self.__path

    @property
    def parent(self) -> Optional[DrbNode]:
        return self.__parent

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return {(k, None): v for k, v in self.__data.items()}

    @property
    def children(self) -> List[DrbNode]:
        return []

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        if namespace_uri is None and name in self.__data.keys():
            return self.__data[name]
        raise DrbException(f'Attribute not found: ({name}, {namespace_uri})')

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        return False

    def close(self) -> None:
        pass

    def has_impl(self, impl: type) -> bool:
        return False

    def get_impl(self, impl: type, **kwargs) -> Any:
        raise DrbException(f'Do not support implementation: {impl}')


class ODataOrderNode(AbstractNode):

    def __init__(self, node: OdataNode, source: dict):
        self.__name = source['Id']
        self.__atr = {(k, None): source[k] for k in source.keys()}
        self.__parent = node
        self.__path = ParsedPath(
            f'{node.get_service_url()}/{node.format_order(self.__name)}')

    @property
    def product(self):
        data = ODataUtils.req_product_order_by_uuid(self)
        return ODataProductNode(self.__parent, data=data)

    @property
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return self.__atr

    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
        if namespace_uri is None:
            try:
                return self.attributes[(name, None)]
            except KeyError:
                pass
        raise DrbException(f'No attribute found: ({name}, {namespace_uri})')

    @property
    def parent(self) -> Optional[DrbNode]:
        return self.__parent

    @property
    def path(self) -> ParsedPath:
        return self.__path

    @property
    def children(self) -> List[DrbNode]:
        return []

    def close(self) -> None:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def namespace_uri(self) -> Optional[str]:
        return None

    @property
    def value(self) -> Optional[Any]:
        return None

    def has_impl(self, impl: type) -> bool:
        return False

    def get_impl(self, impl: type, **kwargs) -> Any:
        return None

    @property
    def status(self):
        data = ODataUtils.get_order_by_uuid(
            self.parent,
            self.parent.format_order(self.name)
        )
        self.__atr = {(k, None): data[k] for k in data.keys()}
        return data['Status']

    def cancel(self):
        if self.parent.type_service == ODataServiceType.CSC:
            return ODataUtils.cancel_order(
                self.parent, self.parent.format_order(
                    self.name
                ))
        else:
            raise NotImplemented

    def _wait_and_check(self, order: ODataOrderNode, wait: int = 60):
        while 1:
            if not order.status != 'in_progress':
                break
            res = ODataUtils.get_order_by_uuid(
                self.parent,
                self.parent.format_order(self.name)
            )
            if res['Status'] == 'completed':
                self.product.attributes[('Online', None)] = 'True'
                break
            if res['Status'] in ['failed', 'cancelled']:
                break
            time.sleep(wait)

    def wait(self, step: int = 60):
        global process
        process = Process(target=self._wait_and_check, args=(self, step))
        process.start()
        return True

    def stop(self):
        global process
        process.terminate()
