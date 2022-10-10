# Netbox VRF Context Plugin

This is a netbox plugin for model VRF Contexts. It has dependencies on:

Netbox BGP - https://pypi.org/project/netbox-bgp/
Static Routes - https://github.com/jbparrish17/netbox-static-routes

## Development

```
cp development/dev.env.example development/dev.env
# Set a password for POSTGRES_PASSWORD and REDIS_PASSWORD
# 
vi development/dev.env


virtualenv --python=python3.10 venv
. ./venv/usr/local/bin/activate
# pip install -r requirements.txt   (for liniting)
# or
# pip install poetry invoke
invoke build
invoke debug
```

## Deployment

The plugin is available as a Python package in pypi and can be installed with pip  

```
pip install netbox-vrf-context
```
Enable the plugin in `netbox/netbox/configuration.py` in the `PLUGINS` parameter (which is a list):
```
PLUGINS = [
    'netbox_bgp',
    'netbox_static_routes',
    'netbox-vrf-context'
]
```
Save the file and restart the Netbox service.
