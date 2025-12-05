One project down and I am feeling like a challenge. As I have mentioned in my previous post, most of my experience with microcontrollers comes with the Arduino Ecosystem. This was sufficient for fulfilling my individual curiosities, but I am hitting roadblocks in my current job when working with highly specific sensors that have high performance criteria. For this I need something more powerful. It is time to get my feet wet with the ESP32. My goal is to do the same thing I just did in the previous project. This time I will be using a temperature and humidity sensor, DFRobot's SHT31 and the Arduino Nano with an ESP32 onboard. But first, I want to better understand the differences in the hardware capabilities of the ESP32 and what I have worked with before.

I will use the Arduino Uno as my benchmark to compare with the ESP32 chip. The first thing I notice when comparing the two is the difference in processors. The Uno uses an 8-bit ATmega328P operating at 16MHz, whereas the ESP32 uses a 32-bit LX6 processor at 160MHz or 240MHz. These are not all of the details, but these seem like the ones worth reviewing at the beginning. So what difference do the number of bits and the operating speed make?

The number of bits can be thought of as the size of a spoon. The bigger then spoon, the more that can be eaten at a time. The greater the number of bits, the more data that can be processed at one time. The operating speed is how many times the food can be placed on the spoon and eaten for a given period of time. Or, how many cycles of data processing can be done in a second. Together, the number of bits and operating speed indicate the speed with which data can be processed. It is clear that the ESP32 has a great advantage over the Uno.





