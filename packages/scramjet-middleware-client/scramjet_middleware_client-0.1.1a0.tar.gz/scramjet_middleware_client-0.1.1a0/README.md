<h1 align="center"><strong>Scramjet Middleware client</strong></h1>

<p align="center">
    <a href="https://github.com/scramjetorg/transform-hub/blob/HEAD/LICENSE"><img src="https://img.shields.io/github/license/scramjetorg/transform-hub?color=green&style=plastic" alt="GitHub license" /></a>
    <a href="https://scr.je/join-community-mg1"><img alt="Discord" src="https://img.shields.io/discord/925384545342201896?label=discord&style=plastic"></a>
</p>

## About:

This package provides a **Middleware client**.


## Usage:
> ❗NOTE: You need to provide your middleware [access token](https://docs.scramjet.org/platform/quick-start#step-1-set-up-the-environment) if you are not hosting STH locally.

```python
import asyncio
from middleware_client.middleware_client import MiddlewareClient

URL = 'https://api.scramjet.cloud/api/v1'
TOKEN = '' # your middleware token

middleware = MiddlewareClient(URL, TOKEN)
res = asyncio.run(middleware.get_managers())
```
