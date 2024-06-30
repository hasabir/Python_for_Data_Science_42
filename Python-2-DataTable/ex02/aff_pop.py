# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import pandas

# from load_csv import load

# def get_info_plot(country: str, csv_file: pandas.DataFrame):
# 	dataFrame = load(csv_file)
# 	row = dataFrame[dataFrame.iloc[:, 0] == country]

# 	y = row.iloc[0].tolist()
# 	y.pop(0)
# 	x = list(dataFrame.columns.values)
# 	x.pop(0)
# 	return x, y




# def main():
# 	x, y = get_info_plot("France", "population_total.csv")
# 	x2, y2 = get_info_plot("Belgium", "population_total.csv")

# 	fig = plt.figure()
# 	ax = fig.add_subplot()
# 	plt.plot(x, y, color='red',label='France')
# 	plt.plot(x2, y2, color='g', label='Belgium')
# 	x_ticks = [year for i, year in enumerate(x) if i % 40 == 0]
# 	ax.set_xticks(x_ticks)
# 	print(y)

# 	print ('*' * 50)
# 	for i in range(len(y)):
# 		y[i] = y[i].replace("M","000000")
# 		y[i] = y[i].replace(".","")
# 	print(y)

# 	# print(f'y = {y[0]} | {int(y[0].replace("M","000000"))}')
# 	y_ticks = [population for i, population in enumerate(y) if i % 10000000 == 0 ]
# 	# ax.set_yticks(y_ticks)
	
	
# 	plt.xlabel('Year')
# 	plt.ylabel('Population')
	
# 	plt.legend()

# 	plt.title('Morocco Life expectancy Projections')
	
# 	plt.show()


# if __name__ == "__main__":
# 	main()

import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load

def get_info_plot(country: str, csv_file: str):
    dataFrame = load(csv_file)
    row = dataFrame[dataFrame.iloc[:, 0] == country]
    
    y = row.iloc[0].tolist()
    y.pop(0)
    x = list(dataFrame.columns.values)
    x.pop(0)
    return x, y

def convert_population(population_list):
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
    x, y = get_info_plot("France", "population_total.csv")
    x2, y2 = get_info_plot("Belgium", "population_total.csv")

    y = convert_population(y)
    y2 = convert_population(y2)

    fig, ax = plt.subplots()
    plt.plot(x, y, color='red', label='France')
    plt.plot(x2, y2, color='green', label='Belgium')

    ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Show a limited number of x ticks
    ax.set_yticks([20_000_000, 40_000_000, 60_000_000])  # Set specific y-axis ticks
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x/1e6)}M'))

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.title('Population Projections')
    plt.show()

if __name__ == "__main__":
    main()
