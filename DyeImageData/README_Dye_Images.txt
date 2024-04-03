# README processed sensor data

## General info

This readme file describes the processed dye image data.

The photos of slice 1L, 1R, 2L, and 2R were all taken on Sept. 13, in the morning after the first irrigation.
The photos of slice 3L and 3R were taken on Sept. 13, in the evening right after the second irrigation.
The photos of slice 4L and 4R were taken on Sept. 14, the morning after the second irrigation.

## Processed Data

We processed the photos through code provided by the University of Zurich, which rectifies and crops the images and classifies each pixel with values of 1 (presence of dye) or 0 (absence of dye). The code only detects dye presence/absence and does not separate different color intensities. The pixel size corresponds to 1 mm. Rows indicate depth and columns indicate the lateral extent of the slice (rightward distance from the left side of the slice). The processed files are named as "sliceXX_data.txt", where XX goes from 1L to 4R (see slice scheme in figure TransectsScheme.png). 

For each slice, we also provide a summary table with the distribution of tracer presence at each depth. This was obtained by counting at each depth the number of pixels that contained tracer. 
