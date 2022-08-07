import os
import pandas as pd
from flask import Flask, request, send_file


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
	if request.method == 'GET':
		return send_file('index.html')
	else:
		pd.DataFrame({
			'first_name': [request.form['fname']],
			'last_name': [request.form['lname']],
		}).to_csv('schedule.csv', index=False)
		return send_file('schedule.csv', as_attachment=True)
