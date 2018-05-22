import sys
import pandas as pd
import numpy as np

def main ():
    df = pd.read_csv('15_03_2017_calendar.csv')
    df = df[df.available != 'f']
    df = df[df.date > '2016']
    df['date'] = pd.to_datetime(df['date'])
    df.to_csv('15_03_2017_dropped_calendar.csv', encoding='utf-8')

main()
