# ⚙️ ETL Python Scripts Overview

---

## 📁 etl_python Folder

This folder contains three core Python scripts responsible for the ETL process, each with **functions**, **logging**, and **exception handling** 🧠💡:

---

### 📥 extract.py
- Reads the raw dataset containing **100,000 rows**. 📄
- Uses a well-structured function to handle data extraction. 🧪
- Includes logging for status updates and exception handling for errors. 🚨

---

### 🔧 transform.py
- Cleans and transforms the **100,000 rows** of data. 🧹✨
- Operations include fixing formats, removing duplicates, and standardizing values. 🛠️
- Entire logic wrapped in a function with proper logs and error checks. 📊

---

### 📤 load.py
- Loads the cleaned data into a **Snowflake** database. ❄️🗃️
- Secure and structured loading using functions. 🚀
- Includes detailed logging and exception management. 🧾

---

## 🧩 etl_pipeline.py (Outside the Folder)

- This is the **main runner script**. 🎯  
- When you run `etl_pipeline.py`, it will:
  1. ✅ Call the extract function from `extract.py`
  2. ✅ Pass the data to the transform function in `transform.py`
  3. ✅ Finally, call the load function from `load.py` to push it to Snowflake  
- This script **orchestrates the full ETL pipeline** in a clean and modular way. 🔄💼

---
