import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = round(df['weight']/(df['height']/100)**2, 2)
df['overweight'] = np.where(BMI>25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol']==1, 0, 1)
df['gluc'] = np.where(df['gluc']==1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  filtered_df = df[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']] 
  df_cat = pd.melt(filtered_df, id_vars=['cardio'], var_name='variable', value_name='value') 


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
  cat_plot = sns.catplot(df_cat, x='variable', hue='value', col='cardio', kind='count').set_axis_labels('variable', 'total').fig

    # Get the figure for the output
  fig = cat_plot
  


    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi'])&
             (df['height']>=df['height'].quantile(0.025))&
             (df['height']<=df['height'].quantile(0.975))&
             (df['weight']>=df['weight'].quantile(0.025))&
             (df['weight']<=df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(1, figsize=(10,10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
