from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load your CSV file
data = pd.read_csv(r"C:\Users\harsh\OneDrive\Desktop\Infosys\StaticData\DescriptionDataCoSupplyChain.csv")

# Show all CSV data directly on home route
@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
