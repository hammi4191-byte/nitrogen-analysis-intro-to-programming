import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt #to graph data easy

#Excess nitrogen per hectare of cropland project

# step 1: load the data
data = pd.read_csv("excess-nitrogen-per-hectare.csv")

column = "Excess nitrogen per hectare of cropland"
print("number of observations:", len(data))
print("Year of data measurement", data["Year"].unique()) #.unique to make sure it only writes 2009 ones
# data set only has year 2009, thats the year of all the measurements done

# step 2: continent classification (add all countries into continents to be able to make conclusions and compare)
africa = "DZA AGO BEN BWA BFA BDI CMR CPV CAF TCD COM COG CIV COD DJI EGY GNQ ERI SWZ ETH GAB GMB GHA GIN GNB KEN LBR LBY MDG MWI MLI MRT MUS MAR MOZ NAM NER NGA REU RWA STP SEN SLE SOM ZAF SSD SDN TZA TGO TUN UGA ZMB ZWE".split()

asia = "AFG ARM AZE BHR BGD BTN BRN KHM CHN CYP GEO HKG IND IDN IRN IRQ ISR JPN JOR KAZ KWT KGZ LAO LBN MAC MYS MNG MMR NPL PRK OMN PAK PSE PHL SAU SGP KOR LKA SYR TWN TJK THA TLS TUR TKM ARE UZB VNM YEM OWID_KOS OWID_CYN".split()

europe = "ALB AUT BLR BEL BIH BGR HRV CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX MLT MDA MNE NLD MKD NOR POL PRT ROU RUS SMR SRB SVK SVN ESP SWE CHE UKR GBR".split()

north_america = "ATG BHS BRB BLZ CAN CYM CRI CUB DMA DOM SLV GRD GLP GTM HTI HND JAM MEX MSR NIC PAN PRI KNA LCA VCT TTO USA GUM MNP MTQ".split()

south_america = "ARG BOL BRA CHL COL ECU GUY PRY PER SUR URY VEN GUF".split()

oceania = "AUS FJI NZL PNG SLB VUT NCL".split()

data["Continent"] = "Unknown" # extra column with continents initially gets unknow but now we will add the continents to it with a loop

for i in range(len(data)):
    code = data.loc[i, "Code"]
    if code in africa:
        data.loc[i, "Continent"] = "Africa"
    elif code in asia:
        data.loc[i, "Continent"] = "Asia"
    elif code in europe:
        data.loc[i, "Continent"] = "Europe"
    elif code in north_america:
        data.loc[i, "Continent"] = "North America"
    elif code in south_america:
        data.loc[i, "Continent"] = "South America"
    elif code in oceania:
        data.loc[i, "Continent"] = "Oceania"

# maybe add a check wether every code received a continent

# step 3: convert all the measurements to numpy array
values = np.array(data[column]) # column = is the earlier mentioned column "excess nitrogen per hectare of cropland"

# statistics: calculate the amount of values, mean, median, standard deviation.
n = len(values)
mean = np.mean(values)
median = np.median(values)
standard_deviation = np.std(values, ddof=1)

# calculate the standard error (uncertainty of the mean) and the highest and lowest value
standard_error = standard_deviation / np.sqrt(n)
minimum = np.min(values)
maximum = np.max(values)

# use pandas to calculate the skewness and kurtosis
series = pd.Series(values)
skewness = series.skew()
kurtosis = series.kurtosis()

# step 4: Answer the question wether a positive nitrogen surplus is common
positive = np.sum(values > 0)
negative = np.sum(values < 0)
positive_percentage = 100 * positive / n

# calculate the uncertainty of step 4
p = positive / n
proportion_uncertainty = np.sqrt(p * (1 - p) / n)
proportion_uncertainty_percent = 100 * proportion_uncertainty

# step 5: print the results of the overall/global data
print("\nGLOBAL RESULTS")
print("------------------------------")
print("Number of observations:", n)
print("Mean:", round(mean, 2), "kg/ha")
print("Median:", round(median, 2), "kg/ha")
print("Standard deviation:", round(standard_deviation, 2), "kg/ha")
print("Standard error of mean:", round(standard_error, 2), "kg/ha")
print("Minimum:", round(minimum, 2), "kg/ha")
print("Maximum:", round(maximum, 2), "kg/ha")
print("Skewness:", round(skewness, 2))
print("Excess kurtosis:", round(kurtosis, 2))
print("Positive surplus:", positive, "of", n)
print("Positive surplus percentage:", round(positive_percentage, 1), "%")
print("Approx. uncertainty of percentage:", round(proportion_uncertainty_percent, 1), "percentage points")

# step 6: the analysis on continent level (to draw conclusions)
#first make array for coninents and add countries to it with a for loop
continents = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
continent_rows = []

#now add values and countries to the array
for continent in continents:
    continent_values = np.array(data.loc[data["Continent"] == continent, column])

    #now do all the calculations for the continents
    count = len(continent_values)
    continent_mean = np.mean(continent_values)
    continent_median = np.median(continent_values)
    continent_std = np.std(continent_values, ddof=1)
    continent_se = continent_std / np.sqrt(count)
    continent_positive = np.sum(continent_values > 0)
    continent_positive_percentage = 100 * continent_positive / count

# now we are going to make the table to store all the data for the continents in
    continent_rows.append([
        continent,
        count,
        continent_mean,
        continent_median,
        continent_std,
        continent_se,
        continent_positive_percentage
    ])

continent_table = pd.DataFrame(
    continent_rows,
    columns=[
        "Continent",
        "N",
        "Mean",
        "Median",
        "Std",
        "SE",
        "Positive_percent"
    ]
)

# now we are going to print the continent results 
print("\nCONTINENT RESULTS")
print("---------------------")
# print the continent table
print(continent_table.round(2).to_string(index=False))
# print the countries with highest and lowest nitrogen values
sorted_data = data.sort_values(column, ascending=False)
print("\nHIGHEST VALUES")
print(sorted_data[["Entity", column]].head(5).round(2).to_string(index=False))

print("\nLOWEST VALUES")
print("------------------------------")
print(sorted_data[["Entity", column]].tail(5).round(2).to_string(index=False))

# now we make the distribution plot of the data
# this plot shows the global distribution of the measurements
plt.figure(figsize=(8, 5))
plt.hist(values, bins=20, edgecolor="black")
plt.axvline(mean, linestyle="--", linewidth=2, label="Mean")
plt.axvline(median, linestyle=":", linewidth=2, label="Median")
plt.xlabel("Excess nitrogen per hectare (kg/ha)")
plt.ylabel("Number of countries")
plt.title("Global distribution of excess nitrogen per hectare, 2009")
plt.legend()
plt.tight_layout()
plt.savefig("global_distribution.png", dpi=200)
plt.show()

# now we make a bar chart that shows the average mean value per continent
# 9. Mean value by continent.
plt.figure(figsize=(8, 5))
plt.bar(continent_table["Continent"], continent_table["Mean"])
plt.axhline(0, linewidth=1)
plt.xlabel("Continent")
plt.ylabel("Mean excess nitrogen (kg/ha)")
plt.title("Mean excess nitrogen by continent, 2009")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("continent_means.png", dpi=200)
plt.show()

#now we save the continent table in a seperate file 
# 10. Save the continent table so the result can be checked easily.
continent_table.round(2).to_csv("continent_summary.csv", index=False)

# interpretation of results of the distributions
print("\nDISTRIBUTION INTERPRETATION")
print("---------------------")
print("The measurements are continuous, so we use a normal distribution as a")
print("reference model, but the skewness and kurtosis show that the data are")
print("not normally distributed. Poisson and binomial distributions are mainly")
print("for counts/proportions; here the positive-surplus count can be viewed")
print("as a binomial-type result. A uniform distribution is not a good")
print("description because the values are concentrated unevenly and have")
print("large negative and positive extremes.")

print("\nDone. The plots and continent_summary.csv were created.")






