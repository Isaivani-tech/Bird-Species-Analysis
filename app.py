import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Page Config
st.set_page_config(page_title="Bird Species Dashboard",
                   page_icon="🐦",
                   layout="wide")

# Load data from SQL
conn = sqlite3.connect(r"C:\Users\Admin\OneDrive\Desktop\Bird_species_project\bird_observations.db")
df = pd.read_sql_query("SELECT * FROM bird_observations", conn)

# Title
st.title("🐦 Bird Species Observation Analysis")
st.markdown("### Forest and Grassland Ecosystem Dashboard")
st.markdown("---")

# Sidebar Filters
st.sidebar.title("🔍 Filters")
ecosystem = st.sidebar.multiselect("Select Ecosystem",
                                    options=df['Ecosystem'].unique(),
                                    default=df['Ecosystem'].unique())

season = st.sidebar.multiselect("Select Season",
                                 options=df['Season'].unique(),
                                 default=df['Season'].unique())

# Apply Filters
filtered_df = df[(df['Ecosystem'].isin(ecosystem)) & 
                 (df['Season'].isin(season))]

# KPI Metrics
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Observations", len(filtered_df))
col2.metric("Unique Species", filtered_df['Common_Name'].nunique())
col3.metric("Total Sites", filtered_df['Site_Name'].nunique())
col4.metric("Total Observers", filtered_df['Observer'].nunique())

st.markdown("---")

# Chart 1: Top 10 Species
st.markdown("### 🐦 Top 10 Most Observed Bird Species")
top10 = filtered_df['Common_Name'].value_counts().head(10).reset_index()
top10.columns = ['Bird Species', 'Count']
fig1 = px.bar(top10, x='Count', y='Bird Species', orientation='h',
              color='Count', color_continuous_scale='teal')
fig1.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 & 3 side by side
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌳 Observations by Ecosystem")
    ecosystem_counts = filtered_df['Ecosystem'].value_counts().reset_index()
    ecosystem_counts.columns = ['Ecosystem', 'Count']
    fig2 = px.pie(ecosystem_counts, names='Ecosystem', values='Count',
                  color_discrete_sequence=['#2ecc71', '#f39c12'])
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.markdown("### 📅 Observations by Season")
    season_counts = filtered_df['Season'].value_counts().reset_index()
    season_counts.columns = ['Season', 'Count']
    fig3 = px.bar(season_counts, x='Season', y='Count',
                  color='Season',
                  color_discrete_sequence=['#3498db','#e74c3c','#2ecc71','#f39c12'])
    st.plotly_chart(fig3, use_container_width=True)

# Chart 4: Sex Distribution
st.markdown("### 🐦 Sex Distribution of Birds")
sex_counts = filtered_df['Sex'].value_counts().reset_index()
sex_counts.columns = ['Sex', 'Count']
fig4 = px.pie(sex_counts, names='Sex', values='Count',
              color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig4, use_container_width=True)

# Chart 5: Sky Condition
st.markdown("### ☁️ Observations by Sky Condition")
sky_counts = filtered_df['Sky'].value_counts().reset_index()
sky_counts.columns = ['Sky Condition', 'Count']
fig5 = px.bar(sky_counts, x='Sky Condition', y='Count',
              color='Sky Condition',
              color_discrete_sequence=px.colors.qualitative.Pastel)
fig5.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.markdown("**Dashboard by Bird Species Analysis Project** 🐦")