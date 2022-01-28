from http import client
import pymongo
if __name__=="__main__":
    print("Welcome to pyMongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client.FavMovies
    collection=db.Movies
    print(collection)
    one=collection.find_one({'name':'IronMan'})
    print(one)
    allDocs=collection.find({'name':'IronMan'}, {'name':1 ,'_id': 0})
    for i in allDocs:
        print(i)
    
    


