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




I am back on my second day working on this. I left off having thought I connected everything properly to my sensor, but I just end up with values of 0.0. I also left my Mega at work so I am now using the Leonardo I had bought many years ago without ever removing from the package. I guess that is an advangtage of using the Arduino ecosystem. It is pretty easy to move between the different microcontollers without having to change much, if any of the code. There are hardware differences between the different models, but for a simple project like this, it is not really relevant.

Anyway, I took a look at the hardware setup on my breadboard and I had a thought. I stuck my sensor module directly into my breadboard and front face of the sensor was pushed down directly into the breadboard and on top of my connecting wires. I swapped out my breadboard for some wires that connect my Leonardo directly to my sensor module and my values came out looking more as how I might expect.

The analog to digital conversion on this board is 8-bits. In other words, digitalized signal is represented in a way that is limited to the number of levels that can be respresented by 8-bits. Without getting to deep into binary code and other concepts, just know that 8-bits can represent values from 0-255. (To know how many levels calculate 2 to the power of the number of bits. For 8-bits, 2^8 = 256. Since zero counts as a level, values 0-255 can be represented.)

So now I need to take this data and convert it to something meaningful. It is back to the datasheet to see how this digitalized signal can be converted to temperature and humidity. Looking back at the datasheet, there is no conversion provided. Considering the values I get, it is more than reasonable to assume that the library provided with the sensor does this conversion already. I might come back to this if I decide to do the bare metal coding myself. In any case, I did find some other interesting information about my sensor when looking through the datasheet again. I have a sense that I will find something new every time I look back. The most important thing I found is that I should not be sampling my sensor more than once a second. I was surprised! In past project I never really considered timing much, but it is important at my current job at work. However, I am working with a much more complicated chip than the one on my sensor module, and it can be sampled every 10s of milliseconds, not every 1 second. This is important for me to know if I want to implemenent algorithms such as the average of my sensor readings.







