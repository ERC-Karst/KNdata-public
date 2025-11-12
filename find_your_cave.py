#%%
import pandas as pd

#%%

df = pd.read_csv('C:/Users/celia/github/erc-karst-repositories/KNdata-public/caves_properties_summary_all_individual.csv',sep=';')
# %%
geometry = df.percentage_csdim > 80
# mean_degree = df.mean_degree > 2.2
length = df.total_length > 100000

result = df[length][['id_dataset','short_name','id_subset','total_length','mean_degree','percentage_csdim']].sort_values(by=['total_length','percentage_csdim'],ascending=False)
print(result)
result.to_csv('selected_caves.csv')

# %%

# %%
