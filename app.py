#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3

# -*- coding: utf8 -*-
# 
# date                 :- 
# author               :- Md Jabed Ali(jabed)

import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import pandas
import os
import time
from flask import Flask, flash, redirect, render_template, request, session, abort
from pusher import Pusher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = os.urandom()
    app.run(debug=True, port=)
