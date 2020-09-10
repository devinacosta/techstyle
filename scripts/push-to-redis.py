#!/usr/bin/env python3

import redis
import threading
import time
import pickle

r = redis.Redis(host='localhost', port=6379, db=0)

list_alphabet = []
list_numbers = []

alpha = 'a'
for i in range(0, 26):
    list_alphabet.append(alpha)
    alpha = chr(ord(alpha)+1)

for i in range(1, 25):
    list_numbers.append(i)

my_alpha = pickle.dumps(list_alphabet)
my_numbers = pickle.dumps(list_numbers)

def push_alphabet():
    r.set("alphabet",my_alpha)

def push_numbers():
    r.set("numbers",my_numbers)


t = threading.Thread(name='alphabet', target=push_alphabet)
w = threading.Thread(name='numbers', target=push_numbers)
t.start() 
w.start() 

print(list_alphabet)
print(list_numbers)

