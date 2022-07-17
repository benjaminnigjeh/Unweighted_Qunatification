import pandas as pd
df = pd.DataFrame.from_csv('input.csv')
group = df.groupby(['Replicate Name', 'Protein Name'])
df_sum = group.sum()
df1 = df_sum.xs('RC3_DIA',level=0,axis=0)
df1.to_csv('output.csv')
