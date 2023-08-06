import io
import json

from drb.core import DrbFactory, DrbNode
from drb.drivers.http import DrbHttpNode
from drb.drivers.json import JsonNode
from drb.exceptions.core import DrbFactoryException
from drb.utils import keyringconnection


from .odata_node import OdataNode
from .odata_nodes import ODataProductNode
from .odata_services_nodes import ODataServiceNodeDhus, \
    ODataServiceNodeDias, ODataServiceNodeCSC
from .odata_utils import ODataServiceType, ODataUtils


class OdataFactory(DrbFactory):
    def _create(self, node: DrbNode) -> DrbNode:
        if isinstance(node, OdataNode):
            return node
        if isinstance(node, DrbHttpNode):
            if '$format=json' not in node.path.original_path:
                if '?' not in node.path.original_path:
                    node._path = node.path.original_path + '?&$format=json'
                else:
                    node._path = node.path.original_path + '&$format=json'
            req = node.get_impl(io.BytesIO).read().decode()
            json_node = JsonNode(json.loads(req))
            return [ODataProductNode(source=node.path.original_path,
                                     auth=node.auth,
                                     data=e.value
                                     ) for e in json_node['value', :]]
        final_url = node.path.name.replace('+odata', '')
        auth = None
        if keyringconnection.kr_check(final_url):
            auth = keyringconnection.kr_get_auth(final_url)
        service_type = ODataUtils.get_type_odata_svc(final_url, auth)
        if service_type == ODataServiceType.CSC:
            return ODataServiceNodeCSC(final_url, auth)
        if service_type == ODataServiceType.DHUS:
            return ODataServiceNodeDhus(final_url, auth)
        if service_type == ODataServiceType.ONDA_DIAS:
            return ODataServiceNodeDias(final_url, auth)
        raise DrbFactoryException(f'Unsupported Odata service: {final_url}')
