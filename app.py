from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "Project": "Count Pigs",
    "Description": "The main goal of this is to count the total of pigs in a farm by AI...",
    "Link": "Link 1"    
  },
  {
    "id": 2,
    "Project": "Weight Pigs",
    "Description": "The purpose of this initiative is to indicate the weight of the pigs by AI...",
    "Link": "Link 2"    
  }
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)