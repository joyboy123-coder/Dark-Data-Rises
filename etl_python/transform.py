import pandas as pd
import logging
from word2number import w2n
import random
import os
def transform_data(data):

    try:
        logging.info('\nData Transformation and Cleaning\n')
        df = pd.DataFrame(data)

        logging.info('Removing Duplicate Rows :>')
        df.drop_duplicates(inplace=True)

        logging.info('Cleaning OrderID Column :>')
        df['OrderID'] = df['OrderID'].astype(int)

        logging.info('Cleaning CustomerName Column :>')
        df['CustomerName'] = df['CustomerName'].str.title().str.strip()
        names = ['Jacob', 'Wills', 'Green', 'Sasuke', 'Shinchi', 'Tom', 'Jimmy', 'Stokes', 'Buttler']
        df['CustomerName'] = df['CustomerName'].apply(lambda x: random.choice(names) if pd.isna(x) else x)

        logging.info('Cleaning Product Column :>')
        df['Product'] = df['Product'].str.title().str.strip()
        df['Product'] = df['Product'].apply(lambda x: random.choice(df['Product'].dropna().tolist()) if pd.isna(x) else x)

        logging.info('Cleaning Quantity Column :>')
        df['Quantity'] = df['Quantity'].apply(lambda x: w2n.word_to_num(x) if isinstance(x, str) else x)
        df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

        logging.info('Cleaning Price Column :>')
        df['Price'] = df['Price'].fillna(df['Price'].mean())
        df['Price'] = df['Price'].round(2)

        logging.info('Cleaning OrderDate Column :>')
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
        daterange = pd.date_range(
            start='1785-07-03',
            periods=df['OrderDate'].isna().sum(),
            freq='1D'
        )
        df.loc[df['OrderDate'].isna(), 'OrderDate'] = daterange
        df['OrderDate'] = df['OrderDate'].dt.date

        logging.info('Cleaning ShippedRegion Column :>')
        region_choices = df['ShippedRegion'].dropna().unique().tolist()
        df['ShippedRegion'] = df['ShippedRegion'].apply(lambda x: random.choice(region_choices) if pd.isna(x) else x)
        df['ShippedRegion'] = df['ShippedRegion'].str.title().str.strip()

        logging.info('Cleaning OrderStatus Column :>')
        df['OrderStatus'] = df['OrderStatus'].str.title().str.strip()
        status = df['OrderStatus'].dropna().unique().tolist()
        df['OrderStatus'] = df['OrderStatus'].apply(lambda x: random.choice(status) if pd.isna(x) else x)

        logging.info('Converting all Column Names into Uppercase :>')
        df.columns = df.columns.str.upper().str.strip()
        
        return df
    
    except Exception as e:
        logging.error(f'Transformation and Cleaning Failed : {e}')

    finally:
       logging.info('Transformation and Data Cleaning Successful :)')
       logging.info('----------------------------------------------------------------')
       
