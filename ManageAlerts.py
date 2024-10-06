from cogs import CryptoUpdate
import time

while True:
    CryptoUpdate.update()
    time.sleep(5)