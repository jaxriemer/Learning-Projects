import machine
i2c = machine.I2C(scl=machine.Pin(12), sda = machine.Pin(11))

print("Scanning the I2C bus...")
devices = i2c.scan()

if len(devices) == 0:
  print("No I2C device")
else:
  print('i2c devices found:',len(devices))

for device in devices:
  print("Decimal address: ",device, " | Hex address: ", hex(device))

i2c.scan()