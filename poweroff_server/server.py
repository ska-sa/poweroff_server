#!/usr/bin/env python3

"""A simple webserver that shuts down the machine when triggered"""

import asyncio
import argparse
from asyncio.subprocess import PIPE, DEVNULL

from aiohttp import web


async def poweroff(request: web.Request) -> web.Response:
    if request.headers.get('X-Poweroff-Server') != '1':
        return web.json_response({'error': 'X-Poweroff-Server header missing or wrong value'},
                                 status=400)
    try:
        if not request.app['dry_run']:
            process = await asyncio.create_subprocess_exec(
                '/bin/systemctl', '--no-ask-password', '--no-block', 'poweroff',
                stdin=DEVNULL, stdout=PIPE, stderr=PIPE)
            stdout_bytes, stderr_bytes = await process.communicate()
            stdout = stdout_bytes.decode('utf-8', errors='replace')
            stderr = stderr_bytes.decode('utf-8', errors='replace')
            returncode = process.returncode
        else:
            stdout = ''
            stderr = 'Dry run successful'
            returncode = 0
    except OSError as exc:
        return web.json_response({'error': str(exc)}, status=500)

    if returncode != 0:
        return web.json_response({'error': 'systemctl failed', 'stdout': stdout, 'stderr': stderr},
                                 status=500)
    else:
        return web.json_response({'stdout': stdout, 'stderr': stderr}, status=202)


def main():
    parser = argparse.ArgumentParser(description='Power off system in response to web request')
    parser.add_argument('--host', help='Host to bind [all]')
    parser.add_argument('--port', type=int, default=8080, help='Port to bind [%(default)s]')
    parser.add_argument('--dry-run', action='store_true', help='Only pretend to power off')
    args = parser.parse_args()

    app = web.Application()
    app['dry_run'] = args.dry_run
    app.router.add_post('/poweroff', poweroff)
    web.run_app(app, host=args.host, port=args.port)


if __name__ == '__main__':
    main()
