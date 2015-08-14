# -*- coding: utf-8-*-
import random
import re

import json
import urllib2
import os.path, sys

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import time
import scipy.io.wavfile as wav

CLIENT_ACCESS_TOKEN = 'b038463ba99448f697fb3ea1c2fec088'
SUBSCRIPTION_KEY = '22aef7f4-029f-414b-9bb5-0d4a5e7d6a5d'

WORDS = []

PRIORITY = 50

CURRENT_ACTION_OBJ = None

class ApiaiActionObject:

    def __init__(self, query, action, paramsObject):
        self.query = query
        self.action = action
        self.paramsObject = paramsObject

def handle(text, mic, profile):
    """
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    
    #use the global action object to change the lights via a HTTP API call
    global CURRENT_ACTION_OBJ

    mic.say(profile['first_name']+", you got it")
    
    response = None
    responseDecode = None
    if CURRENT_ACTION_OBJ:
    	response = urllib2.urlopen("http://lights.imagineitproductions.com:8888/"+CURRENT_ACTION_OBJ.action+".php?switch="+CURRENT_ACTION_OBJ.paramsObject['switch']+"&roomlights="+CURRENT_ACTION_OBJ.paramsObject['roomlights']).read()
    	responseDecode = json.loads(response)
    
    if responseDecode:
        messages = ["You can thank Thomas Edison.", "All finished."]
    else:
    	messages = ["Sorry, "+profile['first_name']+", I couldn't fiddle with the lights."]

    message = random.choice(messages)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to switching lights on/off

        Arguments:
        text -- user-input, typically transcribed speech
    """
#todo: this needs to be faster

    apiai_return = False
    global CURRENT_ACTION_OBJ
    
    #need a check call to api.ai that there is a valid return
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)
    request = ai.text_request()
    request.query = text
    response = request.getresponse()
    responseDecode = json.loads(response.read())
    apiai_return = True if responseDecode['result']['action'] == 'switchLightsState' else False #proven
    
    #save the info to a global ApiaiActionObject
    if apiai_return:
    	CURRENT_ACTION_OBJ = ApiaiActionObject(responseDecode['result']['resolvedQuery'], responseDecode['result']['action'], responseDecode['result']['parameters']) #proven
    
    return  apiai_return
