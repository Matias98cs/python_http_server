import requests

port = 8002
message = 'sucursal=1&s=cafe&rangoregistros=500&categoria='


solicitud = requests.get('http://192.168.0.130:8002', message)
print(solicitud.text)
