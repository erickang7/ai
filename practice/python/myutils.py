import pandas as pd

def prepare_country_stats(oecd_bli, gdp_per_capita):
    #filter oecd_bli dataframe where INEQUALITY == TOT
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]

    # pivot dataframe with Country row, data column Indicator and value Value
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    
    # rename 2015 column in gdp_per_capita dataframe with GDP per capita
    gdp_per_capita.rename(columns = {"2015": "GDP per capita"}, inplace=True)

    # set "Country" as the index column of gpd_per_capaita dataframe
    gdp_per_capita.set_index("Country", inplace=True)
    
    # join oecd_bli and gdp_per_capita dataframews on indexes
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
    
    # sort dataframe by GDP per capita which will be X-axis in linear regression model
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    # filter outliers
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(len(full_country_stats))) - set(remove_indices))
    # return dataframe by selecting index, "GDP per capita" and "Life satisfaction" columns with filtered indices
    return full_country_stats[["GDP per capita", "Life satisfaction"]].iloc[keep_indices]
