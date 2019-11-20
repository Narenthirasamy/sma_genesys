import warnings
import itertools
import numpy as np
import json
# import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
# plt.style.use('fivethirtyeight')
import pandas as pd
import statsmodels.api as sm
# import matplotlib

# def get_FeatureReachability1():
# 	df = pd.read_excel(r"~/IWC/sma_genesys/data/Prediction.xlsx",
#                      sheet_name='Sheet1')
#
# 	cols = ['Hour', 'User Name', 'Tweet content', 'Country', 'Place (as appears on Bio)', 'Followers', 'Following', 'ProductFeature']
#
# 	df.drop(cols, axis=1, inplace=True)
#
# 	json_data = df.to_json
# 	print json.dumps(json_data)
  # json_data = {"lat": ["40.7142",
	# 	"37.69964945",
	# 	"41.87864",
	# 	"29.73222",
	# 	"19.4271",
	# 	"37.7749295",
	# 	"43.7315236",
	# 	"28.35272725"
	# ],
	# "lng": [
	# 	"-74.0064",
	# 	"-118.3975983",
	# 	"-123.01183239",
	# 	"-87.64024999999999",
	# 	"-95.38751999999999",
	# 	"-99.1276",
	# 	"-122.4194155",
	# 	"-79.6083704",
	# 	"-81.60341115999999"
	# ],
	# "reach": [
	# 	"7523",
	# 	"6698",
	# 	"4382",
	# 	"3325",
	# 	"2876",
	# 	"2709",
	# 	"2328",
	# 	"2290",
	# 	"2252"
	# ]}
  # return json_data


def get_feature_reachability():
  df = pd.read_excel(r"/sma_genesys/data/Prediction.xlsx",
                     sheet_name='Sheet1')

  cols = ['Hour', 'User Name', 'Tweet content', 'Country',
          'Place (as appears on Bio)', 'Followers', 'Following',
          'ProductFeature']
  json_data = {"lat": ["40.7142","33.9442368","37.69964945","41.87864",
                       "29.73222","19.4271","37.7749295","43.7315236",
                       "28.35272725"],
               "lng": ["-74.0064","-118.3975983","-123.01183239",
                        "-87.64024999999999","-95.38751999999999",
                        "-99.1276","-122.4194155","-79.6083704",
                        "-81.60341115999999"],
               "reach": ["7523","6698","4382",
                         "3325","2876","2709","2328","2290","2252"]}
  return json_data



# if __name__== "__main__":
# 	get_feature_reachability()

