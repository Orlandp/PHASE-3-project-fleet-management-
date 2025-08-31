from tabulate import tabulate
def print_table(rows, headers):
    print(tabulate(rows, headers=headers, tablefmt="github"))
def parse_float(x):
    return float(x)
def parse_int(x):
    return int(x)
