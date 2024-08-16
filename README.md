# BOT
## Estimation of bottom water characteristics 

Goal: we propose a simple "finder" python code to calculate the closest distance in latitude/longitude and water depth of hydrological parameters (e.g. Temperature, δ<sup>13</sup>C-DIC, δ<sup>18</sup>Osw, nitrate, nitrite data) from sediment samples as a method to estimate bottom water characteristics. 

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

![hidroeepsep_odv_example_githubBOT](https://github.com/user-attachments/assets/a18f29e1-7dfc-4ee7-97ab-e4dacc875136)
Figure 2. Map of hidrological stations from the "hidrodataset-eqsouthpacific_version2023" data set and temperature, oxygen and photosphate sections. Visualizations were made using gridded data processed by Interpolated Variational Analysis (DIVA) (oxygen and phosphate) and Weighted Average Interpolation gridding (temperature) (Gridding of X:40, Y:30) on Ocean Data View 5.6.5 (Schlitzer, R., 2023).
   
5) In your just make section (X, Y, Z), go to the menu interphase and select EXTRAS > CLIPBOARD COPY > Export gridded field values and "poor man's errors" (Column separation character: TAB; Export variable labels and Export data with missing Z value). This optinion will allow you to export the interpolated data into a text file or Excel.
6) Eliminate all spaces of the data and the "poor man's errors" column.
7) Save the file as a txt (Column separation character: Tabulation).

> _SectionLatitude	Depth[m]	Temperatureinsitu
> -43.8925	3300	1.80061
> -43.7863	3300	1.80051
> -43.6811	3300	1.80042
> -43.5771	3300	1.80031
   
## Getting started (Generation of sediment sites imput file)

1) Create a text file (Column separation character: Tabulation) with your sediment sites information (Column 1: station; Column 2: latitude/longitude; Column 3: waterdepth). 

> station	latitude	waterdepth
> BIAC072014L3	-27.11	90
> Crio1104.E1	-12.04	48
> Crio1104.E2	-14.08	180

## Run the BOTcode (Generation of output file)

1) Install Python (recommendable last edition) https://www.python.org/
2) Check BOTcode (attached) 
3) Create in your PC a single folder where you add all imput files: sediment stations, hydrological parameter 1 (e.g., oxygen), hydrologial parameter 2 (e.g., temperatature), Hydrological parameter 3,4,5,6,n; BOTcode python.
4) Run the code

>> For Mac users
1) Open terminal in folfer and add
$ awk '{ printf "%s ", $1; system("python3.6 BOT.py " $2 " " $3 " hidroparametername.txt")}' sedimentstationsname.txt > sedimentstationsname.data.hydroparametersname.txt
example: $ awk '{ printf "%s ", $1; system("python3.6 Cod_022d.py " $2 " " $3 " ioncarbonate.txt")}' estaciones2.txt > stations2.data.ioncarbonate.txt

5) Results (imput station, imput hidro data set, imput latitude, imput water depth; closet find latitude output, closet find water depth output, bottom water hidrological estimation output)

> station 
> BIAC072014L3 temp.txt -27.11 90.0 -27.1432 89.78008 13.13343
> Crio1104.E1 temp.txt -12.04 48.0 -12.0455 47.36325 15.03729
> Crio1104.E2 temp.txt -14.08 180.0 -14.0525 180.20802 13.38986


## BOT Authors 

* **Dharma A. Reyes Macaya** - [*Paleobiogeochemistry working group*](https://pastclimates.site.hw.ac.uk/)*, Lyell Centre, Heriot-Watt University, Scotland, UK* - [*MARUM*](https://www.marum.de/en/index.html)*, University of Bremen, Germany* 
* **Pablo Santamarina** - [*Innovex Tecnologías (Ltd.)*](www.innovex.cl)*, Chile*
* **Rodrigo Troncoso** - *Arturo Prat University, Iquique, Chile*


### BOT Collaborators

* **Laura Farias** * - [*Centro de Ciencia del Clima y Resiliencia*](https://www.cr2.cl/)*, Chile*, * - [*Instituto Milenio en Socio-Ecología Costera (SECOS) - Millennium Science Initiative Program*](https://socioecologiacostera.cl/en/), Chile*, * - [*Departamento de Oceanografía, Universidad de Concepción*](http://oceanografia.udec.cl/)*, Chile*
* **Sebastian Garrido** - [*Paleobiogeochemistry working group*](https://pastclimates.site.hw.ac.uk/)*, Lyell Centre, Heriot-Watt University, Scotland, UK*
* **Sofia Barragan-Montilla** - [*MARUM*](https://www.marum.de/en/index.html)*, University of Bremen, Germany*
