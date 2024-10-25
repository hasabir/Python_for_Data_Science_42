import matplotlib.pyplot as plt
from load_csv import load


def get_info_plot(country: str, csv_file: str):
    '''
    Get the data to plot
    :param country: str: the country to plot
    :param csv_file: str: the csv file to load
    :return: tuple: x, y
    '''
    dataFrame = load(csv_file)

    row = dataFrame[dataFrame.iloc[:, 0] == country]
    x = list(dataFrame.columns.values)
    x = [i for i in x if i.isdigit() and int(i) <= 2050]
    y = row.iloc[0].tolist()[1:len(x) + 1]

    return x, y


def convert_population(population_list):
    '''
    Convert the population list to int
    :param population_list: list: the population list
    :return: list: the converted population list
    '''
    converted_population = []
    for value in population_list:
        if 'M' in value:
            value = value.replace('M', '')
            if '.' in value:
                value = int(float(value) * 1_000_000)
            else:
                value = int(value) * 1_000_000
        converted_population.append(value)
    return converted_population


def main():
    '''
    the main function of the script aff_pop.py
    '''
    x, y = get_info_plot("France", "population_total.csv")
    x2, y2 = get_info_plot("Morocco", "population_total.csv")

    y = convert_population(y)
    y2 = convert_population(y2)

    fig, ax = plt.subplots()
    plt.plot(x, y, color='blue', label='France')
    plt.plot(x2, y2, color='green', label='Morocco')

    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.set_yticks([20_000_000, 40_000_000, 60_000_000])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(
        lambda x, _: f'{int(x/1e6)}M'))

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    plt.title('Population Projections')
    plt.show()


if __name__ == "__main__":
    main()
