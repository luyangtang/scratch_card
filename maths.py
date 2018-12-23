#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 08:19:14 2018

@author: lytang
"""

from math import floor
from random import sample

length = 30
width = 20

gift_name = {0: "小亲亲", 1: "吃火锅", 2: "马杀鸡", 3: "睡懒觉"}
gift_prob = {0: 0.5, 1: 0.1, 2:0.3, 3:0.1}

def generatePrizes(length,width,gift_prob,gift_name):
    total_num = length * width
    prizes_list = []
    for gift_id in gift_prob.keys():
        prizes_list += [gift_name[gift_id]] * floor(total_num * gift_prob[gift_id])
        
#    prizes_list = shuffle(prizes_list)
    
    prizes_list = sample(prizes_list,len(prizes_list))
        
    prize_array = []
    for row in range(0,width):
        tmp_row = []
        for col in range(0,length):
            tmp_row += [prizes_list[0]]
            prizes_list.pop(0)
        prize_array += [tmp_row]
    return prize_array
        
