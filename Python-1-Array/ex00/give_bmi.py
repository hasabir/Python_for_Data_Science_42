import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    '''function give_bmi, take 2 lists of integers\
         or floats in input and returns a list\
         of BMI values'''
    np_height = np.array(height)
    np_weight = np.array(weight)
    bmi = np_weight / (np_height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''unction, apply_limit, accepts a list of\
         integers or floats and an integer representing\
         a limit as parameters. It returns a list of booleans\
         (True if above the limit).'''
    stock: list[bool] = []
    try:
        for x in bmi:
            if not isinstance(x, (int, float)):
                raise ValueError(f"Invalid type {type(x)} for BMI value;\
                                  expected int or float.")
            stock.append(False if limit > x else True)
    except Exception as err:
        print('Error: ', err)
        return
    return stock


def main():
    '''main function to test give_bmi'''
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
