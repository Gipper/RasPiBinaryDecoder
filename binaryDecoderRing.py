#!/usr/bin/env python
 
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os

import pygame
from pygame.locals import *

import binascii
 
DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1400, 400))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Set the font
    font = pygame.font.Font(None, 150)
    bigfont = pygame.font.Font(None, 250)
    # Display the sensor reading from photosensor on pin 18
    # init the low, high and baseline values here
    signal = font.render("high", 1, (10, 10, 10))
    signaltextpos = signal.get_rect()
    signaltextpos.centerx =  140
    background.blit(signal, signaltextpos)
    
     # Display the low, high and baseline trigger indicator
    triggerVal = "LOW"
    trigger = font.render(triggerVal, 1, (10, 10, 10))
    triggertextpos = trigger.get_rect()
    triggertextpos.centerx = 1200
    background.blit(trigger, triggertextpos)
    
    # Display the current binary read buffer
    # init the decode buffer array of length 8
    binaryBufferVal = []
    binarybuffer = font.render(''.join(binaryBufferVal), 1, (10, 10, 10))
    binarybuffertextpos = binarybuffer.get_rect()
    binarybuffertextpos.centerx = 400
    binarybuffertextpos.centery = 150
    background.blit(binarybuffer, binarybuffertextpos)

    # Display the decode buffer
    # init the decode buffer array of a certain length (screen width)
    decodeBufferVal = []
    decodebuffer = bigfont.render(''.join(decodeBufferVal), 1, (10, 10, 10))
    decodebuffertextpos = decodebuffer.get_rect()
    decodebuffertextpos.centery = 300
    decodebuffertextpos.centerx = 20
    background.blit(decodebuffer, decodebuffertextpos)
    
    # Blit everything to the screen intially
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
 
     	background.fill(pygame.Color("white"))   
     	# compare signal delta against baseline
    	# if lower it will be "0" = laser is unimpeded
    	# if higher it will be "1" = laser is blocked
    	# push to binary buffer queue
     	signalVal = RCtime(18)
    	signal = font.render(str(signalVal), 1, (10, 10, 10))  
        background.blit(signal, signaltextpos)
        if signalVal > 1000 and triggerVal != "HIGH":
        	triggerVal = "HIGH"
        	trigger = font.render(triggerVal, 1, (10, 10, 10))
        	binaryBufferVal.append('1')
        elif signalVal < 200 and triggerVal != "LOW":
        	triggerVal = "LOW"
        	trigger = font.render(triggerVal, 1, (10, 10, 10))
        	binaryBufferVal.append('0')
        elif signalVal > 300 and signalVal < 900 and triggerVal != "BASE":
    		triggerVal = "BASE"
        	trigger = font.render(triggerVal, 1, (10, 10, 10))
        	
    	# if there are 8 bits, decode and push to decode queue, clear binary buffer
    	if len(binaryBufferVal) > 7:
    		# int base 2 on binary string to convert to decimal
    		intChar = int(''.join(binaryBufferVal), 2)
    		# then unhexlify into string 
    		if intChar > 0 and intChar < 255:
    			decodedChar = binascii.unhexlify('%x' % intChar)
    			if len(decodeBufferVal) > 13:
    				decodeBufferVal.pop(0)
    			decodeBufferVal.append(decodedChar)
    		binaryBufferVal = []
    	
    	# reset decode and binary buffers on key presses
    	for event in pygame.event.get() :
	    	if event.type == pygame.KEYUP :
	    		if event.key == pygame.K_SPACE :
	    			binaryBufferVal = []
	    		elif event.key == pygame.K_DELETE :
	    			decodeBufferVal.pop()
	    		elif event.key == pygame.K_ESCAPE :
	    			decodeBufferVal = []
    	
    	# if decode queue full, pop and dispose of front of decode display queue
    	# display changes to binary buffer and decode display queue	
        background.blit(trigger, triggertextpos)
        binarybuffer = font.render(''.join(binaryBufferVal), 1, (10, 10, 10))
        background.blit(binarybuffer, binarybuffertextpos)
        decodebuffer = bigfont.render(''.join(decodeBufferVal), 1, (10, 10, 10))
        background.blit(decodebuffer, decodebuffertextpos)
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()