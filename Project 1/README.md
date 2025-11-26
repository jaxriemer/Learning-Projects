This is my very first project. I am excited!

Okay, well, ... it is not my first project. But the first one of hopefully many where I pick out random sensors and test out what I can make in a short period of time. The goal is not to make anything spectacualar or particiularly time-consuming, but rather a way to grow myself.

About me: I do not have a formal backgorund in electronics. I have had an interest in electronics since I was fairly young, but in a way that left more things broken than fixed. Now I would like to be able to deepenn my understanding of the hardware/software interface level. I got my undergraduate degree in Mechanical Engineering, where I only scratched the surface of microcontrollers and programming. I am now working in a company where I am regularly working with integrated chips in sensors. This has left me at place beyond Arduinos and looking more into ESP32s and ARM microntrollers. And don't ask me what each of them is best for...at least not yet. I am still learning, and I want to get better. There is no end goal here. The only objective is to keep moving.



Project Name: Humdidity and Temperature Sensor\
Hardware: Arduino Nano (Clone), DHT11
Software: Arduino IDE

First Step: Let's look at the datasheet of the temperature and humidity sensor. The one I found on Mouser has four pins and not three like the one I have. What is going on?

I found a tutorial that shows the different models and how to connect them:

https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/

There is conflicting information about the pinouts of the sensor module. 

https://www.reddit.com/r/arduino/comments/tv7dpw/warning_elegoo_dht11_wiring/


I looked at a couple videos on YouTube. There seems to be conflicting information, but I am going to make my best guess and hope it works out.

Also, I had to switch to an Arduino Mega (clone) because I do not have the right cable. In any case, the principles here are the same.


Second Step: Let's try wiring the sensor and connecting to the Arduino IDE. I have done this many times before. There can sometimes be some troubleshooting needed when selecting the board and COM port.








