def ft_tqdm(lst) -> None:
    total = len(lst)
    for i, elem in enumerate(lst, 1):
        yield elem
        progress = i * 100 // total
        text_value = f'{progress}%|'
        text_value += f'[{"=" * (progress)}>{" " * (100 - (progress))}]'
        text_value += f'| {round(i * (progress / 100))}/{len(lst)}'
        print(text_value, end='\r', flush=True)


def main():
    from time import sleep
    from tqdm import tqdm

    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
