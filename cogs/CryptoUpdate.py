from cogs import ManageBD, ManageAPI
import time

def update():
    updateBTC()
    updateETH()
    updateLTC()
    print("Cryptocurrency prices updated.")

def updateBTC():
    ManageBD.update_cryptocurrency_price("XBTEUR", ManageAPI.getPriceEUR('XBT'))
    ManageBD.update_cryptocurrency_price("XBTUSD", ManageAPI.getPriceUSD('XBT'))

def updateETH():
    ManageBD.update_cryptocurrency_price("ETHEUR", ManageAPI.getPriceEUR('ETH'))
    ManageBD.update_cryptocurrency_price("ETHUSD", ManageAPI.getPriceUSD('ETH'))

def updateLTC():
    ManageBD.update_cryptocurrency_price("LTCEUR", ManageAPI.getPriceEUR('LTC'))
    ManageBD.update_cryptocurrency_price("LTCUSD", ManageAPI.getPriceUSD('LTC'))

