from flask import Flask, jsonify, request, render_template
from read_obj import generate_coordinate_pairs
  
app = Flask(__name__)
  
  
@app.route('/', methods=['GET'])
def main():
    return render_template("render.html", coords=generate_coordinate_pairs("example_file.obj"))
  
  
if __name__ == '__main__':
    app.run(debug=True)
