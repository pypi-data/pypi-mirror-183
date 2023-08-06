import pandas as pd
import df2img
import uuid
import datetime
from abc import abstractmethod

class Prettify:
    def __init__(self, exchange):
        """
        Args:
        exchange (object) - Exchange (Binance / Bybit) class object
        """

        self.exchange = exchange
        self.output = None


    def prettify(self, mode, filename):
        '''
        General function that creates a prettified output from given data.
        Args:
        mode - [pdImage, PILImage, plain]. default: pdImage
        pdImage - returns pandas DataFrame in png format
        PILImage - returns png image by a given template
        plain - returns output as a plain text
        '''
        if mode == "pdImage" and filename:
            self.pdImage(filename)
            
        if mode == "PILImage" and filename:
            self.PILImage(filename)
    
        #! Might not need this mode
        if mode == "plain":
            self.plain()
            
        return self.output

class Binance(Prettify):

    def pandasDf(self):
        
        df = pd.DataFrame(data={
            "Nickname": self.exchange.nicknames,
            "Price"   : self.exchange.prices,
            "Payment" : self.exchange.payments,
            "Min"     : [x["min"] for x in self.exchange.limits],
            "Max"     : [x["max"] for x in self.exchange.limits],
            "Merchant": self.exchange.merchant,
        }).set_index("Nickname")
        return df

    def dataframeToImage(self, filename):
        '''
        Args:
        filename (str) - Specify path for filename as str
        '''
        fig = df2img.plot_dataframe(self.pandasDf(), fig_size=(500,140))
        df2img.save_dataframe(fig=fig, filename=filename)
        self.output = filename
        
    def pdImage(self, filename):
        self.dataframeToImage(filename)
        return self.output
    
    