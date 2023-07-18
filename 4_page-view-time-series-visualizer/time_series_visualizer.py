import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')
df.index = pd.to_datetime(df.index)

# Clean data
top = df['value'].quantile(0.975)
bottom = df['value'].quantile(0.025)
df = df[(df['value'] >= bottom) & (df['value'] <= top)]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(15, 5))
  plt.plot(df.index, df['value'], 'r')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set(xlabel='Date', ylabel='Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = [d.year for d in df.index]
  df_bar['month'] = [d.month for d in df.index]
  
  # Draw bar plot
  fig, ax = plt.subplots(figsize=(7, 7))
  sns.barplot(
    df_bar,
    x='year',
    y='value',
    hue='month',
    ax=ax,
  )
  plt.legend(loc='upper left', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
  ax.set(xlabel='Years', ylabel='Average Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df.index]
  df_box['month'] = [d.strftime('%b') for d in df.index]
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  df_box.sort_values('month', key = lambda x : pd.Categorical(x, categories=months, ordered=True), inplace=True)

  # Draw box plots (using Seaborn)
  fig, ax = plt.subplots(1, 2, figsize=(20, 10))
  sns.boxplot(df_box, x='year', y='value', ax=ax[0])
  sns.boxplot(df_box, x='month', y='value', ax=ax[1])
  ax[0].set(title='Year-wise Box Plot (Trend)',
            xlabel='Year',
            ylabel='Page Views')
  ax[1].set(title='Month-wise Box Plot (Seasonality)',
            xlabel='Month',
            ylabel='Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
