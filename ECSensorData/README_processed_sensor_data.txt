# README processed sensor data

## General info

This readme file describes the processed sensor data.

Sensors were installed on 12-Sep-2023 around 17:00 UTC+01 in a small soil trench of about 100-cm length and 40-cm depth (see sensor_position_scheme.png). Sensors consisted in 8 Meter/Decagon 5TE sensors and 1 Meter GS3 sensor. These sensors measure volumetric water content, temperature and electrical conductivity. The dataloggers are 2 Meter/Decagon Em50 and they were set up to record data every 2 minutes.

The soil was extremely dry when sensors were installed and made the installation rather challenging.


## Processed Data

Processed data were obtained by combining and cleaning the raw data from the datalogger. Structure and naming convention: 

- Timestamps are formatted as 12-Sep-2023 16:36:00 and refer to time zone UTC+01
- Column names follow the convention <variable>_X_Y, where: 

	- <variable> can be volumetric water content (VWC), Temperature (Temp) or electrical conductivity (EC). 
	- X is the lateral position (sensors were installed along a line of roughly 1 meter, where X=L indicates the upslope end of the trench, X=M the middle point and X=R the downslope end of the trench). 
	- Y is the vertical position (depth): Y=10 is 10-cm depth, Y=20 is 20-cm depth, Y=30 is 30-cm depth and Y=40 is 40-cm depth.
- Units: VWC is [volume H2O / total volume], Temp is [degree Celsius], EC is in [uS/cm].
	
## Known data issues

### Sensor failures

It looks like no EC was recorded at sensors R_10, M_20, M_30: the loggers read constantly 0 or a very low value, but this is strange and it is likely related to a sensor issue. Perhaps the sensor was never wet enough to start a correct reading.

### Animals excavating between 12-13 September

The shallow sensor measurements were disturbed in the night between 12 and 13 September due to animals excavating around them. Sensors were put back in place in the morning of Sep 13.

### Effects of connecting a computer to the dataloggers

We can see in the data, especially from the shallow sensors, that when a computer was connected to the datalogger to download the data, some sensors had a small jump in the data. These jumps are possibly related to the disturbance of electrical currents, or simply just related to soil compaction when walking next to the sensors, rather than to hydrological processes.

