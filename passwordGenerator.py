#!/bin/python3

import random

def passwordGenerator(numPass, lenght):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(!?.,)`~!@#$%^&*_+={}[];:"/<>-0123456789';
    for num in range(numPass):
        password = '';
        for count in range(lenght):
            password += random.choice(chars);
        return(password);

numPass = input('Enter the number of passwords you would like to generate: ')
lenght = int(input('Enter the desired lenght of password: '));
numPass = int(numPass)
print(passwordGenerator(numPass, lenght))
