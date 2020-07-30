import json
import time
import threading
import random
import requests

with open('config.json') as config_data:
    config = json.load(config_data)

START_TEMP = config['start_temp']
INCREMENT_DEG = config['increment_deg']
DECREMENT_DEG = config['decrement_deg']
MOD_INTERVAL = config['mod_interval']
SERVER_URL = config['request_url']
N_DEG = config['normalize_deg']
N_INTERVAL = config['n_interval']

def adjust_temp(target_temp, current_temp):
    if target_temp > round(current_temp, 1):
        time.sleep(MOD_INTERVAL)
        current_temp += INCREMENT_DEG
        print('current_temp: '+str(current_temp))
    elif target_temp < round(current_temp, 1):
        time.sleep(MOD_INTERVAL)
        current_temp -= DECREMENT_DEG
        print('current_temp: ' + str(current_temp))
    else:
        print('Temperatures matched')
    
    return current_temp

def normalize(outside_temp, current_temp):
    print('Normalizing temperature...')
    print('Outside temperature: '+ str(outside_temp))
    print('current_temp: '+str(current_temp))
    while outside_temp > current_temp:
        time.sleep(N_INTERVAL)
        current_temp += N_DEG
        print('current_temp: '+str(current_temp))
    while outside_temp < current_temp:
        time.sleep(N_INTERVAL)
        current_temp -= N_DEG
        print('current_temp: '+str(current_temp))
    return current_temp


#TODO Ask server for the target temp
#Right now this only returns a random double between 23 and 27 excluding 25
def get_target_temp():
    response = requests.get(SERVER_URL)
    return int(response['target_temp'])

current_temp = START_TEMP
target_temp = 26.0
while(round(current_temp,1) != target_temp):
    current_temp = adjust_temp(target_temp, current_temp)








        




