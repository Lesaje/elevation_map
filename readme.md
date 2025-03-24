# ASCII Elevation to Grayscale Image

This script converts elevation data (in ASCII grid format) into a grayscale image, where **white = high elevation** and **black = low elevation**. Useful for quick visualization of terrain data.

## 🗺 Example Data Source

Download elevation data from OpenTopography:

👉 [OpenTopography - SRTMGL1 (1 arc-second)](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.042013.4326.1)

1. Click **"Download data"**
2. Select a region (box or polygon)
3. Choose output format: **ArcASCII (.asc)**
4. Download and unzip the file

## 🛠 Requirements

```bash
pip install numpy Pillow
