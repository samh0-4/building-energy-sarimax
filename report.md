# Comparing Baseline Methods for Building Energy Use

Samuel Hingston · November 2026

## Summary
The aim of this report is to compare three standard ways of building an energy baseline for an office building in London: degree-day linear regression, an ECAM-style change-point model and SARIMAX. Each of the models is built using hourly electricity and weather data for an office building from the Building Data Genome Project 2 (BDG2), an open dataset of over 1,600 non-residential buildings.

## 1. Introduction
To understand why we model energy usage for buildings, its best to start with what a baseline is. Baselines are reference points, an estimate of what would have happened if nothing changed. For example, in clinical trails one group is given a placebo so that patients who would have recovered anyway are not credited towards the drug being tested. The effect of interest can only be measured against an estimate of what would have happened without it.

We see the same problem appearing within real estate, whether that be homes, flats or sky scrapers. For example, if a building has insulation fitted in the autumn season and its winter gas usage drops, we would typically assume that the insulation has worked. Correlation doesn't always mean causation. What if the winter was milder compared to previous years, meaning there was less demand for heating within the home/building? Without a baseline that accounts for the weather, the two cannot be told apart.

## 2. Data

### 2.1 Source
The data for this project comes from the [Building Data Genome Project 2](https://github.com/buds-lab/building-data-genome-project-2) (BDG2), an open dataset of hourly meter readings from over 1,600 non-residential buildings, mostly university campuses, covering the years 2016 and 2017. Hourly weather data is also in the dataset. This dataset was picked in particular as it contains real metered data for a full 24 months along with matching weather data for every building.

### 2.2 Building selection
One office building was selected from this dataset: 'Robin_office_Antonia', at the Robin site in central London. It was built in 1955 with a floor area of 6,100 m² and is heated via gas. As the heating is not electric, its electricity use only covers cooling, lighting, equipment and ventilation, so it is expected to increase in relation to rising outside temperatures as opposed to decreasing outside temperatures.

One of the main reasons this building is suitable for this study is that it has a complete hourly electricity record for 2016, with only small meter dropouts in 2017. The data also responds directly to changes in outdoor temperature along with no step changes in consumption between the two years. Finally, its very much relevant to UK commercial energy management due to the fact its a London office building.

### 2.3 Weather and degree days

The hourly outdoor air temperature for this site was averaged in order to give a daily mean temperature. There was about 29 missing temperatures across the two years, which are filled using linear interpolation.

However, even though we have outside air temperature this isnt what we use to model energy usage. Instead, we use heating degree days (HDD) and cooling degree days (CDD). Degree days measure how much heating or cooling a building is likely to need. HDD adds up how far the daily mean temperature falls below a base temperature and CDD how far it rises above one. We represent this mathematically as follows:

```math
\mathrm{HDD} = \max(T_{\text{base}} - T_{\text{mean}},\ 0), \qquad \mathrm{CDD} = \max(T_{\text{mean}} - T_{\text{base}},\ 0)
```
where $\bar{T}_d$ is the mean of the hourly temperature on day *d* and  
A base temperature of 15.5 °C is the UK standard which was used for both HDD and CDD.



## 3. Methods

### 3.1 Degree-day regression (LINEST)

### 3.2 Change-point regression (ECAM)

### 3.3 SARIMAX

## 4. Evaluation

## 5. Results

## 6. Discussion

## 7. Conclusion

## References
