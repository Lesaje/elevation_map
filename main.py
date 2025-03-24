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

# Proper masking
masked_data = np.ma.masked_equal(data, nodata)

# Use percentiles to ignore outliers
p2 = np.percentile(masked_data.compressed(), 2)
p98 = np.percentile(masked_data.compressed(), 98)

# Clip and normalize
clipped = np.clip(masked_data, p2, p98)
normalized = (clipped - p2) / (p98 - p2) * 255
grayscale_data = normalized.filled(0).astype(np.uint8)  # Fill NODATA with black

# Step 4: Convert to image
image = Image.fromarray(grayscale_data, mode='L')
image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Optional: match geographic orientation

# Step 5: Save the image
image.save("elevation_image.png")
