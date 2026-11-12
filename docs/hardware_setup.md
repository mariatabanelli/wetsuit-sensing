# Hardware setup

## Materials

- 2 mm neoprene
- 2-ply silver-plated conductive thread, embroidered routes
- silver conductive fabric, active sensing zones
- Velostat, pressure-responsive layer under the fabric zone (swatch 3 and the suit)
- stainless sew-on snap connectors, two per zone, at the route terminations
- stretch cover strip over the zone for integration

## Electronics

- Seeed XIAO ESP32-S3
- breadboard, jumper wires, crocodile clips for bench tests
- multimeter

## Connection

Each zone ends in two snaps. One snap goes to an analogue input on the XIAO, the other to a digital pin held LOW. The analogue pin is set to `INPUT_PULLUP`, so the internal pull-up and the textile zone form a divider: as the zone compresses or bends and its resistance drops, the reading falls. No external resistor is needed for the bench tests.

Two channels are read at once (Analog1, Analog2).

## Movement reference takes

The January 2025 takes were recorded with two MyoWare muscle sensors (surface EMG, envelope output) on bicep and knee, read on A0 and A1 at 9600 baud. They are a reference for movement, not readings from the textile.

## Multimeter check

Before logging, each swatch is measured across its two snaps at rest and under bend, to compare the three constructions (route only, fabric zone, fabric plus Velostat) and to confirm the route carries signal while the zone changes under deformation.

## Note

This is prototype wiring for comparative testing. A conditioning circuit (fixed divider, RC filter) will be added when the full suit is calibrated.
