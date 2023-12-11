# README Isotope Sample Data

## General info

This readme file describes the isotope dataset.

Samples were collected using a soil auger. Each sample represents an average over 10 cm depth. We sampled down to 60 cm and occasionally, where possible, down to 70 cm depth. The extracted soil was placed in coffee bags and kept in a fridge before shipment to the lab for analysis. 

The first two profiles (A and B) were collected outside the irrigation area and are representative of pre-irrigation conditions. Since the soil was extremely dry, we dug two holes to collect more soil (and so more water). Thus, for profiles A and B, every sample merges soil collected at the same depth from the 2 holes.

All other profiles were collected within the irrigation area. Profile D was hard to dig and so only the most shallow samples were collected in it (Dtop in the figure). A second hole (Dbot) was dug to collect deeper soil samples.

The profiles C-D were collected right after the second (and trace-free) irrigation. They were collected at the same location where the blue dye slice 2 was excavated, to allow comparisons between the isotope and blue dye distributions. There is an additional sample collected between 10-20 cm at a very blue patch along slice 2 (named 'D020b'). It was collected with the expectation that its dD value should be higher (and the data confirm that this is the case).

Profiles E-F were collected 2 days after tracer application, profiled G-H after 11 days and profiles I-J after 19 days. No rainfall occurred between the soil samples collection.

The dataset also includes a sample of the highly-enriched irrigation water as well as a sample of the tap water that was used for both irrigations.

All soil water analyses and input water analyses were carried out by Matthias Beyer and Alberto Iraheta at the University of Braunschweig, Germany, using the Direct Vapor Equilibration method. The input water sample was also analysed at the University of Braunschweig by measuring the isotope composition of the vapor in equilibrium with the sample. The tap water sample was analysed at the University of Lausanne (liquid water) by the group of Torsten Venneman.

## Dataset structure

The dataset includes a single .csv data table with variables:

- shortID: short sample identifier (e.g. A010, which refers to profile A and maximum depth 10 cm)
- date: date in format 'dd/mm/yyyy' (e.g. 13/09/2023)	
- mean sampling time: approximate time of the day (UTC+01) when the sample was collected
- core: soil core identifier (values A-J)	
- depth_min: minimum sample depth in cm	
- depth_max: maximum sample depth in cm	
- d2H: 2H delta values with respect to the standard VSMOW
- d18O: 18O delta values with respect to the standard VSMOW
- notes: manual notes about the samples


## Known data issues

The sample E020 (collected from core E depth 10-20 cm) had a very high value that is interpreted as non reliable

Due to shipment issues, samples from profiles I-J remained in the bag outside a fridge for over 4 weeks before analysis. However, their isotope values do not seem to be affected by this extra time before analysis

