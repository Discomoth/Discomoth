import serial
import time
import os
import sys
import string

filename = "output2"

counter = serial.Serial('/dev/ttyUSB1')
counter.baud = 9600
counter.timeout = 2
counter.flush()

output_location = os.path.dirname(os.path.abspath(__file__))
print(output_location)

with open(output_location + f'/{filename}.txt', 'w'):
	pass

start_time = time.time()
string_whitelist = [x for x in string.digits]
string_whitelist.append('.')

while True:
	try:
		if counter.in_waiting == 0:
			time.sleep(0.01)
		else:
			read_value = counter.readline().decode()

			with open(output_location + f'/{filename}.txt', 'a') as output_file:
				time_delta = time.time() - start_time
				cleaned_data = ''.join([x for x in read_value if x in string_whitelist])
				output_file.write(f"{time_delta},{cleaned_data}\n")
				print(f"{time_delta}:{cleaned_data}")
	except KeyboardInterrupt:
		quit()
	except Exception as E:
		raise E
