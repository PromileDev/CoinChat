from ManageBD import update_cryptocurrency_price
from ManageAPI import *

def update():
    updateBTC()
    updateETH()
    updateLTC()
    print("Cryptocurrency prices updated.")

def updateBTC():
    update_cryptocurrency_price("XBTEUR", getPriceEUR('XBT'))
    update_cryptocurrency_price("XBTUSD", getPriceUSD('XBT'))

def updateETH():
    update_cryptocurrency_price("ETHEUR", getPriceEUR('ETH'))
    update_cryptocurrency_price("ETHUSD", getPriceUSD('ETH'))

def updateLTC():
    update_cryptocurrency_price("LTCEUR", getPriceEUR('LTC'))
    update_cryptocurrency_price("LTCUSD", getPriceUSD('LTC'))

update()