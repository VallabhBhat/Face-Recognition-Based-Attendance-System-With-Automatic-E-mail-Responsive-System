import pandas as pd
web = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[69,67,78,65,45,52]}
df = pd.DataFrame(web)
df.to_csv('attendence.csv')
print(df)

