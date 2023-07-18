import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Real Data')
  
    # Create first line of best fit
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = reg.intercept+(reg.slope*x1)
    plt.plot(x1, y1, 'r', label='Prediction data from year 1880-2050')

    # Create second line of best fit
    df2000 = df.loc[df['Year']>=2000]
    reg2000 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = reg2000.intercept+(reg2000.slope*x2)
    plt.plot(x2, y2, 'g', label='Prediction data from year 2000-2050')

    # Add labels and title
    plt.legend()
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    ax.set_xlim(1850, 2075)
    ax.set_ylim(df['CSIRO Adjusted Sea Level'].min() - 2, 20)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()