# cording = utf-8
import asyncio
import os
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
from datetime import *

from lib.DataTools import *
from lib.Utils import *


BASE_PATH = "D:\\!!Basedir"
CURTIME = str(date.today()).replace("-", "")

ADD_ATTR = {'platform': "cisco_nxos", "auth_strict_key": False, "transport": "asyncssh"}


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
            chkdir(BASE_PATH + f"\\{item['command']}")
            export_txt(BASE_PATH + f"\\{item['command']}", f"{item['hostname']}_{item['command']}", item['result'])
        else:
            export_txt(BASE_PATH, f"{item['hostname']}", item['result'])


if __name__ == "__main__":
    inventory = read_yaml("data/inventory_SKT.yml")
    # print(inventory['BORAMAE_EVPN_POC'])
    command_set = read_yaml("data/command_set.yml")
    # print(command_set['command_set'])

    asyncio.run(main(inventory['BORAMAE_EVPN_POC'], command_set['command_set']))
