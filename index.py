python
from flask import Flask, render_template, jsonify
import pandas as pd

# Load dataset
data = pd.read_excel("DL99-ISIC-Activities-ADRA-OD-018-AIS.xlsx")

# Initialize Flask application
app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    # Convert dataset to JSON format
    data_json = data.to_dict(orient='records')
    return jsonify(data_json)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
