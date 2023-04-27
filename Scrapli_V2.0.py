# cording = utf-8
import asyncio
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
DEViCE_LIST = [
    {'platform': "cisco_nxos", 'host': "172.27.114.226", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.227", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.244", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.245", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.246", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.247", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.242", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.243", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.248", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.249", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.250", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.251", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.224", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"},
    {'platform': "cisco_nxos", 'host': "172.27.114.225", 'auth_username': "admin", 'auth_password': "cisco123", "auth_strict_key": False, "transport": "asyncssh"}
]


async def list_to_async_iter(d):
    for device in d:
        yield device


async def run_command(device, command):
    try:
        async with AsyncScrapli(**device) as conn:
            response = await conn.send_command("show run | i hostname")
            hostname = await conn.get_prompt()
            return f"{hostname}: {response.result}"
    except ScrapliException as e:
        return f"{device['host']}: Error: {e}"


async def main():
    try:
        tasks = []
        async for device in list_to_async_iter(DEViCE_LIST):
            tasks.append(run_command(device, "cmd"))

        results = await asyncio.gather(*tasks)
        print(results)
    except ScrapliException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())