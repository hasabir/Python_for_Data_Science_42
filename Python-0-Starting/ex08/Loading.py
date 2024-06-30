def ft_tqdm(lst: range) -> None:  # type: ignore
    '''	Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.'''
    try:
        total = len(lst)
        for i, elem in enumerate(lst, 1):
            yield elem
            progress = i * 100 // total
            text_value = f'{progress}%|'
            text_value += f'[{"=" * (progress)}>{" " * (100 - (progress))}]'
            text_value += f'| {round(i * (progress / 100))}/{len(lst)}'
            print(text_value, end='\r', flush=True)
    except Exception as e:
        print('Error:', e)


def main():
    '''main function to test ft_tqdm'''
    from time import sleep
    from tqdm import tqdm
    try:
        for elem in ft_tqdm(range(333)):
            sleep(0.005)
        print()
        for elem in tqdm(range(333)):
            sleep(0.005)
        print()
    except Exception as e:
        print('Error:', e)


if __name__ == "__main__":
    main()
