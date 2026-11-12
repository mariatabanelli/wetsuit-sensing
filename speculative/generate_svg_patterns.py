import csv
import svgwrite
import math

def create_c_curve(intensity, direction, center_x=0, center_y=0, radius=50, sweep_angle=math.pi):
    """Generates SVG path data for a C-curve (arc-based)."""
    start_angle = direction - sweep_angle / 2
    end_angle = direction + sweep_angle / 2
    start_x = center_x + radius * math.cos(start_angle)
    start_y = center_y + radius * math.sin(start_angle)
    end_x = center_x + radius * math.cos(end_angle)
    end_y = center_y + radius * math.sin(end_angle)
    large_arc_flag = 0 if sweep_angle <= math.pi else 1
    path_data = f"M {start_x},{start_y} A {radius},{radius} 0 {large_arc_flag},1 {end_x},{end_y}"
    return path_data

def create_elongated_bean(intensity, direction, center_x=100, center_y=100, length=80, width=30, bulge=20):
    """Generates SVG path data for an elongated bean shape."""
    angle_offset = direction
    p1_x = center_x + length / 2 * math.cos(angle_offset)
    p1_y = center_y + length / 2 * math.sin(angle_offset)
    p2_x = center_x - length / 2 * math.cos(angle_offset)
    p2_y = center_y - length / 2 * math.sin(angle_offset)

    ctrl1_angle = angle_offset + math.pi / 2
    ctrl1_x = center_x + bulge * math.cos(ctrl1_angle) + length / 4 * math.cos(angle_offset)
    ctrl1_y = center_y + bulge * math.sin(ctrl1_angle) + length / 4 * math.sin(angle_offset)

    ctrl2_angle = angle_offset + math.pi / 2
    ctrl2_x = center_x + bulge * math.cos(ctrl2_angle) - length / 4 * math.cos(angle_offset)
    ctrl2_y = center_y + bulge * math.sin(ctrl2_angle) - length / 4 * math.sin(angle_offset)

    ctrl3_angle = angle_offset - math.pi / 2
    ctrl3_x = center_x + bulge * math.cos(ctrl3_angle) - length / 4 * math.cos(angle_offset)
    ctrl3_y = center_y + bulge * math.sin(ctrl3_angle) - length / 4 * math.sin(angle_offset)

    ctrl4_angle = angle_offset - math.pi / 2
    ctrl4_x = center_x + bulge * math.cos(ctrl4_angle) + length / 4 * math.cos(angle_offset)
    ctrl4_y = center_y + bulge * math.sin(ctrl4_angle) + length / 4 * math.sin(angle_offset)

    path_data = f"M {p1_x},{p1_y} C {ctrl1_x},{ctrl1_y} {ctrl2_x},{ctrl2_y} {p2_x},{p2_y} C {ctrl3_x},{ctrl3_y} {ctrl4_x},{ctrl4_y} {p1_x},{p1_y} Z"
    return path_data

def generate_svg(data, filename="speculative_garment_shapes.svg"):
    """Generates an SVG file with overlapping C and bean shapes."""
    dwg = svgwrite.Drawing(filename=filename, profile='tiny', viewBox=(0, 0, 400, 400))
    center_x = 200
    center_y = 200

    for i, row in enumerate(data):
        try:
            timestamp, intensity, direction, vibration, speed = row
            intensity = float(intensity) * 0.8 + 0.2  # Scale intensity
            direction = float(direction)
            offset_x = 50 * math.cos(direction * 2 + i * 0.5)
            offset_y = 50 * math.sin(direction * 2 + i * 0.5)
            scaled_radius = 30 + intensity * 40
            scaled_length = 60 + intensity * 60
            scaled_bulge = 15 + intensity * 25

            # Overlapping C-curves
            c_curve1 = create_c_curve(intensity, direction + i * 0.2, center_x + offset_x, center_y + offset_y, radius=scaled_radius, sweep_angle=math.pi * 1.2)
            c_curve2 = create_c_curve(intensity * 0.8, direction - i * 0.3, center_x + offset_x - 20, center_y + offset_y + 20, radius=scaled_radius * 0.7, sweep_angle=math.pi * 1.5)
            dwg.add(dwg.path(d=c_curve1, fill='none', stroke='purple', stroke_width=2, opacity=0.7))
            dwg.add(dwg.path(d=c_curve2, fill='none', stroke='teal', stroke_width=2, opacity=0.7))

            # Elongated bean shapes
            bean1 = create_elongated_bean(intensity, direction + math.pi / 4 + i * 0.4, center_x + offset_x + 30, center_y + offset_y - 30, length=scaled_length, width=scaled_length * 0.3, bulge=scaled_bulge)
            dwg.add(dwg.path(d=bean1, fill='none', stroke='orange', stroke_width=2, opacity=0.7))

        except ValueError as e:
            print(f"Error processing row: {row} - {e}")
        except IndexError:
            print(f"Error: Incomplete data in row: {row}")

    dwg.save()
    print(f"Generated speculative garment shapes in {filename}")

if __name__ == "__main__":
    import math
    sensor_data = []
    try:
        with open("speculative_sensor_data.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                sensor_data.append(row)
    except FileNotFoundError:
        print("Error: speculative_sensor_data.csv not found. Run speculative_sensor_data.py first.")
        sensor_data = []

    if sensor_data:
        generate_svg(sensor_data)
    else:
        print("No speculative sensor data to generate shapes from.")