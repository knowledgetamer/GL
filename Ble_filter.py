import asyncio
import sys

from bleak import BleakScanner,BleakClient
async def main(wanted_name):
    device = await BleakScanner.find_device_by_filter(
        lambda BLEDevice,AdvertisementData: BLEDevice.name and BLEDevice.name.lower() == wanted_name.lower()
    )
    print(device)
    ADDRESS=device.address
    
    async with BleakClient(device) as client:
        svcs = client.services
        print("Services:")
        for service in svcs:
            print(service)

if __name__ == "__main__":    
    asyncio.run(main("redminor"))
