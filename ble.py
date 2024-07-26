"""
Bleak Scanner
-------------
Updated on 2020-08-12 by hbldh <henrik.blidh@nedomkull.com>
"""
import asyncio
import platform
import sys

from bleak import BleakScanner,BleakClient

ADDRESS = "6D:B8:0D:7D:75:69"  

async def main(address):
    devices = await BleakScanner.discover(timeout=5.0)
    for d in devices:
        print(d)
    device = await BleakScanner.find_device_by_address(address)
    print(device)
    async with BleakClient(address) as client:      #自己作为client,ADDRESS端作为server
        print(client.is_connected)
    """output =client.connect()
        print(client.services)"""
if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
