import versioneer
from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.md') as f:
    long_description = f.read()


setup(
    name='drb-driver-odata',
    packages=find_namespace_packages(include=['drb.*']),
    description='DRB OData CSC driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/impl/odata',
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'drb.driver': 'odata = drb.drivers.odata:OdataFactory',
        'drb.topic': 'odata = drb.topics.odata'
    },
    package_data={
        'drb.topics.odata': ['cortex.yml']
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    data_files=[('.', ['requirements.txt'])]
)
