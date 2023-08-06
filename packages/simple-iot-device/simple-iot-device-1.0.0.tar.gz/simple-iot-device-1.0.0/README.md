# Simple IOT Device

IOT device simulator.

The simulated device takes a number of measurements at some fixed point of time.

The measurements data returned as Python dictionary.

## IOT Device Measurements

- temperature, in °C;
- pressure, in kPa;
- relative humidity, in %;

## Basic Usage

```Python 3
    from simple_iot_device import SimpleIOTDevice
    
    # create Simple IOT Device
    device = SimpleIOTDevice(name="SDM-120230")
    
    # make measurement
    measurement = device.make_measurement()
    
    # print measurement result
    print(measurement)
```




