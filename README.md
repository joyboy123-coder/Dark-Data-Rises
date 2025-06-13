# 🌟 Dark Data Rises: ETL to Snowflake to Visualization

![Dark Data Rises Thumbnail](images/thumbnail/thumbnail_image.png)

A complete data pipeline project that transforms raw data into valuable insights through ETL, data warehousing, and interactive visualizations.

## 🎯 Project Overview

This project demonstrates a full data pipeline:
- 📥 Extract data from CSV
- 🔄 Transform and clean data
- 📤 Load into Snowflake
- 📊 Visualize with interactive dashboards

## 🛠️ Tech Stack

- **ETL**: Python
- **Data Warehouse**: Snowflake
- **Data Transformation**: dbt
- **Visualization**: Plotly
- **Testing**: dbt Tests
- **Logging**: Python Logging

## 📁 Project Structure

```
├── data/               # Data files
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── etl_python/         # ETL scripts
├── dbt_project/        # dbt models and tests
├── visualization/      # Interactive dashboards
├── sql/               # SQL queries
└── log_file.log       # Log file
```

## 🚀 Features

### 1. ETL Pipeline
- ✅ Data extraction from CSV
- ✅ Data cleaning and transformation
- ✅ Loading to Snowflake
- ✅ Error handling and logging

### 2. Data Quality
- ✅ 27 dbt tests
- ✅ Data validation
- ✅ Logging system
- ✅ Error tracking

### 3. Visualization
- ✅ Interactive Plotly dashboard
- ✅ Product filters
- ✅ Dark theme
- ✅ HTML export

## 🎨 Visualization Features

- 📊 Bar chart with product quantities
- 🥧 Pie chart for order status
- 🔍 Interactive filters
- 🎯 Hover tooltips
- 💾 Export to HTML

## 🧪 Testing

- 27 dbt tests in macros folder
- Data quality checks
- Transformation tests
- Clean table tests

## 📈 Data Flow

1. Raw Data → ETL Pipeline
2. ETL Pipeline → Snowflake
3. Snowflake → dbt Models
4. dbt Models → Visualization

## 🚀 Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run ETL pipeline:
```bash
python etl_pipeline.py
```

3. View visualizations:
```bash
cd visualization
python analyze.py
```

4. Run dbt workflow:
```bash
cd dbt_project
dbt run        # Run all models to ensure data is clean
dbt test       # Run all 27 tests to validate data
dbt docs generate  # Generate documentation
dbt docs serve    # View documentation in browser
```

The complete workflow ensures:
- ✅ Data is properly loaded (ETL)
- ✅ Data is clean and transformed (dbt run)
- ✅ All tests pass (dbt test)
- ✅ Documentation is up to date (dbt docs)

## 📊 Output

- Cleaned data in Snowflake
- Interactive HTML dashboard
- Static PNG charts
- Log file for tracking
- dbt test results
- dbt documentation

## 🔍 Monitoring

- Log file in root directory
- dbt test results (27 tests)
- ETL pipeline status
- dbt documentation at http://localhost:8080

## 🎯 Future Improvements

1. Data quality monitoring dashboard
2. Performance optimization
3. Real-time data processing
4. Enhanced documentation
5. Data security features

## 👥 Contributing

Feel free to fork and contribute to this project!

## 📝 License

This project is open source and available under the MIT License.

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

Contains SQL questions and solutions to analyze the data after it's loaded into Snowflake.

- Each SQL file focuses on a specific topic (e.g., filtering, aggregation, window functions, etc.)  
- Run them after ETL to explore insights from your cleaned data ✅

---

## 📊 Visualization Folder

Includes `analyze.py` that visualizes data using:

- 📉 Bar chart (with `matplotlib`)  
- 🥧 Pie chart (with `seaborn`)  

**To use:**

1. Run `analyze.py`  
2. You will see interactive dashboard of "bar graph" and "pie chart" 
3. for backup we have .png files seperately 🎉

---

## ▶️ How to Use This Project

1. 📥 First, install the required Python libraries (see Requirements section below)  
2. ⚙️ Run `etl_pipeline.py` → This will extract, clean, and load data into **Snowflake**  
3. 🔍 Open the **SQL folder** and try the SQL questions to analyze the loaded data  
4. 📊 Run `analyze.py` in the **visualization folder**  
   - It will take u to a window and show you a interactive dashboard  
   - Enjoy bar and pie charts generated from the clean data!  

---

## 📦 Requirements

Install the required dependencies with:

```bash
pip install -r requirements.txt