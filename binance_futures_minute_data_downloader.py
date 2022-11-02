import pandas as pd
from datetime import datetime
import pytz
import json
#from binance.client import Client    
from binance.cm_futures import CMFutures

coins = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT', 'XLMUSDT', 'ADAUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT', 'BATUSDT', 'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT', 'COMPUSDT', 'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT', 'DOTUSDT', 'DEFIUSDT', 'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'EGLDUSDT', 'SOLUSDT', 'STORJUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT', 'ENJUSDT', 'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'LRCUSDT', 'MATICUSDT', 'OCEANUSDT', 'CVCUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT', 'GRTUSDT', '1INCHUSDT', 'UNFIUSDT', 'CHZUSDT', 'SANDUSDT', 'ANKRUSDT', 'LITUSDT', 'REEFUSDT', 'RVNUSDT', 'SFPUSDT', 'XEMUSDT', 'COTIUSDT', 'CHRUSDT', 'MANAUSDT', 'ALICEUSDT', 'ONEUSDT', 'LINAUSDT', 'STMXUSDT', 'DENTUSDT', 'CELRUSDT', 'HOTUSDT', 'MTLUSDT', 'OGNUSDT', 'NKNUSDT', 'DGBUSDT', '1000SHIBUSDT', 'BAKEUSDT', 'BTCDOMUSDT', 'MASKUSDT', 'IOTXUSDT', 'AUDIOUSDT', 'RAYUSDT', 'C98USDT', 'ATAUSDT', 'FTTUSDT', 'DYDXUSDT', '1000XECUSDT', 'GALAUSDT', 'CELOUSDT', 'ARUSDT', 'KLAYUSDT', 'ARPAUSDT', 'LPTUSDT', 'ENSUSDT', 'PEOPLEUSDT', 'ANTUSDT', 'ROSEUSDT', 'DUSKUSDT', 'FLOWUSDT', 'IMXUSDT', 'API3USDT', 'GMTUSDT', 'APEUSDT', 'BNXUSDT', 'WOOUSDT', 'JASMYUSDT', 'ETHUSDT', 'BTCUSDT']
#coins = ['BTCUSDT','ETHUSDT','BCHUSDT']
# # Opening JSON file
# with open('symbols.json', 'r') as openfile:
#     json_object = json.load(openfile)
# coins = json_object['symbols']

api_key='cb0f9c84b253279675fdc443596773a649307520124c77f9ea294676474f9aae'
api_secret='f97ecca128de7ecac4f5eabab519c6dfa0e12ce66a0ece57f8b98efa94fad91f'

limit = 1000
cm_futures_client = CMFutures(base_url = "https://testnet.binancefuture.com")

#start = pd.to_datetime('2022-10-29 20:15:00+00:00')
#end = pd.to_datetime('2022-10-30 01:00:00+00:00')


#t = 0



for coin in coins[35:40]:
    try:
        t=0
        start = ""
        end = ""
        df_final = pd.DataFrame(columns=['time', 'high','low','open','volume','close','timestamp'])
        while(t<263):

            data = cm_futures_client.klines(symbol=coin, interval='1m',
                                        #endTime=int(start.value/1e6), 
                                        #startTime=int(end.value/1e6),
                                        startTime=start,
                                        endTime = end,
                                        limit = limit)
            
            df = pd.DataFrame.from_dict(data=data,orient='columns')
            df.drop(df.iloc[:, 6:12], inplace=True, axis=1)
            df.rename(columns={0:'time',1:'open',2:'high',3:'low',4:'close',5:'volume'},inplace=True)
            end = df['time'].values[0]
            df['timestamp'] = [datetime.fromtimestamp(d/1000,pytz.utc) for d in df.time]
            # date, time = str(df['timestamp'].values[0]).split('T')[0], str(df['timestamp'].values[0]).split('T')[1]
            
            # time_new = time[:8]
            # total_time = date+' '+time_new
            
            #df.drop('time',inplace=True)
            #print(df)
            #df_final = pd.concat([df ,df_final[:]]).reset_index(drop = True)
            #df.to_csv("hmm"+str(end)+".csv")
            df_final = pd.concat([df,df_final[1:]],ignore_index=True)
        

            #date = df['timestamp'].values[1]
            
            
            
            #date = str(df['timestamp'].values[0]).split('+')[0]
            #print(date)
            #print(time)
            #print(total_time)

                #print(date)
            #timeFormat = "%Y-%m-%d %H:%M:%S"
            #end = datetime.strptime(total_time, timeFormat)
            #print(end)
            #toTs = time.mktime(end.timetuple())
            t = t+1
            print(t)
            #print(end)
            #df.to_csv("./data/"+coin+".csv")


        df_final.set_index('timestamp',inplace=True)
        df_final = df_final.drop(['time'],axis=1)
        print(coin+" Downloaded successfully!")
        df_final.to_csv("./data/"+coin+".csv")

    except:
        pass
