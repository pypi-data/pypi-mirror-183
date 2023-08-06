# TA-CMI
A Python wrapper to read out  sensors from Technische Alternative using the C.M.I.

## How to use package

```python
import asyncio

from ta_cmi import CMI, Languages, ApiError, RateLimitError, InvalidCredentialsError, InvalidDeviceError, ChannelType


async def main():
    try:
        cmi = CMI("http://192.168.1.101", "admin", "admin")

        devices = await cmi.get_devices()

        device = devices[0]

        # Set type automatically
        await device.fetch_type()

        # Set type manually
        device.set_device_type("UVR16x2")

        await device.update()

        print(str(device))

        inputChannels = device.get_channels(ChannelType.INPUT)
        outputChannels = device.get_channels(ChannelType.OUTPUT)
        analogLogging = device.get_channels(ChannelType.ANALOG_LOGGING)

        for i in inputChannels:
            ch = inputChannels.get(i)
            print(str(ch))

        for o in outputChannels:
            ch = outputChannels.get(o)
            print(f"{str(ch)} - {ch.get_unit(Languages.DE)}")

        for al in analogLogging:
            ch = analogLogging.get(al)
            print(f"{str(ch)} - {ch.get_unit(Languages.DE)}")

    except (ApiError, RateLimitError, InvalidCredentialsError, InvalidDeviceError) as error:
        print(f"Error: {error}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```