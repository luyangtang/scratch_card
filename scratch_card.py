#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 07:53:09 2018

@author: lytang
"""

from flask import Flask, render_template
from maths import gift_prob,gift_name, generatePrizes # our own maths

app = Flask(__name__)

@app.route('/')
def scratch_card():
    
    length = 10
    width = 10
    sample = generatePrizes(length,width,gift_prob,gift_name)

    
    return render_template('index.html', sample = sample, length = length, width = width)

if __name__ == "__main__":
    app.debug = False
    app.run()   