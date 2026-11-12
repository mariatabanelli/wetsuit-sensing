# Testing workflow

## 1. Swatches

Three constructions on 2 mm neoprene, each with two sew-on snaps and 2-ply silver conductive thread:

1. conductive routes only: base layout and connection points
2. route plus a single-layer conductive fabric zone
3. route plus conductive fabric, Velostat underneath, stretch cover strip

The distinction held throughout: a route carries the signal, a zone changes under deformation.

## 2. Multimeter

Probes across the two snaps, at rest and under bend, for each swatch. The aim is comparison between constructions, not calibrated values.

## 3. Logging

`logging/readData.py` opens the port, asks for a movement name, and records to `data/<movement>_<timestamp>.csv` while a take is running.

The movement takes recorded in January 2025 (swim, dance, flex, fly, hand, hold, palm, ski, eat, clap, chest, sad) used two MyoWare EMG sensors on bicep and knee (`firmware/myoware_emg_two_channel`), as a reference for how the body moves in each action. The textile zones are read with the same pipeline through `firmware/xiao_esp32s3_two_channel`; swatch readings so far are bench tests, and full-suit takes follow the embroidery.

## 4. Reduction

Each take is normalised 0 to 1 and summarised as three values: bend intensity, repetition frequency, left to right asymmetry.

## 5. Outputs

- `plots/`: one radial plot per take, several drawing modes
- TouchDesigner: the three values reshape a point-cloud figure in real time
- rule table: thresholds on the three values map to design actions (expansion, seam migration, zip shift, release panel), draped in CLO3D as speculative garments

## 6. Placement

Zones are placed where the upper body deforms most in the recorded movements: shoulders, scapulae, centre back, upper arms, side torso. Full-suit embroidery is the next step, followed by calibration and durability testing.
