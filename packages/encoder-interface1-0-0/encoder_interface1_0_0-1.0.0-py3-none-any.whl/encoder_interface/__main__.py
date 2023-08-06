'''
    File name: main.py
    Version: v0.1
    Date: 23.12.2022
    Desc: Main python script file for software engineer assignment
'''

import time
from encoder_interface import EncoderInterface

if __name__ == '__main__':
	interface = EncoderInterface(64,16,19)
	interface.connect_interface()
	
	while 1:
		print(interface.read_encoder_data())
		time.sleep(0.1)
		

