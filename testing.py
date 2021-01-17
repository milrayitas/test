import websocket
from websocket import create_connection
import json
import pandas as pd
import psutil
import matplotlib.pyplot as plt
import time

# %matplotlib notebook
# plt.rcParams['animation.html']='jshtml'

fig=plt.figure()
ax=fig.add_subplot(111)
fig.show()

ws = create_connection('wss://api.hitbtc.com/api/2/ws')      
ws.send('{"method":"subscribeTicker" , "params":{"symbol":"ETHUSD"}}') 
ws.recv()
x , y=[],[]
i=0
while True:
    # try:
      datos=json.loads(ws.recv())['params']
      # recibido.append(datos)
      # recibido=recibido.append(datos)
      ultimo=datos['last']
      ask=datos['ask']
      fecha=datos['timestamp']
      x.append(fecha)
      y.append(ultimo)
      # print(ultimo , ask, fecha)
      ax.plot(x,y,color='b')

      fig.canvas.draw()
      time.sleep(0.1)
