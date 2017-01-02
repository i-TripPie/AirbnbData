import pandas as pd
import numpy as np
import time


placeList=["Paris"]

#"New York City" "Paris"
#"Amsterdam","Athens","Austin","Berlin","Boston","Chicago","Denver","Dublin","Edinburgh","Geneva","Hong Kong")  "London", ,(done)"Los Angeles",   (done)
#"Madrid","Manchester","Melbourne","Montreal","Nashville","New Orleans"(done)
#  "Oakland","Portland","San Diego","San Francisco","Seattle","Sydney","Toronto","Vancouver","Venice","Victoria","Vienna","Washington" (done)

num_place = len(placeList)
print num_place
for data_index in range(0,num_place):
    reviews_data = pd.read_csv(placeList[data_index]+'_reviews.csv')
    listings_data = pd.read_csv(placeList[data_index]+'_listings.csv')

    t0 = time.clock()

    #create new dataframe
    combinedDF = pd.DataFrame( columns=['reviewer_id','listing_id','date','street'])
    #print listings_data.keys()
    row_count_reviews = len(reviews_data)  #street  city  state  zipcode smart_location is_location_exact
    #print row_count_reviews

    #traverse reviews_data
    for row_index in range(0,row_count_reviews):
        print str(data_index) +"/" +str(num_place) +": " + str(row_index) +"/" +str(row_count_reviews)
        #get listing_id(house_id) of instance in reviews_data
        temp_row = reviews_data.iloc[row_index]

        temp_listing_id = temp_row.get('listing_id')
        temp_date = temp_row.get('date')
        temp_reviewer_id = temp_row.get('reviewer_id')

        #use listing_id to get  host_location of this listing_id in llistings_data
        temp_row_listing = listings_data.query('id ==' + str(temp_listing_id))
        temp_street =  temp_row_listing.get('street')

        new_record = pd.DataFrame([[str(temp_reviewer_id),str(temp_listing_id), str(temp_date), temp_street]], columns=['reviewer_id','listing_id','date','street'])
        combinedDF = pd.concat([combinedDF,new_record])


    t1 = time.clock()

    print t1-t0
    #combinedDF.sort_values('reviewer_id','date').to_csv('Washington.csv', encoding='utf-8', index=False)
    combinedDF.sort_values(['reviewer_id','date']).to_csv(placeList[data_index]+'.csv', encoding='utf-8', index=False)
