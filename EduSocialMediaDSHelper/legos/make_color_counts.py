# %%
import pandas as pd
# %%
df_colors = pd.read_csv('colors.csv')
df_inventory_parts = pd.read_csv('inventory_parts.csv')
# %%
df_color_counts = df_inventory_parts.merge(df_colors, how='left', left_on='color_id', right_on='id')\
    .rename(columns={'name':'color_name'})\
    [['color_id', 'color_name', 'rgb', 'quantity']]
df_color_counts = df_color_counts.groupby(['color_id', 'color_name', 'rgb'])[['quantity']]\
    .sum().reset_index()
# %%
df_color_counts.to_csv('color_counts.csv', index=False)
# %%

