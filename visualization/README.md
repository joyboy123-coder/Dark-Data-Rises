# 📊 Visualization Folder Overview

The `visualization` folder contains everything related to **data visualization** using `plotly`. This is the **final step** in the workflow — performed **after ETL** and **after SQL checks** are completed. ✅📦📈

---

## 📄 analyze.py

- 🧠 A Python script that generates an interactive dashboard with:
  - 📊 A **Bar Graph** showing total quantity ordered by product
    - Interactive dropdown filter to select specific products
    - Hover tooltips for detailed information
  - 🥧 A **Pie Chart** showing order status distribution
    - Interactive hover effects
    - Percentage display

- 🛠️ Uses:
  - `plotly.express`
  - `plotly.graph_objects`
  - `pandas`

- 🎨 Features:
  - Dark theme with custom colors
  - Interactive filters
  - Responsive layout
  - Export to HTML for easy sharing
  - Backup static PNG files included

- 🧪 Run this script after you've:
  - ✅ Completed the ETL process
  - ❄️ Loaded data into Snowflake
  - 📂 Performed SQL queries and analysis

- ▶️ Run this in CMD :
  ```bash
  python analyze.py
  ```

- 📂 Output Files:
  - `interactive_dashboard.html` - Interactive visualization
  - `bar_graph.png` - Static backup of bar chart
  - `pie_chart.png` - Static backup of pie chart
