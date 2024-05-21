import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	
	np_height = np.array(height)
	np_weight = np.array(weight)
	bmi = np_weight/ (np_height * np_height)
	return bmi.tolist()



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	
	stock: list[bool] = []
	try:
		for x in bmi:
			if not isinstance(x, (int, float)):
				raise ValueError(f"Invalid type {type(x)} for BMI value; expected int or float.")
			result = lambda i: False if limit > x else True
			stock.append(result(x))
	except Exception as err:
		print('Error: ',err)
		return
	return stock

def main():
	...

if __name__ == "__main__":
	main()


