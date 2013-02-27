RasPiBinaryDecoder
==================

Looks for HIGH/LOW/BASE values from GPIO pin 18 of a RaspberryPi and translates binary into displayed string.

A very quick build using Adafruit's Learning build and PyGame to read and display info on screen. If you are using Adafruit's Pi Distro, all modules should be included already. :) 

![RaspiDecoder](http://gipper.github.com/RasPiBinaryDecoder/images/RaspiDecoder.png)


Project Background/History
==================

This project was developed to present the concepts of optical data encoding to a grade school audience. One of the extra activities at our local school is a family science night where families develop and present demonstrations to each other. I had just picked up a used bench laser, and was considering methods to modulate the beam so that information could be sent across the room. Modulating the laser in some way electronically would be a great project, but I was getting a bit worried as we were less than a week out from the event.

Meanwhile my 4th grader was nearby and was having a great time constructing a "secret code", so I looked over and saw it was a worksheet that translated ASCII letters to binary. As he was filling in the ones and zeros I realized that if we could drag this across the laser beam, causing an interruption, we could send our code. I'd already thought about using the Pi as the receiver, so we rigged up the photosensor and started to pull a sheet of paper across the beam to measure some flashes.

It didn't take long to start thinking about how to separate two discrete digits of the same value. You may think to solve this issue by timing the length of the pulses. Although you CAN solve the issue this way, in this case there wasn't a practical way to do it. Ideas of rolling a sled downhill and robotically pulling the digits through were quickly discarded.

Thinking back to some signal processing classes in college yielded the answer. By continuously sending a baseline signal, and then recording the increase and decrease of this signal, timing clock issues are completely avoided. This is, in fact, closer to how optical information is encoded. Look up In-Pit and On-pit and you'll find various documents that explain the modulation of DVD-ROM's, etc. using this technique. Beam modulation in high density fiber cables is also similar (but a LOT more complex).

![InOnPit](http://gipper.github.com/RasPiBinaryDecoder/images/InOnPit.png)

We conclusively proved this approach by adding a bit of scotch tape to act as the substrate that the "Pits" and "Holes" could then be modified upon. We used a marker to block the beam, and a hole punch to allow it. After this modification we could pull coded letters through the beam at any speed with no trouble. You could even leave the code in place halfway through the sequence, come back the next day, and complete the transmission.

In the remaining time we made the binary codes for each letter and attached them to straws to make them easier to push through the beam by threading the straw into the channel bar that held the laser rig. Eventually, I attached an old optical cable and fed the beam into it, with the other end near the photoresistor. The RaspberryPi code was trival, largely due to using Adafruit's Learning System and BitBucket-Based IDE. Realizing that pyGame was already included, as well as everything needed to handle the Raspberry pins, was a stroke of good luck.

It was amazing how transfixed even young kids were as they watched the letters appear on screen exactly as they had arranged the physical representations. Since this process happens around the world trillions upon trillions of times every microsecond, but is largely hidden to us, it was entertaining to see a super-slow speed demonstration. It was also a good time to remind kids that they are driving around with a laser in their car (pew pew), and that there are lasers in MANY places you may not expect.

Materials
==================

15 mW Bench laser - $30 (a laser pointer would probably work fine)

RasberryPi - $35

Adafruit Pi Cobbler - $8

Two Meters of 80/20 channel - $20

Scotch Tape (opaque, not the clear stuff)

Laminated Sheets (empty, heat sealed)

Black Marker

Hole Punch (if you have a vertical slot type, used for scrapbooking, you can fit more letters in a smaller space)


Build Time
==================

Laser mount and POC/research: 2 hours

RaspberryPi photoresistor and rig: 30 mins

Python sensor code and display code: 45 mins

Making the binary letter representations: 4 hours


![BinaryLetters](http://gipper.github.com/RasPiBinaryDecoder/images/BinaryLetters.png)


Basic Workflow
==================

1. Get a nice coherent laser. This one was obtained from: www.surplusgizmos.com. Surplus Gizmos rocks, you should get yourself there right now and say hello to Mike.

2. Punch out some holes in a suitable medium for the laser to shine through. An empty laminated sheet works nicely. These will be your LOW (or Binary 0 Value)

3. Note that you need to record DEVIATION from a baseline value. Think about the nightmare involved in timing your pulses otherwise. 3 or 4 layers of Scotch Tape is a perfect median baseline which permits about 50% of the laser to transmit.

4. Use a Black Sharpie to prevent the laser from transmitting. This will be your HIGH (or Binary 1 value)

5. Shine the laser on a Photoresistor which sends input to GPIO pin 18. Take a look at www.adafruit.com for some ideas. Adafruit rocks, you should get yourself there right now and say hello to Limor. ;)

6. Pull your letters through the laser beam and cause the modulation. In this rig, the beam was sent to the target through a discarded optical cable for extra effect.

7. This is more of an example of how HARD it is to send information optically, and how amazing it is that most of the worlds information is encoded optically at some point. :)





