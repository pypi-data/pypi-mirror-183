import asyncio
import HttpSocket.HttpSocket as HttpSocket

async def main():
    response = await HttpSocket.get('random-word-api.herokuapp.com', '/word?number=5')
    print(response.status)
    print(response.headers)
    print(response.body)

if __name__ == '__main__':
    asyncio.run(main())