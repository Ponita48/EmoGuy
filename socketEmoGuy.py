# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time
import socket
import thread
import numpy as np
import os
from emokit.emotiv import Emotiv

if platform.system() == "Windows":
    pass
isRunning = False

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
def get_data(webS, delay):
    header = ['F3','F4','F7','F8','AF4','AF3','FC5','FC6','P7','P8','T7','T8','O1','O2']
    # ubahData = {'F3':np.array([]),'F4':np.array([]),'F7':np.array([]),'F8':np.array([]),'AF4':np.array([]),'AF3':np.array([]),'FC5':np.array([]),'FC6':np.array([]),'P7':np.array([]),'P8':np.array([]),'T7':np.array([]),'T8':np.array([]),'O1':np.array([]),'O2':np.array([])}
    ubahData = np.array(header)
    old_data = ""
    print "Connection Started at"
    with Emotiv(display_output=False, verbose=True, write=True) as headset:
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")
        dequeue = headset.dequeue
        counter = 0
        mean = 3000;
        i=0
        vstackX = np.vstack
        appendX = np.append
        arrayX = np.array
        while headset.running and isRunning:
            try:
                #packet = headset.dequeue()
                dequeue()
                #print "test"
                if old_data != ("%s\n" % headset.sensors) :
                    old_data = "%s\n" % headset.sensors
                    counter=counter+1
                    print counter
                    # print headset.sensors
                    #print headset.sensors[header[0]]['value']
                    temp = headset.sensors[header[0]]['value']
                    # for i in range (0,14):
	                   #  ubahData[header[i]] = np.append(np.array(ubahData[header[i]]),np.array(headset.sensors[header[i]]['value']))
                    for i in range(1, 14):
                    	temp = appendX(temp, arrayX(headset.sensors[header[i]]['value']))
                    ubahData = vstackX((ubahData, temp))
                    #print '======================================='
                    #print ubahData

                    
                    # if(counter%100==0) :

                    # thread.start_new_thread(send_data, ("%s\n" % (headset.sensors['F8']['value']-mean), webS, ))

                #if not :
                 #   print("Stopped")
                  #  headset.stop()
            except Exception, e:
                print("Error di get_data : "+str(e))
                headset.stop()
            time.sleep(0.001)
        #headset.stop()
def send_data(data, ws):
    #print(data)
    try:
        ws((u""+data))
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
                thread.start_new_thread(get_data, (self.sendMessage, 2, ))
                #print("Hai")
            except Exception, e:
                print("Error: " + str(e))
        elif self.data == 'STOP':
            isRunning = False

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        global isRunning
        isRunning = False
        print(self.address, 'closed')



server = SimpleWebSocketServer('127.0.0.1', 8080, SimpleEcho)

server.serveforever()
			
