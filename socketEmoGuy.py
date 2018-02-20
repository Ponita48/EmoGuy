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

if platform.system() == "Windows":
	pass
isRunning = False

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
def get_data(webS, delay):
	old_data = ""
	print "Connection Started at"
	with Emotiv(display_output=False, verbose=True, write=True) as headset:
		print("Serial Number: %s" % headset.serial_number)
		print("Exporting data... press control+c to stop.")
		dequeue = headset.dequeue
		counter = 0
		mean = 3000.0;
		data = []
		while headset.running and isRunning:
			try:
				#packet = headset.dequeue()
				packet = dequeue()
				#print "test"
				if (packet is not None) and type(packet) is not EmotivExtraPacket:
					old_data = "%s\n" % headset.sensors
					counter=counter+1
					print counter
					#print packet.sensors
					# print "%s\n" % headset.sensors				
					thread.start_new_thread(send_data, ("%s\n" % (headset.sensors), webS, ))
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
			
