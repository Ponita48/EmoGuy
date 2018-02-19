# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time
import socket
import thread
import numpy as np
import os
import json

from emokit.emotiv import Emotiv
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import preprocessing as prp

# Ini buat apa? if tapi isinya kosong
if platform.system() == "Windows":
    pass
isRunning = False

def get_data(webS, delay):
    # Set default value
    header = ['F3','F4','F7','F8','AF4','AF3','FC5','FC6','P7','P8','T7','T8','O1','O2']
    old_data = ""
    vstackX = np.vstack
    appendX = np.append
    arrayX = np.array
    zeros = np.zeros
    ubahData = arrayX(header)
    bpass = prp.bandpass
    dc_off = prp.dcOffset
    put = np.put
    dump = json.dumps
    counter = 0
    mean = 3000
    sampling = 128

    # Connect to emotiv
    print "Connection Started at"
    with Emotiv(display_output=False, verbose=True, write=False) as headset:
        dequeue = headset.dequeue
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")
        while headset.running and isRunning:
            try:
                dequeue()
                if old_data != ("%s\n" % headset.sensors) :
                    old_data = "%s\n" % headset.sensors
                    # counter kepake gak? kalo gak kepake hapus aja
                    # print counter

                    # data yang diambil real time
                    temp = headset.sensors[header[0]]['value']
                    bp_send = zeros(sampling)
                    for i in xrange(1, 14):
                        temp = appendX(temp, arrayX(headset.sensors[header[i]]['value']))
                    if counter % sampling == 0 and counter is not 0:
                        bp = dc_off(ubahData, True)
                        bp, bpABG = bpass(bp, True)
                        print json.dumps(bp.tolist())
                        thread.start_new_thread(send_data, ("%s\n" % (dump(bp.tolist())), webS, ))
                        ubahData = vstackX((arrayX(header), ubahData[sampling:]))
                    ubahData = vstackX((ubahData, temp))
                    counter += 1
            except Exception, e:
                print("Error di get_data : "+str(e))
                headset.stop()
            time.sleep(0.001)

def send_data(data, ws):
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

print "Starting Connection"
server.serveforever()
			
