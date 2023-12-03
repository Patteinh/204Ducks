# 204Ducks 🦆

Welcome to **204ducks**.

This project involves analyzing the behavior of ducks using probability density functions, focusing on the time it takes for disturbed ducks to return to a pond.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** When necessary, via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 204ducks

## Project Overview 🔎

The goal of 204ducks is to create a program that computes various statistics related to the behavior of ducks, based on a given probability density function. The project involves calculating average return time, standard deviation, and specific time intervals for duck returns.

### Key Features

- **Probability Density Function:** Implement the given function to model duck behavior.
- **Statistical Calculations:** Compute the average return time, standard deviation, and specific percentile return times.
- **Command-Line Interface:** Provide a user-friendly interface for input and result display.

### Usage

```
∼> ./204ducks -h
USAGE
    ./204ducks a
DESCRIPTION
    a   constant
```

### Exemples

```
∼> ./204ducks 1.6
Average return time: 1m 21s
Standard deviation: 1.074
Time after which 50% of the ducks are back: 1m 04s
Time after which 99% of the ducks are back: 5m 04s
Percentage of ducks back after 1 minute: 46.9%
Percentage of ducks back after 2 minutes: 79.1

∼> ./204ducks 0.2
Average return time: 0m 50s
Standard deviation: 0.676
Time after which 50% of the ducks are back: 0m 39s
Time after which 99% of the ducks are back: 3m 16s
Percentage of ducks back after 1 minute: 71.3%
Percentage of ducks back after 2 minutes: 94.2%
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `./204ducks a`.
4. For detailed guidelines, refer to `204ducks.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
