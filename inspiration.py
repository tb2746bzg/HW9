from flask import Flask
from flask import render_template
from random import randint

app=Flask(__name__)

l = []
with open('inspiration.txt') as fp:
    content = fp.read()
    l = content.strip().split('\n')
    n = len(l)

@app.route('/')
def random_quote():
    i = randint(0,n-1)
    quote = l[i]
    return render_template('inspiration.html',quote)
