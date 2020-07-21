from flask import Flask, jsonify

from block_info import block_info as bf

app = Flask(__name__)

@app.route('/block/<string:blockID>')
def blockInfo(blockID):
   return jsonify( bf(blockID) )

if __name__ == '__main__':
    app.run(debug=True)
