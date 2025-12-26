One project down, and I am feeling like a challenge. As I have mentioned in my previous post, most of my experience with microcontrollers comes with the Arduino Ecosystem. This was sufficient for fulfilling my individual curiosities, but I am hitting roadblocks in my current job when working with highly specific sensors that have high-performance criteria. For this, I need something more powerful. It is time to get my feet wet with the ESP32. My goal is to do the same thing I just did in the previous project. This time I will be using a temperature and humidity sensor, DFRobot's SHT31 and the Arduino Nano with an ESP32 onboard. But first, I want to better understand the differences in the hardware capabilities of the ESP32 and what I have worked with before.

I will use the Arduino Uno as my benchmark to compare with the ESP32 chip. The first thing I notice when comparing the two is the difference in processors. The Uno uses an 8-bit ATmega328P operating at 16MHz, whereas the ESP32 uses a 32-bit LX6 processor at 160MHz or 240MHz. These are not all of the details, but these seem like the ones worth reviewing at the beginning. So what difference do the number of bits and the operating speed make?

The number of bits can be thought of as the size of a spoon. The bigger then spoon, the more that can be eaten at a time. The greater the number of bits, the more data that can be processed at one time. The operating speed is how many times the food can be placed on the spoon and eaten for a given period of time, or how many cycles of data processing can be done in a second. Together, the number of bits and operating speed indicate the speed at which data can be processed. The ESP32 has a great advantage over the Uno.

Another big difference is that the ESP32 is a System on a Chip (SoC)



I decided to go aheaad and set up my host machine so that I can write programs for the Arduino Nano ESP32. Arduino allows for their devices with an ESP32 chip to be programmed using MicroPython, compatible with Arduino Lab. This IDE is in the same style as their exisiting Arduino IDE. This is a helpful step for me since I will already be working within an IDE that I am familiar with. MicroPython is a light version of Python 3, which is also a programming language that I have experience with.

First step is to download MicroPython installer and upload the firmware to the Arduino Nano ESP32.
https://labs.arduino.cc/en/labs/micropython-installer

Next is to install Arduino Lab for MicroPython.
https://labs.arduino.cc/en/labs/micropython

A walkthrough tutorial from ArduinoDocs gets me start with understanding the file system.
https://docs.arduino.cc/micropython/first-steps/intro-micropython/

Reading through, the first thing I notice is the modularity of this coding style. That makes me super excited, because that was one major limitation I had with using the regular Arduino IDE. Also there is no need to compile so interacting with my board as I develop the code becomes more seamless.

The first thing I do when working with a sensor, is open the datasheet. I take a brief runthrough of all of the documentation, focusing more on the sections that deal directly with hardware connections, and basic information related to establishing the fundamental communication between my sensor and Arduino Nano ESP32.

Since the SHT31 uses I2C protocol, I will need the I2C Peripheral Address. This is the address that the Arduino Nano ESP32 "call out" to, when first establishing connections onto the I2C bus. Looking in the datasheet, this default address is either 0x44 or 0x45, depending on the optional hardware configuration on the sensor itself. I have also included an I2C scanner script that will search for the I2C device and return its address. Using this script, I confirmed that my device address is 0x45.

[I2C Scanner](https://github.com/jaxriemer/Learning-Projects/blob/main/Project%202/scan.py)

Next, to make my life easier I searched online (GitHub) for a SHT31 library. This simplifies coding greatly as it already has functions defined and written for this particular sensor. I found an arduino library and python library through Adafruit but they were not working properly for me. The arduino library will not work because it is meant for C++, and I working with MicroPython. I thought the Python library would work, but I think it is meant for Raspberry Pis. In any case, I used Claude AI to write a library. This is not my preferred method, but for this simple project it will suffice. It is worth noting that, in my experience, using AI to write code for embedded systems is rarely a prompt and answer case. There is iterations needed to get a functioning code. In my opinion, even when the code is functional, it is hardly robust. That is just my opinion though.

Here is the library that was constructed using Claude AI:
[SHT31 Library](https://github.com/jaxriemer/Learning-Projects/blob/main/Project%202/sht31.py)

