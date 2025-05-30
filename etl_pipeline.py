from etl_python.extract import extract_csv_data
from etl_python.transform import transform_data
from etl_python.load import load
import logging

def main():
    raw_data = input('Enter Raw data file Path : ').strip('"')
    data = extract_csv_data(raw_data)
    df = transform_data(data)
    load(df)
    logging.info('ETL Pipeline Finished Successfully :>')


if __name__ == "__main__":
    main()