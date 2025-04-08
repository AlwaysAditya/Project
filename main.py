import pandas as pd
file = r'C:\Users\LEVONO\OneDrive\Documents\Semester6\Project3\Data Analytics Project\people_data.csv'
df = pd.read_csv(file)
a = df.head(50)
print(a)