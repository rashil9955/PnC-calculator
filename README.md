# Permutation and Combination Calculator

A simple yet effective Python calculator for computing permutations and combinations, born out of real classroom needs in Discrete Mathematics.

## Origin Story

This calculator was created during a Discrete Mathematics class where the professor frequently asked students to solve permutation and combination problems. Instead of manually calculating these values repeatedly, I decided to code a solution right there in class. The initial version was later refined into this more structured implementation using functions.

## Features

- Calculate permutations (nPr)
- Calculate combinations (nCr)
- Interactive command-line interface
- Option to perform multiple calculations in one session
- Built-in factorial calculation

## How It Works

The calculator includes three main functions:
1. `calculate_factorial(input)`: Computes the factorial of a given number
2. `permutation(n, n_r)`: Calculates permutation using the formula n!/(n-r)!
3. `combination(n, r, n_r)`: Calculates combination using the formula n!/(r!(n-r)!)

## Usage

1. Run the program
2. Enter the value for 'n' (total number of items)
3. Enter the value for 'r' (number of items being chosen)
4. View the calculated permutation and combination results
5. Choose whether to perform another calculation (Y/y to continue)

Example:
```
----- PERMUTATION AND COMBINATION CALCULATOR -----

Enter n: 5
Enter r: 2

         Permutation -->  20.0
         Combination -->  10.0

More?: n
```

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
```

2. Navigate to the project directory:
```bash
cd permutation-combination-calculator
```

3. Run the script:
```bash
python calculator.py
```

## Contributing

Feel free to fork this repository and submit pull requests to put contributions to this project. You can also open issues for bugs or feature suggestions.

## License

This project is open source and available under the [MIT License](LICENSE).
