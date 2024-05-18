# def ft_tqdm(lst) -> None:
#     total = len(lst)
#     for i, elem in enumerate(lst, 1):
#         yield elem
#         progress = i * 100 // total
#         text_value = f'{progress}%|'
#         text_value += f'[{"=" * (progress)}>{" " * (100 - (progress))}]'
#         text_value += f'| {round(i * (progress / 100))}/{len(lst)}'
#         print(text_value, end='\r', flush=True)


# Get terminal size without importing anything
def get_terminal_size():
    try:
        # Open a subprocess to execute the 'stty size' command and read the output
        # 'stty size' returns the terminal rows and columns
        with open('/dev/tty') as tty:
            rows, cols = map(int, tty.readline().strip().split())
        return cols, rows
    except Exception:
        return 80, 24  # Default terminal size if the actual size cannot be determined

columns, rows = get_terminal_size()
print(f"Terminal size: {columns} columns, {rows} rows")
