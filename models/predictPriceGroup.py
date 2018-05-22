import tensorflow as tf
import os

filename = "../data/features.csv"

# host_is_superhost, security_deposit, seaViews
iFeatures_ = tf.placeholder(tf.int8, shape=[3], name='nFeatures_')
# bathrooms, bedrooms, beds, guests_included, review_scores_rating, availability
fFeatures_ = tf.placeholder(tf.float32, shape=[6], name='sFeatures_')
# zipcode, property_type, groupedPrice
sFeatures_ = tf.placeholder(tf.string, shape=[3], name='bFeatures_')

total_ = tf.reduce_sum(fFeatures_, name='total_')
printerop_ = tf.Print(total_, [fFeatures_, total_], name='printer_')

with open(filename) as inf:
    next(inf)
    for line in inf:
        try:
            zipcode, property_type, bathrooms, bedrooms, beds, guests_included, review_scores_rating, host_is_superhost, security_deposit, seaViews, availability, groupedPrice = line.strip().split(",")
            print (zipcode, property_type, bathrooms, bedrooms, beds, guests_included, review_scores_rating, host_is_superhost, security_deposit, seaViews, availability, groupedPrice)
            host_is_superhost = int(float(host_is_superhost)) if '' else 0
            security_deposit = int(float(security_deposit)) if '' else 0
            seaViews = int(float(seaViews)) if '' else 0
            bathrooms = float(bathrooms) if '' else 1.0
            bedrooms = float(bedrooms) if '' else 1.0
            beds = float(beds) if '' else 1.0
            guests_included = float(guests_included) if '' else 1.0
            review_scores_rating = float(review_scores_rating) if '' else 2.5
            availability = float(availability) if '' else 50.0
            # if str(groupedPrice) == "lowCost":
            #     groupedPrice = 0
            # if str(groupedPrice) == "medium":
            #     groupedPrice = 1
            # if str(groupedPrice) == "premium":
            #     groupedPrice = 2
        except ValueError:
            print('ended with the extracting')

# TF stuff still not working...
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sum = sess.run(printerop_, feed_dict={fFeatures_: [bathrooms, bedrooms, beds, guests_included, review_scores_rating, availability], groupedPrice:groupedPrice})
    print(groupedPrice, sum)
