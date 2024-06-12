import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    xlim = (1850, 2075)
    xticks = np.arange(1850., 2076, 25)
    df[['Year', 'CSIRO Adjusted Sea Level']].plot.scatter(
        x='Year',
        y='CSIRO Adjusted Sea Level',
        ax=ax,
        color='blue',
        xlim=xlim,
        xticks=xticks,
        title='Rise in Sea Level',
        xlabel='Year',
        ylabel='Sea Level (inches)'
    )

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # ax.axline(xy1=(0, line1.intercept), slope=line1.slope, color='r')

    # Create second line of best fit
    line2 = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])
    # ax.axline(xy1=(0, line2.intercept), slope=line2.slope, color='g')

    # Alternative method for passing tests
    xArrayLine1 = np.arange(1880, 2051)
    yArrayLine1 = (line1.slope * xArrayLine1 + line1.intercept)
    xArrayLine2 = np.arange(2000, 2051)
    yArrayLine2 = (line2.slope * xArrayLine2 + line2.intercept)
    df.loc[df['Year'] < 2000, 'second_line'] = None
    ax.plot(
        xArrayLine1,
        yArrayLine1,
        color='red'
    )
    ax.plot(
        xArrayLine2,
        yArrayLine2,
        color='blue',
    )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
