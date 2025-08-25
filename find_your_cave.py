#%%
import pandas as pd

#%%

df = pd.read_csv('caves_properties_summary_all_individual.csv',sep=';')
# %%

df[["mean_degree", "percentage_csdim"]].max()
# %%
high_degree = df[df.mean_degree > 2]
# %%
