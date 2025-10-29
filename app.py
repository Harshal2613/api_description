from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ✅ Load CSV from same folder as app.py
csv_path = os.path.join(os.path.dirname(__file__), "DescriptionDataCoSupplyChain.csv")
data = pd.read_csv(csv_path)

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
