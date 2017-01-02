import pandas as pd
import numpy as np
import time


placeList=["Paris","New York City"]

num_place = len(placeList)
print num_place
for data_index in range(0,num_place):
    file = open(placeList[data_index]+'_route.csv', 'w')

    processed_data = pd.read_csv(placeList[data_index]+'.csv')

    t0 = time.clock()

    #create new dataframe
    combinedDF = pd.DataFrame( columns=['reviewer_id','listing_id','date','street'])
    #print listings_data.keys()
    row_count_reviews = len(processed_data)  #street  city  state  zipcode smart_location is_location_exact
    #print row_count_reviews
    #traverse reviews_data

    count = 0
    for row_index in range(0,row_count_reviews):
        temp_row = processed_data.iloc[row_index]
        cur_temp_reviewer_id = temp_row.get('reviewer_id')
        cur_temp_street = temp_row.get('street')


        if row_index >0:
            if cur_temp_reviewer_id == pre_temp_reviewer_id:
                cur_location = cur_temp_street.split(",")[0]
                cur_location = cur_location[1:]

                pre_location = pre_temp_street.split(",")[0]
                pre_location = pre_location[1:]

                if count == 0:
                    file.write("\n"+pre_location +"," +cur_location)
                else:
                    file.write("," + cur_location)
                count = count +1
            else:
                count = 0

        pre_temp_reviewer_id = cur_temp_reviewer_id
        pre_temp_street = cur_temp_street
        print str(data_index) +"/" +str(num_place) +": " + str(row_index) +"/" +str(row_count_reviews)
        #get listing_id(house_id) of instance in reviews_data
    file.closed



t1 = time.clock()

print t1-t0

