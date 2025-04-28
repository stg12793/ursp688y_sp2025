# Exercise 04: Underutilized Residential Parcels Analysis (City of College Park, MD)

## Research Question
The primary question addressed in this analysis is:  
**"What is the extent of underutiliresidential land useland witthe City of hin College Park near Metro stat?nt?"**

This analysis explores underutilized parcels of land within College Park, Maryland, particularly those near Metro stations, and calculates underutilization ratios based on zoning and built density. The goal is to identify opportunities for zoning changes that could help promote sustainable urban growth.

## Approach

1. **Data Acquisition**: 
   - Property data containing information about land use, zoning, and parcel details.
   - Zoning data that outlines allowed densities for different zoning types.
   - Geospatial data for College Park and nearby Metro stations.

2. **Data Preparation**:
   - Filter data to include only parcels within College Park and within a specified radius of Metro stations.
   - Ensure all datasets use the same Coordinate Reference System (CRS) for accurate spatial analysis.

3. **Merge Data**:
   - Combine zoning data with property parcels to calculate potential allowable densities.

4. **Density Calculation**:
   - For each parcel, calculate the built density (actual development) and the allowed density based on its zoning type.
   - Compute the underutilization ratio, which is the difference between allowed density and built density relative to the allowed density.

5. **Analysis**:
   - Calculate the percentage of underutilized parcels and analyze which zoning types contribute most to underutilization.

6. **Visuaization**:
   - Generate maps of underutilized parcels to visually highlight areas where zoning adjustments could lead to higher-density development.

## Files and Directoexercise04_michael.ipynb*`underutilized_land_analysis.ipynb`**: The main Jupyter notebook containing all data processing, analysis, and visualization cois for**`data/`**: This directory contains th: requiClean_Zoning_Py, Metro_One_Mile_Buffer_Py, Municipal_Boundary_Py, and red data_Info_Py. folder befor_exercise04_michaele runninE3. **`Re.md`**: This file, which explains the analysis and provides instru Filesny
**Property Information Shapefile:**
- Property_Info_Py.shp
- Property_Info_Py.dbf
- Property_Info_Py.shx
- Property_Info_Py.prj
- Property_Info_Py.cpg

**Zoning Information Shapefile:**
- Clean_Zoning_Py.shp
- Clean_Zoning_Py.dbf
- Clean_Zoning_Py.shx
- Clean_Zoning_Py.prj
- Clean_Zoning_Py.cpg

**Metro One-Mile Buffer Shapefile:**
- Metro_One_Mile_Buffer_Py.shp
- Metro_One_Mile_Buffer_Py.dbf
- Metro_One_Mile_Buffer_Py.shx
- Metro_One_Mile_Buffer_Py.prj
- Metro_One_Mile_Buffer_Py.cpg

**Municipal Boundary Shapefile:**
- Municipal_Boundary_Py.shp
- Municipal_Boundary_Py.dbf
- Municipal_Boundary_Py.shx
- Municipal_Boundary_Py.prj
- Municipal_Boundary_Py.cpg

### File Organization

exercise04/
│
├── your_first_name/
│   ├── exercise04_michael.ipynb
│   ├── ReadMe.md
│   ├── data/
│   │   ├── Property_Info_Py.shp
│   │   ├── Property_Info_Py.dbf
│   │   ├── Property_Info_Py.shx
│   │   ├── Property_Info_Py.prj
│   │   ├── Property_Info_Py.cpg
│   │   ├── Clean_Zoning_Py.shp
│   │   ├── Clean_Zoning_Py.dbf
│   │   ├── Clean_Zoning_Py.shx
│   │   ├── Clean_Zoning_Py.prj
│   │   ├── Clean_Zoning_Py.cpg
│   │   ├── Metro_One_Mile_Buffer_Py.shp
│   │   ├── Metro_One_Mile_Buffer_Py.dbf
│   │   ├── Metro_One_Mile_Buffer_Py.shx
│   │   ├── Metro_One_Mile_Buffer_Py.prj
│   │   ├── Metro_One_Mile_Buffer_Py.cpg
│   │   ├── Municipal_Boundary_Py.shp
│   │   ├── Municipal_Boundary_Py.dbf
│   │   ├── Municipal_Boundary_Py.shx
│   │   ├── Municipal_Boundary_Py.prj
│   │   └── Municipal_Boundary_Py.cpg
r College Park and Metro station locations.

### Data A[https://drive.google.com/drive/folders/18SFvOqeQhXGY8KrIgw38ZvlkBIADTXlW?usp=drive_linkfor Datasets**: [Insert Google Drive Link Here]
   - Download the datasets from the above link and place them in the `data` directory in your local environment to ensure the analysis runs properly.

## How to Run the Code

1. **Install Required Libraries**:
   - The code relies on the following Python libraries: `pandas`, `geopandas`, `matplotlib`, and `shapely`.
   - You can install them using `pip`:
     ```bash
     pip install pandas geopandas matplotlib shapely
     ```

2. **Data Setup**:
   - Download the required datasets from the link above and place them in the `data` folder in the same directory as the notebook.exercise04_michael:
   - Open the Jupyter notebook `underutilized_land_analysis.ipynb` in your preferred environment (e.g., JupyterLab, Google Colab, etc.).
   - Run all cells to reproduce the analysis and generate the results.

4. **Results**:
   - The notebook will output:
     - The total number of underutilized parcels
     - The percentage of underutilized parcels
     - The 

## Sources
- Shapefiles: Downloaded from Prince George’s County GIS Open Data Portal [https://gisdata.pgplanning.org/opendata/]
- Allowable Density Values for Zoning Districts: Taken from the Prince George’s County Zoning Ordinance [https://online.encodeplus.com/regs/princegeorgescounty-md/doc-viewer.aspx#secid-634]avdes the notebook, the data (or links to the data), and this `ReadMe.md` file.

## Notes

- Ensure all data files are correctly placed in the `data` folder before running the analysis.
- If any datasets are too large for GitHub or should not be made public, they can be hosted on a cloud service like Google Drive. Please ensure all files are accessible to classmates and the instructor.

---

*This README was created for Exercise 04 of the URSP688Y course at the University of Maryland.*
