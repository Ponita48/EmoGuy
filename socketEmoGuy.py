# This is an example of popping a packet from the Emotiv class's packet queue
# Additionally, exports the data to a CSV file.
# You don't actually need to dequeue packets, although after some time allocation lag may occur if you don't.


import platform
import time
import socket
import thread
import os
from emokit.emotiv import Emotiv
import matplotlib.pyplot as plt
from emokit.packet import EmotivExtraPacket
import numpy as np
import json
import preprocessing as prp

if platform.system() == "Windows":
	pass
isRunning = False
header = ['F3','F4','F7','F8','AF4','AF3','FC5','FC6','P7','P8','T7','T8','O1','O2']
populated_data = np.zeros(14) # tanpa header
# populated_data = np.array(header) #pake header

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
def get_data(webS, delay):
	old_data = ""
	print "Connection Started at"
	with Emotiv(display_output=False, verbose=True, write=True) as headset:
		print("Serial Number: %s" % headset.serial_number)
		print("Exporting data... press control+c to stop.")
		dequeue = headset.dequeue
		counter = 0
		vstackX = np.vstack
		dump = json.dumps
		mean = 3000.0;
		data = []
		bpass = prp.bandpassX
		dc_off = prp.dcOffset
		while headset.running and isRunning:
			try:
				#packet = headset.dequeue()
				packet = dequeue()
				#print "test"
				if (packet is not None) and type(packet) is not EmotivExtraPacket:
					counter=counter+1
					print counter
					#print packet.sensors
					# print "%s\n" % headset.sensors				
					thread.start_new_thread(send_data, ("%s\n" % (packet.sensors), webS, ))
					thread.start_new_thread(populate_data, (packet.sensors, ))
				#if not :
				 #   print("Stopped")
				  #  headset.stop()
			except Exception, e:
				print("Error di get_data : "+str(e))
				headset.stop()
			time.sleep(0.001)
		headset.stop()
		np.savetxt("saved-raw.csv", populated_data, delimiter=",")
		bp = dc_off(populated_data, True)
		np.savetxt("saved-dcoff.csv", bp, delimiter=",")
		bp, bpABG = bpass(bp, True)
		np.savetxt("saved-bandpass.csv", bp, delimiter=",")
		np.savetxt("saved-bandpass(delta).csv", bpABG[0], delimiter=",")
		np.savetxt("saved-bandpass(theta).csv", bpABG[1], delimiter=",")
		np.savetxt("saved-bandpass(alpha).csv", bpABG[2], delimiter=",")
		np.savetxt("saved-bandpass(beta).csv", bpABG[3], delimiter=",")
		#headset.stop()
def send_data(data, ws):
	#print(data)
	try:
		ws((u""+data))
	except Exception, e:
		print("Error di send_data :" + str(e))

def populate_data(data):
	#print(data)
	global populated_data
	try:
		temp = np.array([])
		appendX = np.append
		for i in header:
		    #print header[i]
		    temp = appendX(temp, data[i]['value'])
		populated_data = np.vstack((populated_data, temp))
	except Exception, e:
		print("Error di populate_data :" + str(e))

def butter_bandpass_filter(data, lowcut, highcut, sampleRate, order=2):
	b, a = butter_bandpass(lowcut, highcut, sampleRate, order=order)
	y = lfilter(b, a, data.astype(np.float))
	return y

def butter_bandpass(lowcut, highcut, sampleRate, order = 2):
	nyq = 0.5 * sampleRate
	low = lowcut / nyq
	high = highcut / nyq
	b, a = butter(order, [low, high], btype = 'band')
	return b, a

class SimpleEcho(WebSocket):
	# Define a function for the thread
	def handleMessage(self):
		# echo message back to client
		global isRunning
		data = u"Hallo"
		#self.sendMessage(data)
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
			
