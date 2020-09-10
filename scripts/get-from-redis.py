#!/usr/bin/env python3

import redis
import threading
import time
import pickle

r = redis.Redis(host='localhost', port=6379, db=0)

def get_alphabet():
    output = r.get("alphabet")
    alpha = pickle.loads(output)
    print(alpha)

def get_numbers():
    output = r.get("numbers")
    number = pickle.loads(output)
    print(number)


t = threading.Thread(name='alphabet', target=get_alphabet)
w = threading.Thread(name='numbers', target=get_numbers)
t.start() 
w.start() 


