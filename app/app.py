import os
import json
from flask import Flask
import feature_Prediction
import feature_reachability
import sentimental_analysis


app = Flask(__name__)


@app.route("/")
def index():
    """
    Home page
    """
    chart_data = {}
    return chart_data

@app.route("/feature_pred/")
def feature_pred():
    chart_data = feature_Prediction.get_FeaturePrediction()
    chart_data = json.dumps(chart_data, indent=2)
    return chart_data

@app.route("/feature_reach/")
def feature_reach():
    data = feature_reachability.get_feature_reachability()
    data = json.dumps(data, indent=2)
    return data

@app.route("/sent_analysis/")
def sentiment_analysis():
    data = sentimental_analysis.get_Sentiments()
    data = json.dumps(data, indent=2)
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
