# 🐦 Bird Species Observation Analysis
## Forest and Grassland Ecosystem

## 📌 Project Overview
This project analyzes the distribution and diversity of bird species 
across two distinct ecosystems: Forests and Grasslands. 
The study examines observational data to understand how environmental 
factors influence bird populations and behavior.

## 🎯 Business Use Cases
- Wildlife Conservation
- Land Management
- Eco-Tourism Development
- Sustainable Agriculture
- Policy Support
- Biodiversity Monitoring

## 🛠️ Tech Stack
- Python
- Pandas
- Plotly
- Streamlit
- SQLite
- Jupyter Notebook

## 📊 Dataset
- Total Observations: 15,372
- Unique Bird Species: 126
- Ecosystems: Forest & Grassland
- Year: 2018
- Total Sites: 71

## 📈 Key Findings
- Northern Cardinal is the most observed species (1,125 times)
- Forest ecosystem has slightly more observations than Grassland
- Summer season has the highest bird activity (10,508 observations)
- Only 3 observers recorded all the data
- CHOH 7 site has the highest bird diversity (48 unique species)

## 📁 Project Structure
- `bird_analysis.ipynb` — Data Cleaning and EDA
- `app.py` — Streamlit Interactive Dashboard
- `Bird_Cleaned_Data.csv` — Cleaned Dataset
- `bird_observations.db` — SQL Database

## 🚀 How to Run
1. Install required libraries:
pip install pandas plotly streamlit openpyxl

2. Run the Streamlit dashboard:
streamlit run app.py
