from etl_python.extract import extract_csv_data
from etl_python.transform import transform_data
from etl_python.load import load
import logging
import os  # ✅ You forgot to import os

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    raw_data = os.path.join(BASE_DIR, 'data', 'raw_data.csv')  
    data = extract_csv_data(raw_data)  # ✅ Use data_path instead of undefined raw_data
    df = transform_data(data)
    load(df)
    logging.info('ETL Pipeline Finished Successfully :>')

if __name__ == "__main__":
    main()
