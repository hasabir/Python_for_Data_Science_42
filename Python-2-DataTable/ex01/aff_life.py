from load_csv import load
import matplotlib.pyplot as plt


def main():
    ''' the main function of the script aff_life.py '''
    dataFrame = load("life_expectancy_years.csv")
    row = dataFrame[dataFrame.iloc[:, 0] == "Morocco"]

    y = row.iloc[0].tolist()
    y.pop(0)
    x = list(dataFrame.columns.values)
    x.pop(0)

    fig = plt.figure()
    ax = fig.add_subplot()
    plt.plot(x, y)

    x_ticks = [year for i, year in enumerate(x) if i % 40 == 0]
    ax.set_xticks(x_ticks)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Morocco Life expectancy Projections')
    plt.show()


if __name__ == "__main__":
    main()
