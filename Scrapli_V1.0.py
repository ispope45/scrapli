# cording = utf-8
import asyncio
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


async def main():
    try:
        async with AsyncScrapli(
            host="172.27.114.226",
            auth_username="admin",
            auth_password="cisco123",
            transport="asyncssh",
            platform="cisco_nxos",
            auth_strict_key=False
        ) as conn:
            print(conn)

            await conn.open()
            response = await conn.send_command("show runn")
            print(await conn.get_prompt())
            print(response)
            print(response.result)
    except ScrapliException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())