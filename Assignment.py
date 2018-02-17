import requests
import matplotlib.pyplot as plt

class graph:
    def __init__(self,coinName,convertTo,datapoints):
        self.coinName = coinName
        self.convertTo = convertTo
        self.datapoints = datapoints
        self.price = []
        self.time = []

    def getDatafromURL(self):
        url = "https://min-api.cryptocompare.com/data/histominute?" \
              "fsym="+self.coinName.upper()+"&tsym="+self.convertTo.upper()+"&limit="+self.datapoints+"&aggregate=3&e=CCCAGG"
        req = requests.get(url)
        self.Fulldata = req.json()['Data']
        for data in self.Fulldata:
            self.time.append(float(data['time']))
            self.price.append(float(data['close']))

    def plotting(self):
        plt.plot(self.time, self.price)
        plt.title(self.coinName.upper()+' convert to '+self.convertTo.upper())
        plt.xlabel('Time in Seconds')
        plt.ylabel('Price in '+self.convertTo.upper())
        plt.show()



btc = graph('btc','usd','99')
btc.getDatafromURL()
btc.plotting()

eth = graph('eth','usd','99')
eth.getDatafromURL()
eth.plotting()