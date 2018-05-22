import sys
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('15_03_2017_calendar.csv')
    # ['listing_id' 'date' 'available' 'price']
    print "calendar listing head", df.columns.values
    # print df.head()
    # print df["date"].max(), df["date"].min()
    print

    # print "\n\n\n"

    # df = pd.read_csv('listings.csv')
    # print "general listing head", df.columns.values
    # print df.calendar_updated.head()
    # print df.neighbourhood_cleansed.head()

    # use lambda or the code bellow for this -> print df.loc[df.street.contains('Montferrutx')]
    # df = pd.DataFrame({"body": ["ball", "red BALL", "round sphere"]})
    # urba = df[df["street"].str.contains("Montferrutx")]
    # print urba
    # print df.loc[df.experiences_offered != 'none'].values

    # mafioso = df.loc[df.calculated_host_listings_count == 752]
    # print mafioso.host_url
    # print df["calculated_host_listings_count"].max()

main()
