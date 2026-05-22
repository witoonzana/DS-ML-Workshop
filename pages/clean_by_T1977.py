import pandas as pd
import numpy as np
from scipy.stats.mstats import winsorize
import matplotlib.pyplot as plt
import seaborn as sns

def perform_data_cleaning(df_raw):
    df = df_raw.copy()

    print('--- Data Cleaning Process Started ---')

    # 1. Duplicate Data
    initial_rows = len(df)
    exact_dups = df.duplicated()
    exact_dup_count = exact_dups.sum()
    if exact_dup_count > 0:
        df = df.drop_duplicates()
        print(f'✅ ลบ Exact Duplicate: ลดลง {initial_rows - len(df):,} แถว (เหลือ {len(df):,} แถว)')
    else:
        print('✅ ไม่พบ Exact Duplicate')

    # 2. Inconsistent Data
    # Region Column
    df['Region'] = df['Region'].str.strip().str.lower()
    region_mapping = {
        'th-central': 'TH-Central', 'th central': 'TH-Central',
        'thailand central': 'TH-Central', 'thailand-central': 'TH-Central',
        'thailand': 'TH-Central',
        'usa-east': 'USA-East', 'us east': 'USA-East',
        'united states east': 'USA-East', 'u.s.a.': 'USA-East',
        'europe-eu': 'Europe-EU', 'eu': 'Europe-EU',
        'europe': 'Europe-EU', 'european union': 'Europe-EU',
        'asia-pacific': 'Asia-Pacific', 'asia-pac': 'Asia-Pacific',
        'apac': 'Asia-Pacific', 'asia pacific': 'Asia-Pacific'
    }
    df['Region'] = df['Region'].replace(region_mapping)
    df['Region'] = df['Region'].str.upper()

    # Product_Variant Column
    df['Product_Variant'] = df['Product_Variant'].str.strip().str.lower()
    product_variant_mapping = {
        'original blue': 'Original Blue', 'original  blue': 'Original Blue',
        'krating daeng 250': 'Krating Daeng 250',
        'red edition': 'Red Edition',
        'sugarfree': 'Sugarfree', 'sugar free': 'Sugarfree',
        'sugarfree ': 'Sugarfree', 'sugar-free': 'Sugarfree',
        'tropical edition': 'Tropical Edition', 'tropical  edition': 'Tropical Edition',
        'tropical': 'Tropical Edition',
    }
    df['Product_Variant'] = df['Product_Variant'].replace(product_variant_mapping)

    # Channel Column
    df['Channel'] = df['Channel'].str.strip().str.lower()
    channel_mapping = {
        'social media': 'Social Media', 'social_media': 'Social Media',
        'tv ad': 'TV Ad', 'tv ads': 'TV Ad',
        'tv advertisement': 'TV Ad', 'television ad': 'TV Ad',
        'in-store promo': 'In-store Promo',
        'f1 sponsorship': 'F1 Sponsorship',
        'extreme sports': 'Extreme Sports'
    }
    df['Channel'] = df['Channel'].replace(channel_mapping)
    df['Channel'] = df['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x)

    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    print('✅ จัดการ Inconsistent Data สำเร็จ')

    # 3. Missing Data
    initial_missing_count = df.isnull().sum().sum()
    if initial_missing_count > 0:
        median_marketing = df['Marketing_Spend'].median()
        df['Marketing_Spend'] = df['Marketing_Spend'].fillna(median_marketing)
        median_score = df['Customer_Score'].median()
        df['Customer_Score'] = df['Customer_Score'].fillna(median_score)
        print(f'✅ จัดการ Missing Data: เติม Marketing_Spend ด้วย Median {median_marketing:,.2f} และ Customer_Score ด้วย Median {median_score}')
    else:
        print('✅ ไม่พบ Missing Data')

    # 4. Noisy Data
    noisy_before_rows = len(df)
    df = df[df['Unit_Price'] > 0]
    df = df[df['Units_Sold'] > 0]
    df = df[df['Marketing_Spend'] >= 0]
    df = df[(df['Customer_Score'] >= 1) & (df['Customer_Score'] <= 10)]
    if len(df) < noisy_before_rows:
        print(f'✅ จัดการ Noisy Data: ลบไป {noisy_before_rows - len(df):,} แถว (เหลือ {len(df):,} แถว)')
    else:
        print('✅ ไม่พบ Noisy Data ที่ต้องแก้ไข')

    # 5. Outlier Detection (No Treatment Applied as per notebook's decision)
    print('✅ ตรวจสอบ Outlier (ไม่ทำการปรับแก้ตาม Business Logic)')

    print('--- Data Cleaning Process Finished ---')
    return df

# Example Usage:
# Assuming df_raw is your original DataFrame from loading data
# df_cleaned = perform_data_cleaning(df_raw)
# print('\nCleaned Data Info:')
# df_cleaned.info()
# print('\nCleaned Data Head:')
# print(df_cleaned.head())
