import bluetooth
class Blsocket: 
    flag = False
    socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    socket_port = 1 

    def connectToGlove(device):
        device = '98:DA:60:0A:85:FF'   
        Blsocket.socket.connect( (device, Blsocket.socket_port) )
        #if socket.connect():
        flag = True
        return(True)
    
    def recvData(acces):
            while acces == True:
                print(str(Blsocket.socket.recv(1024)))
        
