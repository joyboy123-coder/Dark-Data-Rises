# 📊 ETL to Snowflake to SQL to Visualization

This project demonstrates a full data pipeline — from raw data to valuable insights and beautiful charts.

---

## 🧠 Project Overview

This project includes:

- ✅ ETL (Extract, Transform, Load) process using Python  
- ❄️ Loading the cleaned data into **Snowflake**  
- 🧮 Using **SQL** to extract insights from the data  
- 📊 Visualizing insights with **matplotlib** and **seaborn**

---

## 📁 Data Folder

- `raw_data.csv` → Contains the original **100,000 rows** of unprocessed data  
- `cleaned_data.csv` → The result of cleaning `raw_data.csv` through ETL process

---

## 🧰 ETL Process (in `etl_python` folder)

The ETL is broken into three main steps:

1. **Extract** data from `raw_data.csv`  
2. **Transform** it (cleaning, formatting, etc.)  
3. **Load** the final cleaned data into **Snowflake**

To perform the ETL:

> 🚀 Run `etl_pipeline.py` (which is **outside** the `etl_python` folder)  
> This script will trigger the full ETL pipeline and load the data to Snowflake.

---

## 🖼️ Images Folder

This folder contains screenshots of the project stages:

- Before & after data cleaning  
- Before & after loading to Snowflake  
- Logs from ETL in `log_file.log`  
  *(📝 Currently empty because ETL hasn't been run yet)*

---

## 📁 SQL Folder

Contains SQL questions and solutions to analyze the data after it’s loaded into Snowflake.

- Each SQL file focuses on a specific topic (e.g., filtering, aggregation, window functions, etc.)  
- Run them after ETL to explore insights from your cleaned data ✅

---

## 📊 Visualization Folder

Includes `analyze.py` that visualizes data using:

- 📉 Bar chart (with `matplotlib`)  
- 🥧 Pie chart (with `seaborn`)  

**To use:**

1. Run `analyze.py`  
2. When prompted, provide the path to `cleaned_data.csv` (from the `data` folder)  
3. First a **bar graph** will appear  
4. Close the graph window, and the **pie chart** will pop up next 🎉

---

## ▶️ How to Use This Project

1. 📥 First, install the required Python libraries (see Requirements section below)  
2. ⚙️ Run `etl_pipeline.py` → This will extract, clean, and load data into **Snowflake**  
3. 🔍 Open the **SQL folder** and try the SQL questions to analyze the loaded data  
4. 📊 Run `analyze.py` in the **visualization folder**  
   - Paste the path to `cleaned_data.csv` when asked  
   - Enjoy bar and pie charts generated from the clean data!  

---

## 📦 Requirements

Install the required dependencies with:

```bash
pip install -r requirements.txt
