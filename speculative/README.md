# speculative

The branch that turns values into form, run on simulated data while the full suit is unfinished.

- `speculative_sensor_data.py` writes `speculative_sensor_data.csv` with random intensity, direction, vibration and speed, one row a second. Replace `simulate_sensor_data()` with real readings when the suit is calibrated.
- `generate_svg_patterns.py` reads that CSV and draws overlapping C-curves and bean shapes to `speculative_garment_shapes.svg`, the starting geometry for the rule-table garments draped in CLO3D.

These values are simulated and are labelled as such on the project page. The recorded takes in `data/` are real.
