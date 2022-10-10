from setuptools import find_packages, setup

setup(
    name='netbox-vrf-context',
    version='0.1',
    description='A netbox plugin to support VRF contexts',
    url='https://github.com/UK2group/netbox-vrf-context/tree/master/vrf_context',
    author='The Hut Group',
    license='BSD-2-Clause',
    install_requires=['netbox-bgp', 'netbox-static-routes-plugin'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
