import pandas as pd

df = pd.read_excel('stu.xlsx')

print(df.loc[(df['语文'] < 60) | (df['数学'] < 60) | (df['英语'] < 60)])
print()
print(df.groupby('班级').mean())
