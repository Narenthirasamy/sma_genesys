import warnings
import itertools
import json
import numpy as np
# import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
# plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
# import matplotlib
# matplotlib.rcParams['axes.labelsize'] = 14
# matplotlib.rcParams['xtick.labelsize'] = 12
# matplotlib.rcParams['ytick.labelsize'] = 12
# matplotlib.rcParams['text.color'] = 'k'

def get_FeaturePrediction():
	df = pd.read_excel(r"/sma_genesys/data/Feature_Prediction.xls")
	multicamera = df.loc[df['Category'] == 'MultiCamera']

	#Data Preprocessing
	cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Quantity', 'Discount', 'Profit']
	multicamera.drop(cols, axis=1, inplace=True)
	multicamera = multicamera.sort_values('Date')
	multicamera.isnull().sum()
	multicamera = multicamera.groupby('Date')['Reachability'].sum().reset_index()

	multicamera = multicamera.set_index('Date')
	y = multicamera['Reachability'].resample('MS').mean()

	p = d = q = range(0, 2)
	pdq = list(itertools.product(p, d, q))
	seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

	for param in pdq:
		for param_seasonal in seasonal_pdq:
			try:
				mod = sm.tsa.statespace.SARIMAX(y,
												order=param,
												seasonal_order=param_seasonal,
												enforce_stationarity=False,
												enforce_invertibility=False)
				results = mod.fit()

				#print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
			except:
				continue


	#Fitting the ARIMA model
	mod = sm.tsa.statespace.SARIMAX(y,
								order=(1, 1, 1),
								seasonal_order=(1, 1, 0, 12),
								enforce_stationarity=False,
								enforce_invertibility=False)
	results = mod.fit()

	pred_uc = results.get_forecast(steps=100)
	pred_ci = pred_uc.conf_int()

	# print(pred_uc.predicted_mean.to_json())

	return pred_uc.predicted_mean.to_json()

# if __name__== "__main__":
# 	get_FeaturePrediction()
