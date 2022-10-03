# Netbox VRF Context Plugin

This is a netbox plugin for model VRF Contexts. It has dependencies on:

Netbox BGP - https://pypi.org/project/netbox-bgp/
```
pip install netbox-vrf-context
```
Static Routes - https://github.com/jbparrish17/netbox-static-routes
This project is not currently packaged. Installation will require cloning the repository and running setup.py in the Netbox virtual environment.

## Development

```
virtualenv --python=python3.10 venv
. ./venv/usr/local/bin/activate
# pip install -r requirements.txt   (for liniting)
# or
# pip install poetry invoke
invoke build
invoke debug
```

## Installation

The plugin is available as a Python package in pypi and can be installed with pip  

```
pip install netbox-vrf-context
```
Enable the plugin in /opt/netbox/netbox/netbox/configuration.py:
```
PLUGINS = [
    'netbox_bgp',
    'netbox_static_routes',
    'netbox-vrf-context'
]
```
Restart NetBox and add `netbox-vrf-context` and 2 other dependencies to your local_requirements.txt

See [NetBox Documentation](https://docs.netbox.dev/en/stable/plugins/#installing-plugins) for details
