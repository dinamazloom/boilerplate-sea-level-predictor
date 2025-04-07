import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # 3. Line of best fit (1880 to 2050)
    full_reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(1880, 2051))
    y_full = full_reg.slope * x_full + full_reg.intercept
    plt.plot(x_full, y_full, color='blue', label='Best Fit: All Data')

    # 4. Line of best fit (2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    recent_reg = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = recent_reg.slope * x_recent + recent_reg.intercept
    plt.plot(x_recent, y_recent, color='red', label='Best Fit: 2000+ Data')

    # 5. Customize plot
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # 6. Save and return figure
    plt.tight_layout()
    fig = plt.gcf()
    fig.savefig('sea_level_plot.png')
    return fig
