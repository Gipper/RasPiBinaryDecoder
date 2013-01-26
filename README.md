RasPiBinaryDecoder
==================

Looks for HIGH/LOW/BASE values from GPIO pin 18 of a RaspberryPi and translates binary into displayed string.

A very quick build using Adafruit's Learning build and PyGame to read and display info on screen. If you are using Adafruit's Pi Distro, all modules should be included already. :) 

![RaspiDecoder](http://gipper.github.com/RasPiBinaryDecoder/images/RaspiDecoder.png)


Here's how this goes down:

1. Get a nice coherent laser. This one was obtained from: www.surplusgizmos.com. Surplus Gizmos rocks, you should get yourself there right now and say hello to Mike.

2. Punch out some holes in a suitable medium for the laser to shine through. An empty laminated sheet works nicely. These will be your HIGH (or Binary 0 Value)

3. Note that you need to record DEVIATION from a baseline value. Think about the nightmare involved in timing your pulses otherwise. 3 or 4 layers of Scotch Tape is a perfect median baseline which permits about 50% of the laser to transmit.

4. Use a Black Sharpie to prevent the laser from transmitting. This will be your LOW (or Binary 1 value)

5. Shine the laser on a Photoresistor which sends input to GPIO pin 18. Take a look at www.adafruit.com for some ideas. Adafruit rocks, you should get yourself there right now and say hello to Limor. ;)

6. Pull your letters through the laser beam and cause the modulation. In this Rig, the beam was sent to the target through a discarded optical cable for extra effect.

7. This is more of an example of how HARD it is to send information optically, and how amazing it is that most of the worlds information is encoded optically at some point. :)

(http://gipper.github.com/RasPiBinaryDecoder/images/BinaryLetters.png)