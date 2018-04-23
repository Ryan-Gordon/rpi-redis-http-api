from flask_injector import inject
from services.RedisProvider import RedisProvider
import flask

from flask import request, Response

@inject(data_provider=RedisProvider)
def getLeaderboard(data_provider) -> str:
    return data_provider.getLeaderboard()

@inject(data_provider=RedisProvider)
def getTodaysCurrentChampion(data_provider) -> str:
    return data_provider.getTodaysCurrentChampion()
