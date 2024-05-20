import re
import cv2
import numpy as np

def plot_layers_gcode(gcode_file, num_layers):
    with open(gcode_file, 'r') as file:
        lines = file.readlines()

    coords = []

    layer_count = 0

    for line in lines:

        if line.startswith('G1') or line.startswith('G0'):

            x_match = re.search('X([0-9\\.]+)', line)
            y_match = re.search('Y([0-9\\.]+)', line)

            if x_match and y_match:
                coords.append((float(x_match.group(1)), float(y_match.group(1))))

        elif line.startswith(';LAYER:'):

            layer_count += 1

            if layer_count >= num_layers:
                break

    coords = np.array(coords)

    coords -= np.min(coords, axis=0)
    coords /= np.max(coords, axis=0)

    img_size = (500, 500)
    coords *= np.array(img_size)

    img = np.zeros((*img_size, 3), dtype=np.uint8)

    for i in range(1, len(coords)):
        cv2.line(img, tuple(coords[i-1].astype(int)), tuple(coords[i].astype(int)), (255, 255, 255), 1)

    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

plot_layers_gcode('chaveiro.gcode', 5)
