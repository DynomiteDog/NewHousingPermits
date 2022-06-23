# Python API that establishes a connection and displays a column of information from the Federal Reserve Economic Data website
	# Selecting a series in FRED
	# The instalation packages to create a column structure output:
    # https://pandas-datareader.readthedocs.io/en/latest/genindex.html
!pip install pandas-datareader -q
	
	# Next, import the necessary packages.
import requests # data from api
import pandas_datareader as pdr # access fred
import pandas as pd
import plotly.express as px # visualize
from datetime import datetime
	
	# Create a variable where you will store your API key as a string type object.
		# extract api key example key from FRED: abcdefghijklmnopqrstuvwxyz123456
fred_api_key = 'https://api.stlouisfed.org/fred/series/search?api_key=abcdefghijklmnopqrstuvwxyz123456&search_text=canada'

# Retrieving data for a single series in New Private Housing Units Authorized by Building Permits for Ohio (OHBPPRIVSA)
    # https://fred.stlouisfed.org/series/OHBPPRIVSA
	# This is a function to retrieve the data and reset the index 

def get_fred_data(param_list, start_date, end_date):
  df = pdr.DataReader(param_list, 'fred', start_date, end_date) # this gives us the DATE field as a column
  return df.reset_index() # rebuilds the indexing based on the defined param_list

# Next, call the function and define the parameters
    # create a variable to hold the value of the series
series = 'OHBPPRIVSA' 

    # get data for series
df = get_fred_data(param_list=[series], 
                   start_date='2021-01-01', 
                   end_date='2021-12-31')

# plotly.express
# plot
fig = px.line(df, x="DATE", 
                y="OHBPPRIVSA", 
                title='New Private Housing Units Authorized by Building Permits')
fig.show()



