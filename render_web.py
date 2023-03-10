from flask import Flask, jsonify, request, render_template
  
app = Flask(__name__)
  
  
@app.route('/', methods=['GET'])
def main():
    return render_template("render.html")
  
  
if __name__ == '__main__':
    app.run(debug=True)