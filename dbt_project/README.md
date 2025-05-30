# 📦 DBT Project

This folder contains all DBT models, macros, custom tests, and documentation used in the data pipeline.

---

## 📁 models/

### 1. `models/cleaning/`
- Removes **duplicate rows** from raw data  
- Performs basic cleaning (null handling, formatting)

### 2. `models/transformations/`
- Filters to only include rows with `order_status = 'delivered'`  
- Splits output by `shipped_region`: north, south, east, west, central

---

## 🛠️ macros/
- Includes custom **macros**  
- Contains **27 tests** such as:
  - not null  
  - accepted values  
  - unique constraints

All tests are implemented using Jinja macros.

---

## 🚀 Run Everything in One Go

To run all models, tests, and generate docs in one command sequence:

```bash
dbt run && dbt test && dbt docs generate && dbt docs serve


---

