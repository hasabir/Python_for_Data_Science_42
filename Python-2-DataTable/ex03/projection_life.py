
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def main():
    income_per_person = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")

    # Include the country column and filter for the year 1900
    income_1900 = income_per_person[["country", "1900"]].rename(columns={"1900": "GDP_1900"})
    life_expectancy_1900 = life_expectancy[["country", "1900"]].rename(columns={"1900": "LifeExpectancy_1900"})

    print(income_1900.head())
    print(life_expectancy_1900.head())

    # Merge the data on the country column
    merged_data = pd.merge(income_1900, life_expectancy_1900, on="country")
    print(merged_data.head())

    # Plot the data
    plt.figure()
    plt.scatter(merged_data["GDP_1900"], merged_data["LifeExpectancy_1900"])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()

if __name__ == "__main__":
    main()
