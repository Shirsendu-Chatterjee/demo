from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = int(data.get("num1", 0))
    num2 = int(data.get("num2", 0))
    result = num1 + num2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
