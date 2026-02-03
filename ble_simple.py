import asyncio
from bless import BlessServer

async def main():
    server = BlessServer(name="GOLDEN-BALISE")
    await server.start()
    print("Serveur BLE actif...")
    await asyncio.sleep(999999)

asyncio.run(main())
    
