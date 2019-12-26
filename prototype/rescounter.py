import pandas as pd
import numpy as np
import argparse
from datetime import date, datetime, timedelta

# setting up argument parser
parser = argparse.ArgumentParser(description='Computes number of days outside UK for residency purposes.')
parser.add_argument('infile', type=str, help='location of the CSV file with the list of trips')

args = parser.parse_args()

# reading passed csv file
df = pd.read_csv(args.infile, header=0, parse_dates=[0,1], dayfirst=True)

# performing computations
df['duration'] = df['arrival']-df['departure']
df['adjusted'] = df['duration'] - timedelta(days=1)
cum_sum_series = pd.Series(index=df.index)
out_of_series = pd.Series(index=df.index)

for index, row in df.iterrows():
    start_date = row['arrival'] - pd.DateOffset(months=12)
    last_year_df = df[(df['departure'] < row['arrival']) & (df['arrival'] >= start_date)]

    # add handling for leaves which start at the beginning of a year
    sorted_last_year_df = last_year_df.sort_values(by='departure', axis=0, ascending=True)
    first_dep_date = sorted_last_year_df.iloc[0]['departure']
    deduct_extra_days = pd.DateOffset()
    if start_date > first_dep_date:
        deduct_extra_days = start_date - first_dep_date
    cum_sum_series.iloc[index] = last_year_df['adjusted'].sum() - deduct_extra_days

    # calculate how many days you could be out for in the last 12 months
    out_of_series.iloc[index] = np.floor((row['arrival'] - start_date).days/2)

# preparing output
df['time out of UK ytd'] = pd.to_timedelta(cum_sum_series, unit='D')
df['allowed time out'] = pd.to_timedelta(out_of_series, unit='D')
print(df[['departure', 'arrival', 'description', 'time out of UK ytd', 'allowed time out']])