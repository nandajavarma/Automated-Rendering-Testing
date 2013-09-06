from flask import Flask, render_template, request
import os
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
	ff = request.form['fontfile']
	wf = request.form['testcases']
	rf = request.form['referencefile']
	rendf = request.form['renderedoutput']
	outfile = request.form['outputfile']
	errorfile = request.form['errorfile']
	mydir = request.form['directory']
	return render_template('success.html')

@app.route('/about')
def about():
  return render_template('about.html')
 
if __name__ == '__main__':
  app.run(debug=True)
