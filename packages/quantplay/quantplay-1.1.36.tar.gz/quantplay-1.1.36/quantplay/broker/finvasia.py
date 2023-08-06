from quantplay.broker.finvasia.shoonya import ShoonyaApiPy
from quantplay.utils.constant import Constants
import pyotp
import io
import os
import zipfile

import pandas as pd
import numpy as np
import requests
import time

logger = Constants.logger

class FinvAsia:

    def __init__(self,
                 order_updates=None,
                 api_secret=None,
                 imei=None,
                 password=None,
                 totp_key=None,
                 user_id=None,
                 vendor_code=None):
        self.order_updates = order_updates

        self.api = ShoonyaApiPy()
        totp = pyotp.TOTP(totp_key).now()
        response = self.api.login(userid=user_id,
                             password=password,
                             twoFA=totp,
                             vendor_code=vendor_code,
                             api_secret=api_secret,
                             imei=imei)
        print("finvasia login successful email {} account_id {}".format(response['email'], response['actid']))
        self.load_instrument()
        pass

    def initialize_expiry_fields(self):
        self.instrument_file_FO.loc[:, 'tradingsymbol'] = self.instrument_file_FO.Symbol
        self.instrument_file_FO.loc[:, 'expiry'] = pd.to_datetime(self.instrument_file_FO.Expiry)

        self.instrument_file_FO.loc[:, "expiry_year"] = self.instrument_file_FO["expiry"].dt.strftime("%y").astype(str)
        self.instrument_file_FO.loc[:, "month"] = self.instrument_file_FO["expiry"].dt.strftime("%b").str.upper()

        self.instrument_file_FO.loc[:, "month_number"] = self.instrument_file_FO["expiry"].dt.strftime("%m").astype(
            float).astype(str)
        self.instrument_file_FO.loc[:, 'month_number'] = np.where(self.instrument_file_FO.month_number == 'nan',
                                                                  np.nan,
                                                                  self.instrument_file_FO.month_number.str.split(
                                                                      ".").str[0]
                                                                  )

        self.instrument_file_FO.loc[:, "week_option_prefix"] = np.where(
            self.instrument_file_FO.month_number.astype(float) >= 10,
            self.instrument_file_FO.month.str[0] + self.instrument_file_FO["expiry"].dt.strftime("%d").astype(str),
            self.instrument_file_FO.month_number + self.instrument_file_FO["expiry"].dt.strftime("%d").astype(str),
        )

        self.instrument_file_FO.loc[:, "next_expiry"] = self.instrument_file_FO.expiry + pd.DateOffset(days=7)

    def add_quantplay_fut_tradingsymbol(self):
        seg_condition = [
            ((self.instrument_file_FO["Instrument"].str.contains("FUT")) & (
                        self.instrument_file_FO.Instrument != "OPTFUT"))
        ]

        tradingsymbol = [
            self.instrument_file_FO.tradingsymbol + self.instrument_file_FO.expiry_year + self.instrument_file_FO.month + "FUT"
        ]

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.select(
            seg_condition, tradingsymbol, default=self.instrument_file_FO.tradingsymbol
        )

    def add_quantplay_opt_tradingsymbol(self):
        seg_condition = (self.instrument_file_FO["StrikePrice"] > 0)
        weekly_option_condition = (
                (self.instrument_file_FO.expiry.dt.month == self.instrument_file_FO.next_expiry.dt.month) & (
                    self.instrument_file_FO.Exchange == "NFO"))
        month_option_condition = (
                (self.instrument_file_FO.expiry.dt.month != self.instrument_file_FO.next_expiry.dt.month) | (
                    self.instrument_file_FO.Exchange == "MCX"))

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.where(
            seg_condition,
            self.instrument_file_FO.tradingsymbol + self.instrument_file_FO.expiry_year,
            self.instrument_file_FO.tradingsymbol
        )

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.where(
            seg_condition & weekly_option_condition,
            self.instrument_file_FO.tradingsymbol + self.instrument_file_FO.week_option_prefix,
            self.instrument_file_FO.tradingsymbol
        )

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.where(
            seg_condition & month_option_condition,
            self.instrument_file_FO.tradingsymbol + self.instrument_file_FO.month,
            self.instrument_file_FO.tradingsymbol
        )

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.where(
            seg_condition,
            self.instrument_file_FO.tradingsymbol +
            self.instrument_file_FO.StrikePrice.astype(float).astype(str).str.split(".").str[0],
            self.instrument_file_FO.tradingsymbol
        )

        self.instrument_file_FO.loc[:, "tradingsymbol"] = np.where(
            seg_condition,
            self.instrument_file_FO.tradingsymbol + self.instrument_file_FO.OptionType,
            self.instrument_file_FO.tradingsymbol
        )

    def get_df_from_zip(self, url):
        response = requests.get(url, timeout=10)
        z = zipfile.ZipFile(io.BytesIO(response.content))

        directory = '/tmp/'
        z.extractall(path=directory)
        file_name = url.split(".txt")[0].split("/")[-1]
        os.system('cp /tmp/{}.txt /tmp/{}.csv'.format(file_name, file_name))
        time.sleep(2)
        return pd.read_csv('/tmp/{}.csv'.format(file_name))

    def load_instrument(self):
        instrument_file_FO = self.get_df_from_zip("https://api.shoonya.com/NFO_symbols.txt.zip")
        instrument_file_MCX = self.get_df_from_zip("https://api.shoonya.com/MCX_symbols.txt.zip")

        self.instrument_file_FO = pd.concat([instrument_file_MCX, instrument_file_FO])

        self.initialize_expiry_fields()
        self.add_quantplay_opt_tradingsymbol()
        self.add_quantplay_fut_tradingsymbol()
        self.fno_symbol_map = dict(zip(self.instrument_file_FO.TradingSymbol, self.instrument_file_FO.tradingsymbol))

    def event_handler_order_update(self, order):
        try:
            order['placed_by'] = order['actid']
            order['tag'] = order['actid']
            order['order_id'] = order['norenordno']
            order['exchange_order_id'] = order['exchordid']
            order['exchange'] = order['exch']

            # TODO translate symbol
            # -EQ should be removed
            # F&O symbol translation
            order['tradingsymbol'] = order['tsym']

            if order['exchange'] == "NSE":
                order['tradingsymbol'] = order['tradingsymbol'].replace("-EQ", "")
            elif order['exchange'] in ["NFO", "MCX"]:
                order["tradingsymbol"] = self.fno_symbol_map[order["tradingsymbol"]]

            order['order_type'] = order['prctyp']
            if order['order_type'] == "LMT":
                order['order_type'] = "LIMIT"
            elif order['order_type'] == "MKT":
                order['order_type'] = "MARKET"
            elif order['order_type'] == "SL-LMT":
                order['order_type'] = "SL"

            if order['trantype'] == "S":
                order['transaction_type'] = "SELL"
            elif order['trantype'] == "B":
                order['transaction_type'] = "BUY"
            else:
                logger.error("[UNKNOW_VALUE] finvasia transaction type {} not supported".format(order['trantype']))

            order['quantity'] = int(order['qty'])

            if 'trgprc' in order:
                order['trigger_price'] = float(order['trgprc'])
            else:
                order['trigger_price'] = None

            order['price'] = float(order['prc'])

            if order["status"] == "TRIGGER_PENDING":
                order["status"] = "TRIGGER PENDING"
            elif order["status"] == "CANCELED":
                order["status"] = "CANCELLED"

            print(f"order feed {order}")
            self.order_updates.put(order)
        except Exception as e:
            logger.error("[ORDER_UPDATE_PROCESSING_FAILED] {}".format(e))

    def stream_order_data(self):
        self.api.start_websocket(order_update_callback=self.event_handler_order_update)

