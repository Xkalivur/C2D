from flask import Flask,render_template, request
import json
import random

codelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901234567890123456789"

app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    result = data
    code = ''.join(random.choice(codelist) for _ in range(6))
    with open('data.json', 'r') as file: 
        data = json.load(file)
    if result in data.keys():
        return result
    if result == "":
        return "Empty string cannot be used"
    data[result] = code
    with open('data.json', 'w') as file: 
        json.dump(data, file, indent=6)
    return result
    
if __name__ == '__main__':
    app.run(debug=True)
