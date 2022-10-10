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


