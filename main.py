import numpy as np
from PIL import Image

# Path to your ASCII file
ascii_file_path = "output_SRTMGL1.asc"

# Step 1: Read and parse the file
with open(ascii_file_path, 'r') as f:
    header = {}
    for _ in range(6):
        key, value = f.readline().split()
        header[key.lower()] = float(value) if '.' in value else int(value)

    # Extract header info
    ncols = header['ncols']
    nrows = header['nrows']
    nodata = header['nodata_value']

    # Step 2: Load the rest as elevation data
    data = np.loadtxt(f)

# Step 3: Mask and normalize data to 0-255
masked_data = np.ma.masked_equal(data, nodata)
min_val = masked_data.min()
max_val = masked_data.max()

# Normalize to 0–255 for grayscale
normalized = (masked_data - min_val) / (max_val - min_val) * 255
grayscale_data = normalized.filled(0).astype(np.uint8)  # Fill NODATA with black (0)

# Step 4: Convert to image
image = Image.fromarray(grayscale_data, mode='L')

# Step 5: Save the image
image.save("elevation_image.png")
