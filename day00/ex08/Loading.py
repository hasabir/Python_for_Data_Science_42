def ft_tqdm(lst) -> None:
    total = len(lst)
    for i, elem in enumerate(lst, 1):
        yield elem
        progress = i * 100 // total
        text_value = f'{progress}%|'
        text_value += f'[{"=" * (progress)}>{" " * (100 - (progress))}]'
        text_value += f'| {round(i * (progress / 100))}/{len(lst)}'
        print(text_value, end='\r', flush=True)


# Get terminal size without importing anything
