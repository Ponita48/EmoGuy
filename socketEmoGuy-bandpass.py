# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time
import socket
import thread
import numpy as np
import json
import os
from emokit.packet import EmotivExtraPacket

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
    bpass = prp.bandpassX
    dc_off = prp.dcOffset
    put = np.put
    dump = json.dumps
    counter = 0
    mean = 3000
    sampling = 128
    bp = None
    startThread = thread.start_new_thread
    # Connect to emotiv
    print "Connection Started at"
    with Emotiv(display_output=False, verbose=True, write=True) as headset:
        dequeue = headset.dequeue
        print("Serial Number: %s" % headset.serial_number)
        print("Exporting data... press control+c to stop.")
        while headset.running and isRunning:
            try:
                packet = dequeue()
                if (packet is not None) and type(packet) is not EmotivExtraPacket :
                    # old_data = "%s\n" % headset.sensors
                    # counter kepake gak? kalo gak kepake hapus aja
                    # print counter

                    # data yang diambil real time
                    sensors = packet.sensors
                    temp = arrayX([])
                    # bp_send = zeros(sampling)
                    for i in header:
                        #print header[i]
                        temp = appendX(temp, sensors[i]['value'])
                    if counter % sampling == 0 and counter is not 0:
                        bp = dc_off(ubahData, True)
                        bp, bpABG = bpass(bp,vstackX,arrayX,zeros, True)
                        print json.dumps(bp.tolist())
                        bp = bp.T
                        thread.start_new_thread(send_data, ("%s\n" % (dump(bp.tolist())), webS, ))
                        ubahData = vstackX((arrayX(header), ubahData[sampling:]))
                        # print bp
                        # print bp.shape
                        # print ubahData.shape
                        # print temp
                        # print ubahData
                        # print bp
                        # break
                    ubahData = vstackX((ubahData, temp))
                    print counter
                    counter += 1
            except Exception, e:
                print("Error di get_data : "+str(e))
                headset.stop()
            time.sleep(0.001)
        f = open( 'file.py', 'w' )
        f.write( dump(bp.tolist()) )
        f.close()

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
			
