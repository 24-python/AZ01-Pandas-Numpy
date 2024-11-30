import pandas as pd
#
# data = [1, 2, 3, 4, 5]
#
# series = pd.Series(data)
#
# print(series)

# data = {
#     'Name': ['Tom', 'nick', 'krish', 'jack'],
#     'Age': [20, 21, 19, 18],
#     'City': ['London', 'Manchester', 'Liverpool', 'Bristol']
#     }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')

print(df.loc[9])
