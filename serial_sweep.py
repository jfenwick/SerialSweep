"""Control a servo over serial.

This is for a servo with angles from 20-165.
"""

import glob
import platform
import serial
from time import sleep

import atexit

# A function that tries to list serial ports on most common platforms
def list_serial_ports():
	system_name = platform.system()
	if system_name == "Windows":
		# Scan for available ports.
		available = []
		for i in range(256):
			try:
				s = serial.Serial(i)
				available.append(i)
				s.close()
			except serial.SerialException:
				pass
		return available
	elif system_name == "Darwin":
		# Mac
		return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
	else:
		# Assume Linux or something else
		return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

if __name__ == "__main__":
	# get all ports
	ports = list_serial_ports()

	# fiilter Arduino port
	arduinos = glob.glob('/dev/tty.usbmodem*')

	# select first arduino
	try:
		arduino = arduinos[0]
	except IndexError:
		print "No Arduinos found"

	print "Connecting to " + arduino

	pos = 20
	try:
		# connect to serial port
		ser = serial.Serial(arduino, 115200)
	except:
		print "Failed to connect to Arduino"

	# need a short delay right after serial port is started for the Arduino to initialize
	sleep(2)

	try:
		while True:
			print pos
			# get and print a line of data from Arduino
			#data = ser.readline()
			#if len(data) > 0:
			#	print data
			
			# write a position to the Arduino
			written = ser.write(str(pos))
			pos = pos + 1
			if pos > 165:
				pos = 20
			sleep(1.1)
	# close the serial port on exit, or you will have to unplug the Arduino to connect again
	finally:
		ser.close()