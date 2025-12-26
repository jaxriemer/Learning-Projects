import time

class SHT31:
    def __init__(self, i2c, addr=0x45):
        self.i2c = i2c
        self.addr = addr
        print(f"Initializing SHT31 at address {hex(addr)}")
        
        # Verify device is present
        if addr not in self.i2c.scan():
            raise Exception(f"SHT31 not found at address {hex(addr)}")
        print("Device found in scan")
    
    def read_temp_humidity(self):
        print("Attempting to read temperature and humidity...")
        
        # Try method 1: Standard single-shot measurement
        try:
            print("Method 1: Trying standard command 0x2C 0x06")
            buf = bytearray([0x2C, 0x06])
            self.i2c.writeto(self.addr, buf)
            time.sleep_ms(20)
            data = bytearray(6)
            self.i2c.readfrom_into(self.addr, data)
            print(f"Method 1 SUCCESS! Data: {[hex(b) for b in data]}")
            return self._convert_data(data)
        except Exception as e:
            print(f"Method 1 failed: {e}")
        
        # Try method 2: Older command format
        try:
            print("Method 2: Trying command 0x24 0x00")
            buf = bytearray([0x24, 0x00])
            self.i2c.writeto(self.addr, buf)
            time.sleep_ms(50)
            data = bytearray(6)
            self.i2c.readfrom_into(self.addr, data)
            print(f"Method 2 SUCCESS! Data: {[hex(b) for b in data]}")
            return self._convert_data(data)
        except Exception as e:
            print(f"Method 2 failed: {e}")
        
        # Try method 3: Using write + read without stop
        try:
            print("Method 3: Trying write without stop bit")
            buf = bytearray([0x2C, 0x06])
            self.i2c.writeto(self.addr, buf, False)  # No stop bit
            time.sleep_ms(20)
            data = bytearray(6)
            self.i2c.readfrom_into(self.addr, data)
            print(f"Method 3 SUCCESS! Data: {[hex(b) for b in data]}")
            return self._convert_data(data)
        except Exception as e:
            print(f"Method 3 failed: {e}")
        
        # Try method 4: Lower I2C frequency
        try:
            print("Method 4: Trying with lower I2C frequency")
            # Re-init I2C at lower speed
            old_freq = self.i2c
            self.i2c = SoftI2C(scl=self.i2c.scl, sda=self.i2c.sda, freq=100000)
            
            buf = bytearray([0x2C, 0x06])
            self.i2c.writeto(self.addr, buf)
            time.sleep_ms(20)
            data = bytearray(6)
            self.i2c.readfrom_into(self.addr, data)
            print(f"Method 4 SUCCESS! Data: {[hex(b) for b in data]}")
            return self._convert_data(data)
        except Exception as e:
            print(f"Method 4 failed: {e}")
            
        raise Exception("All read methods failed")
    
    def _convert_data(self, data):
        """Convert raw data to temperature and humidity"""
        # Temperature
        temp_raw = (data[0] << 8) | data[1]
        temp_c = -45 + (175 * temp_raw / 65535.0)
        
        # Humidity
        hum_raw = (data[3] << 8) | data[4]
        hum_rh = 100 * hum_raw / 65535.0
        
        return temp_c, hum_rh
    
    @property
    def temperature(self):
        temp, _ = self.read_temp_humidity()
        return temp
    
    @property
    def humidity(self):
        _, hum = self.read_temp_humidity()
        return hum