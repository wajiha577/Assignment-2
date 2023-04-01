#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:17:34 2023

@author: wajiha
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

default_countries_list = ['United States', 'India', 'China', 'Pakistan', 
                  'United Kingdom', 'Japan', 'Thailand', 'Uganda', 'Bangladesh',
                  'South Africa']


def read_data(file_path):
    """
    Parameters
    ----------
    file_path : String
        Complete absolute file path of the data in csv format.

    Returns
    -------
    data : DataFrame
        The cleaned data read from the file_path having years as columns.
    data_with_year_columns : DataFrame
        The cleaned data read from the file_path having countries as columns.

    """
    
    data = pd.read_csv(file_path)
    data = data.set_index("Country Name")
    data = data.dropna()
    transposed_data = data.copy()
    transposed_data = transposed_data.drop(
        ['Indicator Name', 'Indicator Code', 'Country Code'], axis=1)

    transposed_data = transposed_data.T
    data_with_country_columns = transposed_data.dropna()

    return data, data_with_country_columns.iloc[-20:]
    

def describe_data(df):
    """
    Parameters
    ----------
    df : DataFrame
        Dataframe object of data.
    This function is used to describe the data passed as the parameter.
    
    Returns
    -------
    None.

    """
    
    print(df.describe())
    print(df.max())
    print(df.min())
    

def time_series_plot(data, title, xlabel, ylabel):
    data_for_graph = data[default_countries_list ]
    plt.figure(figsize=(8,6))
    plt.plot(data_for_graph)
    plt.xlabel(xlabel)
    plt.xticks(rotation=75)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(default_countries_list, bbox_to_anchor=(1.0, 1), fontsize="7", 
               loc="upper right")
    plt.show()


def bar_plot(data, title, xlabel, ylabel):
    countries = ['India', 'China', 'Pakistan','Zambia', 'East Asia & Pacific',
                 'Turkiye']
    data = data.iloc[0:10]
    data = data[countries]
    # last_years_data = last_years_data.T
    plt.figure(figsize=(8,6))
    ax = data.plot(kind='bar')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    plt.xticks(rotation=0)
    ax.set_ylabel(ylabel)
    plt.legend(countries, bbox_to_anchor=(1.0, 1), fontsize="7", loc="upper right")
    plt.show()


def define_correlation():
    agricultural_data = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/data/data1.csv")
    agr_land_data, agr_land_data_year = read_data(agricultural_data)
     
    gdp = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/data/data3.csv")
    gdp_data, gdp_data_year = read_data(gdp)
    
    life_expect_at_birth = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/data/data4.csv")
    life_expect_at_birth_data, life_expect_at_birth_data_year = read_data(life_expect_at_birth)
    
    population_growth = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/data/data5.csv")
    population_growth_data, population_growth_data_year = read_data(population_growth)
    
    co2_data_path = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
        "/co2_metric_tons_per_capita/data.csv")
    co2_data, co2_data_year = read_data(co2_data_path)
    
    rural_population_data_path =  (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
        "/RuralPopulation.csv")
    rur_pop, rur_pop_year = read_data(rural_population_data_path)
    
    heatmap_data = pd.DataFrame({
            "Production of CO2: ":  co2_data_year['United States'],
            "Agricultural land (% of land area)": agr_land_data_year['United States'],
            "GDP (current US$)": gdp_data_year['United States'],
            "Life expectancy at birth": agr_land_data_year['United States'],
            "Population growth (annual %)": 
                population_growth_data_year['United States'],
            "Rural Population": rur_pop_year['United States']
        })
    fig, ax = plt.subplots(figsize = (12, 7))
    corr = heatmap_data.corr()
    corr.style.background_gradient(cmap ='coolwarm')
    sn.heatmap(corr, annot = True)
    

co2_data_path = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "\co2_metric_tons_per_capita\data.csv")
co2_data, co2_country_columned = read_data(co2_data_path)

population_data_path = (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "\population_growth_percentage\data.csv")

population_data, population_country_columned = read_data(population_data_path)
describe_data(co2_data)

time_series_plot(co2_country_columned, "CO2 Emissions in some countries",
                  "Year", "CO2 Emissions (metric tons per capita)")

time_series_plot(population_country_columned, "Population growth percentage by year",
                  "Year", "Population Growth")

define_correlation()

rural_population_data_path =  (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/RuralPopulation.csv")
rur_pop, rur_pop_country_columned = read_data(rural_population_data_path)

bar_plot(rur_pop_country_columned, "Rural Population growth by year", "Year",
          "Rural Population")


gdp_forest_path =  (r'C:\Users\wajih\OneDrive\Desktop\New Folder\wajihaassignement 2' + 
    "/GDPGrowthAgricultural.csv")

gdp_forest, gdp_forest_country_columned = read_data(gdp_forest_path)


bar_plot(gdp_forest_country_columned, "Agriculture, forestry, and fishing, value added (% of GDP)", 
          "Year", "Value added to GDP (%)")







































