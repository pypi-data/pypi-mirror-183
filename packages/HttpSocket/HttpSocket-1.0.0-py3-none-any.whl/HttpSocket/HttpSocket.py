import asyncio
from dataclasses import dataclass


@dataclass
class Response:
    status: str
    headers: dict
    body: str


async def send_request(method, host, path, headers=None, body=None):
    # Create a socket and connect to the host
    reader, writer = await asyncio.open_connection(host, 80)

    # Send the request
    request_line = f'{method} {path} HTTP/1.1\r\n' \
                   f'Host: {host}\r\n'
    writer.write(request_line.encode())
    if headers:
        for header, value in headers.items():
            header_line = f'{header}: {value}\r\n'
            writer.write(header_line.encode())
    writer.write(b'\r\n')
    if body:
        writer.write(body)
    await writer.drain()

    # Read the response
    response_line = (await reader.readline()).decode("utf-8").strip()
    response_headers = {}
    while True:
        header_line = await reader.readline()
        if header_line == b'\r\n':
            break
        header, value = header_line.split(b': ')
        response_headers[header.decode("utf-8").strip()] = value.decode("utf-8").strip()
    response_body = (await reader.read()).decode("utf-8").strip()

    # Close the connection
    writer.close()

    # Return the response
    return Response(response_line, response_headers, response_body)

async def get(host, path, headers=None):
    return await send_request('GET', host, path, headers)

async def post(host, path, headers=None, body=None):
    return await send_request('POST', host, path, headers, body)

async def delete(host, path, headers=None):
    return await send_request('DELETE', host, path, headers)

async def put(host, path, headers=None, body=None):
    return await send_request('PUT', host, path, headers, body)
