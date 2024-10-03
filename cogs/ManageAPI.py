import requests

def getPriceUSD(cripto):
    url = f"https://api.kraken.com/0/public/Ticker?pair={cripto}USD"
    response = requests.get(url)
    data = response.json()
    
    if "result" in data:
        precio = data["result"][list(data["result"].keys())[0]]['c'][0]  # Precio actual
        return precio
    else:
        return None
       
def getPriceEUR(cripto):
    url = f"https://api.kraken.com/0/public/Ticker?pair={cripto}EUR"
    response = requests.get(url)
    data = response.json()
    
    if "result" in data:
        precio = data["result"][list(data["result"].keys())[0]]['c'][0]  # Precio actual
        return precio
    else:
        return None

# Ejemplo de uso
Price = getPriceUSD('XBT')
Price2 = getPriceEUR('XBT')

print(f"El precio actual de Bitcoin es: {Price} USD")
print(f"El precio actual de Bitcoin es: {Price2} EUR")


'''
CRYPTO
Bitcoin: XBTUSD
Ethereum: ETHUSD
Litecoin: LTCUSD
'''