# cording = utf-8
import asyncio
import os
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from datetime import *
from lib.Utils import Logtools
from lib.DataTools import DataTools

BASE_PATH = "D:\\!!Basedir"
CURTIME = str(date.today()).replace("-", "")


DEVICE_LIST = [
    {'host': "172.27.114.226", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.227", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.244", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.245", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.246", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.247", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.242", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.243", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.248", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.249", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.250", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.251", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.224", 'auth_username': "admin", 'auth_password': "cisco123"},
    {'host': "172.27.114.225", 'auth_username': "admin", 'auth_password': "cisco123"}
]

ADD_ATTR = {'platform': "cisco_nxos", "auth_strict_key": False, "transport": "asyncssh"}


def export_txt(savePath, filename, contents):
    try:
        with open(f"{savePath}//{CURTIME}_{filename}.log", "w", encoding="utf8") as f:
            f.write(contents)
    except Exception as e:
        print(e)


async def run_command(device, command):
    async with AsyncScrapli(**device, **ADD_ATTR) as conn:
        try:
            response = await conn.send_command(command)
            hostname = await conn.get_prompt()
            Logtools.write_log(string=f'{hostname};{response.result};{command}', log_name='Scrapli')
            return {'hostname': hostname, 'result': response.result, 'command': command}
        except ScrapliException as e:
            return f"{device['host']}: Error: {e}"


async def main(inventory, command_set):
    # command = "show runn"
    tasks = []
    for device in inventory:
        for command in command_set:
            tasks.append(run_command(inventory[device], command))

    results = await asyncio.gather(*tasks)

    for item in results:
        if item['command']:
            if os.path.isdir(BASE_PATH + f"\\{item['command']}"):
                export_txt(BASE_PATH + f"\\{item['command']}", f"{item['hostname']}_{item['command']}", item['result'])
            else:
                os.mkdir(BASE_PATH + f"\\{item['command']}")
                export_txt(BASE_PATH + f"\\{item['command']}", f"{item['hostname']}_{item['command']}", item['result'])
        else:
            export_txt(BASE_PATH, f"{item['hostname']}_{item['command']}", item['result'])
    # print("\n".join(results))


if __name__ == "__main__":
    DataTools = DataTools()
    inventory = DataTools.read_yaml("data/inventory_SKT.yml")
    # print(inventory['BORAMAE_EVPN_POC'])
    command_set = DataTools.read_yaml("data/command_set.yml")
    # print(command_set['command_set'])

    asyncio.run(main(inventory['BORAMAE_EVPN_POC'], command_set['command_set']))
