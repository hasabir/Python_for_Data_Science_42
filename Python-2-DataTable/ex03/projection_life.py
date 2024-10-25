
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    ''' the main function of the script projection_life.py '''
    income_per_person =\
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")

    income_1900 = income_per_person[["country", "1900"]].\
        rename(columns={"1900": "GDP_1900"})
    life_expectancy_1900 = life_expectancy[["country", "1900"]].\
        rename(columns={"1900": "LifeExpectancy_1900"})

    merged_data = pd.merge(income_1900, life_expectancy_1900, on="country")

    plt.figure()
    plt.scatter(merged_data["GDP_1900"], merged_data["LifeExpectancy_1900"],
                color="blue", label="life expectancy vs GDP")
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")
    plt.xlim(300, 1000)
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
