import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
import matplotlib

def get_FeatureReachability():
	df = pd.read_excel(r"C:\Users\mibrahim\Desktop\sma_genesys\Data\Prediction.xlsx", sheet_name='Sheet1')

	cols = ['Hour', 'User Name', 'Tweet content', 'Country', 'Place (as appears on Bio)', 'Followers', 'Following', 'ProductFeature']

	df.drop(cols, axis=1, inplace=True)

	json_data = df.to_json
	print(json_data)
	return json_data

if __name__== "__main__":
	get_FeatureReachability()

