import sys
import pandas as pd
import numpy as np

df = pd.read_csv('15_03_2017_calendar.csv')

a = df.available.apply(lambda x: (x.replace('t', '1')))
a = a.apply(lambda x: (x.replace('f', '0')))
df = df.drop(['available'], axis=1)
df['available'] = a.values

p = df.price.astype(str).apply(lambda x: (x.replace('$', '')))
p = p.astype(str).apply(lambda x: (x.replace('nan', '0')))
df = df.drop(['price'], axis=1)
df['price'] = p.values

df.to_csv('cleanCalendar.csv', index='False',  header='true', encoding='utf-8')
