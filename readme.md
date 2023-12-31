# WATSON Soil Tracer Experiment Data

This repository includes tracer data from a soil multi-tracer experiment carried out on a single soil plot of 3 m<sup>2</sup>. The data include:

- Images of brilliant blue dye from 4 soil transects ([DyeImageData](DyeImageData) folder)
- Timeseries of electrical conductivity, temperature and volumetric water content measured through 9 soil water probes ([ECSensorData](ECSensorData) folder)
- Isotope composition of 10 soil cores ([IsotopeSampleData](IsotopeSampleData) folder)

These tracer data were collected during a fall training school about isotopic tracer and labelling experiments, as part of the COST Action WATSON. The training school took place near Florence, Italy, between 12-14 September 2023.


## Experiment Design and Chronology

The main idea behind the experiment was to apply labeled water on top of a soil plot and track it over space and time.

We considered a plot of 3 m<sup>2</sup> (square of 1.75 m x 1.75 m) at the Training School venue ([see on Google Map](https://maps.app.goo.gl/LWNWN5TZWTygcvvv9)). The plot was basically flat, with just a very mild south-facing slope.
 
We used 3 tracers to label the water:
- **Brilliant Blue dye**, to visually see the spatial distribution of the tracer along transects
- **NaCl**, to measure the resulting pulse in Electrical Conductivity (EC) through EC sensors that measure at high temporal resolution
- **Deuterium**, to see the tracer in soil profiles analysed for their water isotope composition

## Irrigation 1 

On Sep 12 2023, between 16:40 and 19:00 UTC+01 we applied the three tracers together in a single irrigation (80 liters / 27 mm of tap water) using manual sprayers.

The applied water was labeled with:
- 4 g/l of Brilliant Blue dye
- 5 g/l of NaCl (which should make an EC of about 7000 uS/cm)
- 62.5 ug/l of D2O water at 99.99% (which should make the d2H of the solution about +330 permil)

![](labelSummary_small.jpg)

## Irrigation 2

On Sep 13 2023 between 17:30 and 19:45 UTC+01 we applied another 28 mm of tap water <u> that only had NaCl (5 g/l) and not the other tracers</u>. The goal was to better see a breakthrough in the EC signal while pushing down the other tracers.

## Measurement strategy

### Brilliant Blue Dye data

We excavated 4 transects and collected 2 pictures (a and b) from each of them. 

![](DyeImageData/TransectsScheme.png)

The data and additional details are in the [DyeImageData](DyeImageData) folder.

### NaCl data

We measured the pulse in EC at 9 locations:
- 'Left' side, at depths 10 cm, 20 cm and 30 cm  
- 'Middle' side at depths 10 cm, 20 cm, 30 cm, 40 cm 
- 'Right' side at depths 10 cm and 20 cm

![](ECSensorData/SensorsScheme.png)

Each probe also measured volumetric water content and temperature. The data and additional details are in the [ECSensorData](ECSensorData) folder.

### Deuterium data

We colleced soil profiles in 5 different days from 2 profiles each day (total 10 profiles): 

- Profiles A-B were collected before the tracer was applied, to evaluate the background condition
- Profiles C-D were collected the day after the tracer application 
- profiles E-F were collected after another day (after the second, unlabeled irrigation)
- profiles G-H were collected after 11 days
- profiles I-J were collected after 19 days 

The Bulk soil samples were analysed using the Direct Vapor Equilibration method at the University of Braunschweig by the group ot Matthias Beyer. 

![](IsotopeSampleData/cores_scheme.png)

The data and additional details are in the [IsotopeSampleData](IsotopeSampleData) folder.
	
### Summary scheme

The image below shows the tracer application area from the top and identifies the different measurement locations.

![](MeasurementSummary.jpg)