import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = list(range(df['Year'].min(), 2051))
    y_all = [intercept + slope*x for x in x_all]
    plt.plot(x_all, y_all, 'r', label='Fit: all years')
    
    # Create second line of best fit (from 2000 to most recent year)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = list(range(2000, 2051))
    y_2000 = [intercept_2000 + slope_2000*x for x in x_2000]
    plt.plot(x_2000, y_2000, 'g', label='Fit: 2000 onwards')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
