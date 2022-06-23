# We can visualize the data using plotly.express.

# plot
fig = px.line(df, x="DATE", 
                y="OHBPPRIVSA", 
                title='New Private Housing Units Authorized by Building Permits')
fig.show()



