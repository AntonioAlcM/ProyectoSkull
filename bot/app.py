from flask import Flask, json, request
from contendores import *

app = Flask(__name__)

@app.route('/')
def status():
 return json(status='OK')

@app.route('prueba')
def prueba(){
 return json(getclasificacion())
