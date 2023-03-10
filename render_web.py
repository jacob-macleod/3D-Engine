from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
  
@app.route('/', methods=['GET'])
def main():
    return "Hellow world"
  
  
if __name__ == '__main__':
    app.run(debug=True)