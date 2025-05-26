# 📊 Visualization Folder Overview

The `visualization` folder contains everything related to **data visualization** using `matplotlib` and `seaborn`. This is the **final step** in the workflow — performed **after ETL** and **after SQL checks** are completed. ✅📦📈

---

## 📄 analyze.py

- 🧠 A Python script that generates:
  - 📊 A **Bar Graph** showing total quantity ordered by product
  - 🥧 A **Pie Chart** showing order status distribution

- 🛠️ Uses:
  - `matplotlib.pyplot`
  - `seaborn`
  - `pandas`

- 🧪 Run this script after you've:
  - ✅ Completed the ETL process
  - ❄️ Loaded data into Snowflake
  - 📂 Performed SQL queries and analysis

- ▶️ Run this in CMD :
  ```bash
  python analyze.py
