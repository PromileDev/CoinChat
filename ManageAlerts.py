from cogs import CryptoUpdate, ManageBD
import time

while True:
    CryptoUpdate.update()
    time.sleep(5)

