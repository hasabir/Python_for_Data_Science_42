from time import sleep
from tqdm import tqdm
# from Loading import ft_tqdm

def ft_tqdm(lst: range) -> None:
	# print('100%|')
	print('=', end='')
	# for i in range()
	# return (iter(lst))


for elem in ft_tqdm(range(333)):
	sleep(0.005)
print()
for elem in tqdm(range(333)):
	sleep(0.005)
print()

