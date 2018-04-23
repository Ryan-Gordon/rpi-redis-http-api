import os
import requests
import flask
import redis
import datetime
import json

class RedisProvider(object):
    def __init__(self, items: list=[]):
        self._items = items
        self.formatted_results = []
        
        
    def getLeaderboard(self) -> str:
        self.formatted_results = []
        #Connect to redis
        pool = redis.ConnectionPool(host='192.168.1.8', port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        
        # Run zrevrange from docs zrevrange(name, start, end, withscores=False, score_cast_func=<type 'float'>)
        raw_results = r.zrevrange(str('score.quizscore:'+datetime.datetime.today().strftime('%Y-%m-%d')) , 0, 5, withscores=True) 
        print(raw_results)

        for score in raw_results:
            print(score)
            print("\n\n Score before:"+score[0].decode("utf-8"))
            print("\n\n User : "+score[0].decode("utf-8")+ " with Score : "+str(score[1]) )

            self.formatted_results.append([score[0].decode("utf-8"), score[1]])
       #Format results 

       #Return

        return json.dumps(self.formatted_results), 200

    def getTodaysCurrentChampion(self) -> str:

        #Connect to redis
        pool = redis.ConnectionPool(host='192.168.1.8', port=6379, db=0)
        r = redis.Redis(connection_pool=pool)
        
        # Run zrevrange from docs zrevrange(name, start, end, withscores=False, score_cast_func=<type 'float'>)
        results = r.zrevrange(str('score.quizscore:'+datetime.datetime.today().strftime('%Y-%m-%d')) , 0, 5, withscores=True) 
        
       
        #Format results - Take winning player (first tuple) 
        score = results[0]
        #Return

        return "Todays champion is : \n User : "+str(score[0].decode("utf-8"))+ " with Score : "+str(score[1]), 200