# Wetsuit as a Sensing System

E-textile sensing wetsuit: neoprene re-engineered from passive sportswear into the sensor itself.
Maria Tabanelli, with Felix Loftus. 2024, ongoing. Prototype stage.

Embroidered conductive routes carry the signal; conductive fabric and Velostat zones at the shoulders, scapulae and centre back change under deformation. Readings are logged over serial, reduced to three values (bend, frequency, asymmetry) and used to drive a live TouchDesigner figure and a rule table for derived garments.

Project page: https://mariatabanelli.com

## Pipeline

1. **Sense.** Embroidered 2-ply silver conductive thread routes, silver conductive fabric zones, Velostat pressure layer, sew-on snap connectors on 2 mm neoprene.
2. **Read.** A XIAO ESP32-S3 reads the zones as analogue channels and prints them over serial (`firmware/xiao_esp32s3_two_channel`). The movement takes in `data/` were recorded earlier with two MyoWare EMG sensors on the same pipeline (`firmware/myoware_emg_two_channel`), as the movement reference for placement and for the live figure.
3. **Log.** A Python script records the serial stream to timestamped CSV, one file per movement (`logging/`).
4. **Plot.** Each CSV is normalised 0 to 1 and drawn as a radial pattern (`plots/`, `outputs/`).
5. **Drive.** The same values feed a TouchDesigner network in real time (not in this repo; see the project page).
6. **Form.** A rule table maps the values to design actions; `speculative/` generates the starting geometry for the CLO3D garments from simulated values.

## Repository structure

```text
wetsuit-sensing/
├── README.md
├── LICENSE
├── requirements.txt
├── firmware/
│   ├── xiao_esp32s3_two_channel/      two textile zones, pull-up divider, CSV over serial
│   ├── myoware_emg_two_channel/       two MyoWare EMG envelopes, used for the January 2025 takes
│   └── single_channel_test/           first bench test of a swatch
├── logging/
│   └── readData.py                    serial to CSV, space bar starts and stops a take
├── plots/
│   └── radialDataGenerator.py         CSV to radial plot (line, bar, spiral, scatter, waveform, rose)
├── speculative/
│   ├── speculative_sensor_data.py     simulated values, stand-in until the suit is calibrated
│   └── generate_svg_patterns.py       values to C-curve and bean geometry (SVG) for the CLO3D garments
├── data/                              recorded takes, Timestamp,Analog1,Analog2
├── outputs/                           radial plots
└── docs/
    ├── hardware_setup.md
    └── testing_workflow.md
```

## Running it

```bash
pip install -r requirements.txt
python logging/readData.py          # choose port, name the movement, space bar to start and stop
python plots/radialDataGenerator.py # set file_path and the plot option at the top of the script
```

Set `port` and `baud_rate` at the top of `readData.py` to match the sketch: 9600 for the MyoWare sketch, 115200 for the XIAO textile sketch. The firmware prints `analog1,analog2` per line; `readData.py` prepends a Unix timestamp and writes `Timestamp,Analog1,Analog2`.

## Status

Sensing swatches and the recording workflow work. Next: full-suit embroidery, calibration against repeated movement, durability testing.

## Licence

Code: MIT (see LICENSE). Photographs, drawings and text: © Maria Tabanelli, all rights reserved.
