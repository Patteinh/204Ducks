from src.utils import help

def check_args(ac, av):
    if ac == 2 and av[1] == "-h":
        help()
        exit(0)
    if ac != 2:
        raise Exception("ERROR: The number of arguments must be 2.")
    try:
        arg_value = float(av[1])
    except ValueError:
        raise Exception("ERROR: The provided argument must be a number.")
    if not (0 <= arg_value <= 2.5):
        raise Exception("ERROR: The provided argument must be between 0 and 2.5.")