# BOT
## Estimation of bottom water characteristics 

Goal: we propose a simple "finder" python code to calculate the closest distance in latitude/longitude and water depth of hidrological parameters (e.g. Temperature, δ<sup>13</sup>C-DIC, δ<sup>18</sup>Osw, nitrate, nitrite data) from sediment samples as a method to estimate bottom water characteristics. 

![GC_MUC_sediment_model](https://user-images.githubusercontent.com/57748370/113622334-231a8e80-965d-11eb-977d-943e565c5e71.png) 
Figure 1. Schematic representation of sediment core locations relative to overlying water mass distributions based on δ<sup>13</sup>C-DIC (Reyes-Macaya et al., 2022). Visualizations were generated using gridded data processed by Interpolated Variational Analysis (DIVA) (X:30, Y:20 grid) in Ocean Data View 5.6.5 (Schlitzer, R., 2023).

Motivation: Oceanographers and paleoceanographers typically define bottom water as the water column within approximately 10 meters of the seabed/seafloor. A significant challenge in paleoceanography is the scarcity of in-situ measurements of bottom water properties at locations where surface or long sediment cores are obtained. This hinders the development of methods that we can use to determinate bottom waters characterists estimated from regional/global hidrological data bases, then we can use that data to be used for proxy calibrations and define modern oceanographic settings. 

Here, we will provide detailed and simple method to estimated bottom waters at the Equatorial and Southeast Pacific. As an example we will use the curated data set "hidrodataset-eqsouthpacific_version2023" (a dataset emphasizing to host high-quality oxygen, nutrient, δ<sup>13</sup>C-DIC, δ<sup>18</sup>O-sea water, δD-sea water data in the Equatorial and Southeast Pacific), can be utilized. These datasets can be visualized and interpolated using software like Ocean Data View (https://odv.awi.de/software/download/).
 
### Prerequisites

- Ocen Data View software (https://odv.awi.de/software/download/)   
- Text file manager (eg. note ++, Excel).
- Python software https://www.python.org/downloads/ 

### Getting started (Generation of Hydrological imput file): preparation of the data in Ocen Data View software (https://odv.awi.de/software/download/)

1) Call your data to ODV (e.g., hidrodataset-eqsouthpacific_version2023). If you curated the data, we recomend you to use a ODV template (attached doc, https://drive.google.com/file/d/1ZyONN1T7nXM2F6SS73UdqvW5-ooHM6aB/view?usp=drive_open) and save the data set in text file (prefence CVS)
2) Make a section in the study area that you are working on, we recomend to do a section close to you sediment stions. Plot your data in sections (x: Latitude or Longitude; Y: Depth; Z: Hidrological variable). Safe important information: 1) your map section (picture) and section properties as "Mean Width" of the section; 2) Hidrological Section properties (Gridded field, Automatic Scale lenghts, Quality limit). 
3) You can apply Data Interpolated Variational Analysis (referred to as DIVA-interpolation), Weighted Average Interpolation gridding to interpolated your data (maximum gridding recomendable 40:X and 30:Y scale-length (permille) by [*Ocen Data View software*] (https://odv.awi.de/software/download/). If you use DIVA inteprolation, report the "signal-to-Noise Ratio" and of you configurate or not the "Prevent negative gridded values". 
4) In your just make section (X, Y, Z), go to the menu interphase and select EXTRAS > CLIPBOARD COPY > Export gridded field values and "poor man's errors" (Column separation character: TAB; Export variable labels and Export data with missing Z value). This optinion will allow you to export the interpolated data into a text file or Excel.
5) Eliminate all spaces of the data and the "poor man's errors" column.
6) Save the file as a txt (Column separation character: Tabulation).

![](![hidroeepsep_odv_example_githubBOT](https://github.com/user-attachments/assets/a18f29e1-7dfc-4ee7-97ab-e4dacc875136)
)





## Getting started (Generation of sediment sites imput file): 


Download the latest version of ODV in https://odv.awi.de/software/download/ 

- Organize your data using the Ocean Data View (ODV) data template (excel file example). Excel file example (Please not delete the first row items, you can add new columns after the parameter “depth [m]”) https://drive.google.com/file/d/1ZyONN1T7nXM2F6SS73UdqvW5-ooHM6aB/view?usp=drive_open 
- The excel file with your data needs to be exported as a text file (preference format cvs)
- Import from ODV the txt file 
- Organize the data by meridional o zonal hydrological section 
- Use the tool **clipboard copy (right bottom, option Extra) type export grilled filled values with tabulations** were used. The full grilled data was a copy in an excel file, edited the first line taking care to avoid text space and saved in txt separated with tabulations or in comma-separated csv. For futher information use https://odv.awi.de/fileadmin/user_upload/odv/misc/odv4Guide.pdf 

### Second Step (data-sediments)...

#### Determination of relative bottom water characteristics at the surface sediment sites

With the goal of finding the relative bottom water hydrological characteristics from the grilled hydrological interpolations (explained in point 1) in top of surface sediments collected in the South-East Pacific, a python script was developed. 

**Step 1.** Install Python (recommendable last edition) https://www.python.org/ 

**Step 2.** Create in your PC a single folder for each hydrological parameter (eg. one specific folder for oxygen, temperature, salinity). In that folder, add 

i) the hydrological parameter grilled text file obtained previously in Ocean Data View (example file format, https://drive.google.com/open?id=1DU3xOgopRsxX4oWs65YJ8nyRAoMPxk-9) 

ii) the station’s text file (example file format https://drive.google.com/open?id=1usasObWq-_4XA57hb3dHwZay6TwVpQc2) and the 

iii) python script. Remember that the name of the files needs to be simple and without spaces.  


### Third Step (Script-Python)...



## Example ... (Paper undercostruction)






## DAFT Authors 

* **Dharma A. Reyes Macaya** - [*MARUM*](https://www.marum.de/en/index.html)*, University of Bremen, Germany* 

* **Pablo Santamarina** - [*Innovex Tecnologías (Ltd.)*](www.innovex.cl)*, Chile*

* **Rodrigo Troncoso** - *Arturo Prat University, Iquique, Chile*



### Collaborators

> **Dharma Reyes** - *MARUM Institute, University of Bremen, Germany* - [dreyesmacaya@marum.de]

> **Pablo Santamarina** - *Innovex (Ltd.), Chile*

> **Rodrigo Troncoso** - *Arturo Prat University, Iquique, Chile*



See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
