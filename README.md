# Weather_dashboarding
# Big Data Weather Analysis Project

## Introduction

This project focuses on collecting, processing, and visualizing weather data from the National Centers for Environmental Information (NCEI) hosted by the National Oceanic and Atmospheric Administration (NOAA). We use Hadoop for distributed data processing, Python for data manipulation and analysis, MapReduce for distributed data processing, and Power BI for data visualization.

## Project Components

### Data Collection

We obtain weather data from the following source:
- NOAA NCEI Data Access: [https://www1.ncdc.noaa.gov/](https://www1.ncdc.noaa.gov/)

### Data Processing

#### Hadoop

We use Hadoop for distributed data processing. Make sure you have Hadoop properly installed and configured.

#### Data Processing Pipeline

1. Use Python scripts to download weather data from NOAA.
2. Use MapReduce to process and aggregate the data.
3. Store the processed data in Hadoop Distributed File System (HDFS).

### Data Analysis

We use Python for data analysis and manipulation. The analysis includes:

- Calculate average temperature, pressure, and wind speed.
- Find daily minimum and maximum temperature, pressure, and wind speed.
- Prepare the data for visualization.

## Apache Airflow Integration

We use Apache Airflow to orchestrate and schedule data workflows in this project. Apache Airflow allows us to automate the execution of various tasks, ensuring that data collection, processing, and analysis are performed efficiently and reliably. It helps manage dependencies between tasks and provides a clear and scalable way to schedule data-related operations.

### Airflow DAG (Directed Acyclic Graph)

Our Apache Airflow setup includes a Directed Acyclic Graph (DAG) that defines the sequence of tasks for this project. The DAG includes tasks for data download, data processing using MapReduce, data analysis, and other relevant steps. Airflow ensures that these tasks run in a coordinated and controlled manner.

`
- `dags/`                  # Store Apache Airflow DAG configuration files
  - `weather_analysis_dag.py`  # Defines the DAG for this project

### Data Visualization

We use Power BI to create interactive dashboards for visualizing the weather data. The dashboards include various charts, graphs, and maps to provide insights into the weather data.

![image](https://github.com/Frandiiile/Weather_dashboarding/assets/95171284/e322a63b-d663-42cd-b4c6-c6a60c52a667)


## Project Structure

The project structure is organized as follows:

- `data/`                   # Store raw weather data downloaded from NOAA
- `mapreduce/`              # MapReduce code for data processing
  - `mapper.py`             # MapReduce mapper script
  - `reducer_daily.py`      # MapReduce reducer script for daily data
- `scripts/`                # Python scripts for data processing and analysis
  - `download_data.py`      # Script to download weather data from NOAA
  - `extractData.py`        # Script to extract and preprocess data
  - `Working_on_data.ipynb` # Jupyter notebook for working with data
- `output/`                 # Store processed data and output files (CSV files)
- `README.md`               # This README file

## Usage

1. Clone this repository to your local environment.

2. Set up Hadoop for distributed data processing.

3. Run the data download script to fetch weather data on NOAA:

   ```shell
   python scripts/download_data.py
