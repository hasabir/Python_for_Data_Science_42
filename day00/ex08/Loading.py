from time import sleep
from tqdm import tqdm
# from Loading import ft_tqdm

def ft_tqdm(lst) -> None:
	import time

	total = len(lst)
	for i, elem in enumerate(lst, 1):
		yield elem
		progress = i * 100 // total
		text_value = f'{progress}%|[{"=" * (progress + 32)}>{" " * (100 - (progress))}]| {round(i * (progress / 100))}/{total}'
		print(text_value, end='\r', flush=True)


for elem in ft_tqdm(range(333)):# Here you can do whatever you want with the elements, for example:
	# print(elem)
	sleep(0.005)
print()


for elem in tqdm(range(333)):
	sleep(0.005)
print()






