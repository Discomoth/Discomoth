import serial
import time
import os
import sys


counter = serial.Serial('/dev/ttyUSB0')
counter.baud = 9600
counter.timeout = 2

outputLocation = os.path.dirname(os.path.abspath(__file__))
print(outputLocation)

with open(outputLocation + '/output.txt', 'w'):
	pass

while True:

	if counter.in_waiting == 0:
		time.sleep(0.01)
	else:
		readValue = counter.readline().decode()

		with open(outputLocation + '/output.txt', 'a') as outputFile:
			cleanedData = str((readValue)).replace('FA', '')
			outputFile.write(cleanedData)
			print(cleanedData)
