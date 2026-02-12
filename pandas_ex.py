import pandas as pd

data = [101,102,104,106]

series = pd.Series(data, index = ["Room1","Room2","Room3","Room4"])

print(series)