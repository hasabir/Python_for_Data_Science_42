import pandas


def load(path: str) -> pandas.DataFrame:
    '''
    Load a csv file
    :param path: str: the path to the csv file
    :return: pandas.DataFrame: the dataFrame

    '''
    try:
        if path is None or path == '':
            raise ValueError('Path mast be a string')
        data = pandas.read_csv(path)
        print(f'Loading dataset of dimension {data.shape}')
        return data
    except Exception as err:
        print("Error:", err)
        return


def main():
    print(load('life_expectancy_years.csv'))


if __name__ == "__main__":
    main()
