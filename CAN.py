import os
import can
import time

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

msg2 = can.Message(arbitration_id=0x0, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)

print('start connection')

while True:
	msg = can0.recv(0.05)
	print(msg)
	can0.send(msg2)
#	if msg is None:
#		print('No message was received')
	
	time.sleep(0.01)
		
os.system('sudo ifconfig can0 down')