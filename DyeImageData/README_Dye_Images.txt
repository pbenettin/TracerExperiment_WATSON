# README processed sensor data

## General info

This readme file describes the processed dye image data.

The photos of slice 1L, 1R, 2L, and 2R were all taken on Sept. 13, in the morning after the first irrigation.
The photos of slice 3L and 3R were taken on Sept. 13, in the evening right after the second irrigation.
The photos of slice 4L and 4R were taken on Sept. 14, the morning after the second irrigation.

## Processed Data

Processed data were obtained by using the the code provided in "image_analysis_for_python3_adapted_new_v2.py" and running it in PyCharm.
A step-by-step explanation is provided in the PDF "Blue dye step by step instructions with screenshots.pdf"

The individual processed slice data are provided as 2D images named "sliceXX_data.txt", where XX goes from 1L to 4R (see slice scheme in figure TransectsScheme.png). The pixel size in each image is 1x1 cm. Rows indicate depth and columns indicate the lateral extent of the slice (rightward distance from the left side of the slice). Pixels can either take a value of 1 (presence of dye) or 0 (absence of dye).

For each slice, we also provide a summary table with the distribution of tracer presence at each depth. This was obtained by counting at each depth the number of pixels that contained tracer. 
