from pymongo import MongoClient
import json


def load_data(MONGO_HOST, data_list):
    client = MongoClient(MONGO_HOST)
            
    #insert the data into the mongoDB into a collection called tweets
    #if tweets doesn't exist, it will be created.
    client.twitter.collections.tweets.insert(data_list)
 
if __name__ == "__main__":
	load_data(MONGO_HOST, data_list)
