# import websocket
from websocket import create_connection
import json
import pandas as pd
# import psutil
import matplotlib.pyplot as plt
import time
import datetime as dt
from datetime import datetime , date
import pytz
import plotly.graph_objects as go
from IPython.display import clear_output


ws = create_connection('wss://api.hitbtc.com/api/2/ws')      
ws.send('{"method":"subscribeTicker" , "params":{"symbol":"BTCUSD"}}') 
ws.recv()

def graphic_online():
  tz_BA = pytz.timezone('America/Buenos_Aires')
  ahora=datetime.now(tz_BA).time()
  ahoraFormat = ahora.strftime("%H:%M")
  print(ahoraFormat)
  end_MervalCI = datetime.strptime('15:57', "%H:%M").time()
  start_MervalCI = datetime.strptime('11:00', "%H:%M").time()
  Check_hora = False #@param {type:"boolean"}
  
  if Check_hora == True:
    print(start_MervalCI, ahoraFormat, end_MervalCI)
    if (start_MervalCI < ahora < end_MervalCI) != True:
      print('Mercado Cerrado')
      return
    else:
      print("Dentro del horario del mercado")
      print('')
      pass
  else:
    print('Estamos en modo prueba')
    pass 
  
  recibido=[]
  oldtime = time.time()
  while True:
    try:
      datos=json.loads(ws.recv())['params']#aqui poner el websocket que corrponda
      recibido.append(datos)
    except:
      pass
    if time.time() - oldtime < 10:#poner cada 60, antes es al pedo
      pass
    else:
      a=pd.DataFrame(recibido)
      oldtime = time.time()
      clear_output()
       
      fig= go.Figure(data=[go.Scatter(x=a['timestamp'], y=a['last'])])
      fig.show()

 
b=graphic_online() 
