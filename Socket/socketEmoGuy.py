# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time
import socket
import thread
import os
from emokit.emotiv import Emotiv

if platform.system() == "Windows":
    pass
isRunning = False
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

def get_data(webS, delay):
    print "Connection Started at"
    with Emotiv(display_output=False, verbose=True, write=True) as headset:
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")

        while headset.running:
            try:
                packet = headset.dequeue()
                #print "%s\n" % headset.sensors
                thread.start_new_thread(send_data, ("%s\n" % headset.sensors, webS, ))
                if not isRunning:
                    print("Stopped")
                    headset.stop()
            except Exception, e:
                print("Error di get_data : "+str(e))
                headset.stop()
            time.sleep(0.001)
def send_data(data, ws):
    #print(data)
    try:
        ws.sendMessage((u""+data))
    except Exception, e:
        print("Error di send_data :" + str(e))
        headset.stop()

class SimpleEcho(WebSocket):
    # Define a function for the thread
    def handleMessage(self):
        # echo message back to client
        global isRunning
        data = u"Hallo"
        self.sendMessage(data)
        print(self.data)
        if self.data == 'START':
            isRunning = True
            try:
                thread.start_new_thread(get_data, (self, 2, ))
                #print("Hai")
            except Exception, e:
                print("Error: " + str(e))
        elif self.data == 'STOP':
            isRunning = False

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('127.0.0.1', 8080, SimpleEcho)

server.serveforever()
			
