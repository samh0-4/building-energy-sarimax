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



## 3. Methods

### 3.1 Degree-day regression (LINEST)

### 3.2 Change-point regression (ECAM)

### 3.3 SARIMAX

## 4. Evaluation

## 5. Results

## 6. Discussion

## 7. Conclusion

## References
