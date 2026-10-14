# Title: Excess nitrogen per hectare of cropland

## Research question

How is excess nitrogen per hectare of cropland distributed across countries and continents in 2009? Is a positive nitrogen excess common worldwide, and what does the global distribution look like?

## Dataset

This dataset is from 'Our World in Data'.

This dataset is retrieved from: 

West, P. C. et al. (2014), Leverage points for improving global food security and the environment, Science, 345(6194), 325-328.

Dataset page:

https://ourworldindata.org/grapher/excess-nitrogen-per-hectare

The excess nitrogen per hectare is measured in kilograms per hectare (kg/ha). It is the difference between nitrogen inputs (fertilizers, manure and fixation) and nitrogen removed in the crops that were harvested.

The CSV used contains 193 countries observations for 2009. There is one observation per country.

### Interpretation

A positive value means that the nitrogen inputs were larger than the amount amount of nitrogen removed in harvested crops. A negative value means that the estimated nitrogen removed was larger than the nitrogen input.

The dataset and analysis counts each country as one observation. So when said "79.8% are positive" it means that 79.8% of the observations are and not 79.8% of global cropland is.

## all files made in the project

- `analysis.py` analysis made in python.
- `excess-nitrogen-per-hectare.csv` the dataset from our world in data.
- `report.tex` the LaTeX report.
- `global_distribution.png` data displayed in histrogram created by the code.
- `continent_means.png` continent comparison plot created by the code.
- `continent_summary.csv`continent-level results created by the code.

## packages

The project uses the following:

- Python 3
- NumPy
- pandas
- matplotlib
- statistics

## Installation

Open the project folder (excess_nitrogen_project) in Visual Studio Code.

Open the VS Code terminal and run:

"python3 -m pip install numpy"

then 

"python3 -m pip install pandas"

then

"python3 -m pip install matplotlib"

## Run the analysis

Make sure the terminal is inside the project folder, then run the file.

The program:

1. it loads the CSV using `pd.read_csv`.
2. checks the number of observations and missing values.
3. assigns each observation to a continent.
4. calculates mean, median, standard deviation and standard error.
5. calculates skewness and kurtosis.
6. calculates the percentage of observations with a positive nitrogen surplus.
7. calculates a binomial-style uncertainty.
8. compares the continents.
9. prints the highest and lowest observations.
10. creates two plots.
11. saves a continent summary CSV.

## Data cleaning

No missing values, no data cleaning was needed. The only preperation that was needed to be done is adding the countries to continents for the project analysis.

## summary of the results

The nitrogen measurement is continuous. A normal distribution is therefore a useful reference, but skewness and kurtosis are used to check whether the observed distribution looks approximately normal. Poisson and binomial distributions are more naturally connected to counts; the number of positive observations is treated as a binomial-type quantity. A uniform distribution is not expected because the measurements are not evenly spread across the range.

## Reproducibility

Another student can easily reporduce this project. A link to the data was added in this READme file and the data doesn't need any cleaning.
