# PiPyCalc

A Python-based calculator for determining a high number of decimal places of the mathematical constant Pi ($\pi$) using the Gauss-Legendre algorithm. This project also includes a feature to compare the calculated digits against a reference file for verification.

## Author

* **Droggler**
    * GitHub: `https://github.com/Droggler`

## License

This project is licensed under the terms of the MIT license

## Features

* Calculates Pi to a user-specified number of decimal places.
* Implements the Gauss-Legendre algorithm.
* Utilizes Python's `decimal` module for arbitrary-precision arithmetic.
* Includes a function to compare computed Pi digits with a reference file (e.g., for 1,000,000 digits).
* Precision for calculations is configurable.

## Tech Stack / Requirements

* Python 3.x
* `decimal` module (Python standard library)
* `math` module (Python standard library)

## Setup & Usage

1.  **Prerequisites:**
    * Ensure Python 3 is installed on your system.

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Droggler/PiPyCalc.git
    cd PiPyCalc
    ```

3.  **Running the Calculator:**
    * The main script is `main.py`.
    * To run the script and calculate Pi:
        ```bash
        python main.py
        ```

4.  **Digit Comparison:**
    * The script will automatically compare its output for the first 1,000,000 decimal places against the reference file `pi.txt`.