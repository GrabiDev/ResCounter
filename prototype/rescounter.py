import pandas as pd
import argparse
from datetime import date, datetime, timedelta

parser = argparse.ArgumentParser(description='Computes number of days outside UK for residency purposes.')
parser.add_argument('infile', type=str, help='location of the CSV file with the list of trips')

args = parser.parse_args()

df = pd.read_csv(args.infile, header=0, parse_dates=[0,1], dayfirst=True)

df['duration'] = df['arrival']-df['departure']
df['adjusted'] = df['duration'] - timedelta(days=1)
cum_sum_series = pd.Series(index=df.index)

for index, row in df.iterrows():
    last_year_df = df[(df['departure'] < row['arrival']) & (df['arrival'] >= row['arrival'] - pd.DateOffset(months=12))]
    
    cum_sum_series.iloc[index] = last_year_df['adjusted'].sum()

df['time out of UK ytd'] = cum_sum_series
print(df[['departure', 'arrival', 'time out of UK ytd']])