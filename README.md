# U.S. Gas Prices, Crude Oil, and Inflation

*A data-analysis project examining how gasoline prices moved in relation to crude-oil prices, inflation, and regional market differences from 2023–2026.*

## Business Question

How have U.S. gasoline prices changed since 2023, and what relationships can be observed among gasoline prices, crude-oil prices, inflation, and regional price patterns?

## Intended Audience

Consumers, financial-services professionals, policymakers, and business analysts interested in understanding the economic and regional factors associated with fuel-price changes.

## Data Sources

- **U.S. Energy Information Administration (EIA):** Weekly gasoline and crude-oil price data
- **Federal Reserve Economic Data (FRED):** Consumer Price Index data used to represent inflation
- **Analysis period:** May 18, 2023 through 2026

## Tools and Technologies

- Python
- Pandas
- Jupyter Notebook
- Matplotlib
- Seaborn
- Plotly
- EIA Open Data
- FRED API
- Git and GitHub

## Analytical Approach

- Collected gasoline, crude-oil, and inflation data from multiple public sources
- Cleaned and standardized dates and numeric fields
- Aligned weekly datasets using shared date ranges
- Merged gasoline, crude-oil, and CPI data for comparative analysis
- Normalized the series to compare variables with different measurement scales
- Evaluated the relationship between gasoline and crude-oil prices
- Compared average gasoline prices across Petroleum Administration for Defense Districts (PADDs)
- Developed static and interactive visualizations to communicate findings

## Key Findings

- Gasoline and crude-oil prices generally followed similar directional patterns during the analysis period.
- Gasoline prices changed less immediately than crude-oil prices, reflecting differences in how upstream price changes reach consumers.
- CPI followed a steadier pattern and was considerably less volatile than gasoline and crude oil.
- Regional analysis showed persistent differences in average gasoline prices across PADD regions.
- The findings indicate a visible relationship between crude oil and gasoline prices, while inflation followed a broader and more gradual trend.

## Project Evidence

- [View Sal’s Analysis Notebook](notebooks/sal.ipynb)
- [Normalized Gas, Oil, and CPI Trends](data/processed/Normalized%20trends.png)
- [Crude Oil and Gasoline Relationship](data/processed/Relationship%20btwn%20crude%20oil%20and%20gas.png)

## Individual Contribution

**Sal** prepared and aligned weekly gasoline and crude-oil price data across the shared 2023–2026 analysis period and merged the datasets by week for consistent comparison. She analyzed the relationship among gasoline prices, crude-oil prices, and inflation; standardized the three measures to make their different scales visually comparable; and developed a normalized trend chart and a crude-oil versus gasoline scatterplot with a trendline. She also calculated the Pearson correlation coefficient to measure the relationship between crude-oil and gasoline prices and documented her analysis and findings in `notebooks/sal.ipynb`.

**Aman** Developed the API connections used to retrieve project data and contributed to data collection and preparation. Created Repo organization and outline. Explored the relationship between crude-oil prices and inflation, analyzed their movement over time, and documented findings in `notebooks/ahmad.ipynb`. |

## Limitations and Future Work

- The aligned analysis begins in May 2023 and does not cover the full period immediately following the onset of COVID-19.
- Correlation and similar directional movement do not establish causation.
- National and regional averages may obscure differences among individual states and local markets.
- Future analysis could incorporate fuel taxes, refinery capacity, supply disruptions, seasonal demand, and additional state-level data.

# Original Project Scope and Planning Notes

The following notes document the team’s original project scope and proposed variables.
# Overview

## What does our dataset explore?

How U.S. gasoline prices vary across time and location, and what economic and regional factors explain those changes.

## Dependent Variable

Gasoline price per gallon (regular, premium, diesel)

## Independent Variables

- State / region (location)
- Date (time)
- Fuel type (regular, premium, diesel)
- Crude oil price (WTI/Brent)
- Season / month
- Inflation (CPI)
- Optional: tax rates, supply region (PADD)

### Variable Types

- **Quantitative:** gas price, crude oil price, CPI
- **Categorical:** state, fuel type, region, season/month
- **Time-based:** date (weekly/monthly trend)

## Number of Independent Variables

6–8 main variables

## Dataset Size

~5,000–50,000 rows (weekly data across multiple states and years)

## Summary

A time-series + panel dataset combining U.S. gasoline prices with geographic, and macroeconomic factors to analyze what drives price variation over time and across states. Also, if there was a spike in increase of oil, gas price in the last decade and how did it impact inflation. What kind of relation does oil, gas, national prices and inflation have?
