# firmware

- `xiao_esp32s3_two_channel/` reads two textile zones through the internal pull-up and prints `value1,value2` at 115200 baud. This is the wetsuit sketch (`Wetsuit_presure_sensor_code_and_test.ino`), with two typos fixed so it compiles (`kneeInPin` case, a missing semicolon) and the labelled debug prints replaced by plain CSV so `readData.py` can log it.
- `myoware_emg_two_channel/` reads two MyoWare muscle sensors (ENV pins A0 and A1) and prints the two envelopes in millivolts at 9600 baud. This is the sketch the January 2025 movement takes in `data/` were recorded with.
- `single_channel_test/` prints one analogue pin, the first bench test of a swatch.
