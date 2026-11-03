::: {align="center"}
# 📊 DATA ANALYZER AND TRANSFORMER

### Python Functional Programming Project --- PR-4

**Analyze · Transform · Filter · Sort**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-PR--4-6C63FF?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Console%20Application-2E8B57?style=for-the-badge)
:::

------------------------------------------------------------------------

## 👨‍💻 Project Details

  Field                  Details
  ---------------------- ---------------------------------
  **Project Title**      Data Analyzer and Transformer
  **Practical Number**   PR-4 --- Functional Treat
  **Author**             **Prince Shah**
  **Guided By**          **Girish Gondaliya**
  **Language**           Python 3
  **Application Type**   Menu-driven Console Application
  **Data Structures**    1D and 2D Lists

## 📖 About the Project

The **Data Analyzer and Transformer** is a menu-driven Python
application designed to perform basic analysis and transformation
operations on numerical data.

The program accepts values in a one-dimensional (1D) list or a
two-dimensional (2D) nested list. It demonstrates Python functions and
programming techniques through seven main menu options, including data
input, statistical summaries, factorial calculation using recursion,
threshold filtering, sorting, and multiple-value returns.

## 🎯 Objectives

-   Practice Python built-in and user-defined functions.
-   Work with one-dimensional and two-dimensional lists.
-   Calculate basic statistics such as minimum, maximum, sum, and
    average.
-   Demonstrate recursion through factorial calculation.
-   Use lambda expressions with `map()` and `filter()`.
-   Understand `*args`, `**kwargs`, global variables, and docstrings.
-   Demonstrate list sorting with `sort()` and `sorted()`.

## ✨ Main Menu and Features

    Option Operation                    Concepts Demonstrated
  -------- ---------------------------- ------------------------------------
         1 Input Data                   1D and 2D lists
         2 Display Data Summary         `len()`, `min()`, `max()`, `sum()`
         3 Calculate Factorial          Recursion
         4 Filter Data by Threshold     Lambda, `map()`, `filter()`
         5 Sort Data                    `sort()`, `sorted()`
         6 Display Dataset Statistics   Returning multiple values
         7 Exit Program                 Menu control using a loop

## 🧰 Python Concepts Used

-   **Built-in functions:** `len()`, `sum()`, `min()`, and `max()`.
-   **User-defined functions:** Separate functions for input, analysis,
    filtering, sorting, and calculations.
-   **`*args`:** Accepts a variable number of positional arguments.
-   **`**kwargs`:** Accepts keyword arguments for displaying summary
    information.
-   **Docstrings (`__doc__`):** Describe the purpose of functions.
-   **Recursion:** A function calls itself to calculate a factorial.
-   **Lambda:** Creates a small anonymous function.
-   **`map()` and `filter()`:** Apply a transformation and select values
    that meet a condition.
-   **Global keyword:** Allows functions to access or update a global
    variable.
-   **Multiple return values:** Returns minimum, maximum, sum, and
    average from one function.
-   **List sorting:** Uses `sort()` and `sorted()` for ordering list
    data.

------------------------------------------------------------------------

# 🖥️ Sample Execution and Output

The following sample run uses this 1D dataset:

``` text
34 12 56 78 43 21 90
```

## Main Menu

``` text
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit

Please enter your choice:
```

## 1 --- Input Data

**Purpose:** Enter numerical values and store them in a 1D list.

``` text
Please enter your choice: 1

Enter data for a 1D array (separated by spaces):
34 12 56 78 43 21 90

Data has been stored successfully!
```

Stored dataset:

``` python
[34, 12, 56, 78, 43, 21, 90]
```

## 2 --- Display Data Summary

**Purpose:** Display the number of elements, minimum, maximum, sum, and
average using built-in functions.

``` text
Please enter your choice: 2

Data Summary:
- Total elements: 7
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71
```

## 3 --- Calculate Factorial (Recursion)

**Purpose:** Calculate the factorial of a non-negative integer using
recursion.

``` text
Please enter your choice: 3

Enter a number to calculate its factorial:
5

Factorial of 5 is: 120
```

Calculation:

``` text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

## 4 --- Filter Data by Threshold

**Purpose:** Select values greater than or equal to the threshold
entered by the user.

``` text
Please enter your choice: 4

Enter a threshold value to filter out data above this value:
50

Filtered Data (values >= 50):
56, 78, 90
```

## 5 --- Sort Data

**Purpose:** Arrange values in ascending or descending order.

``` text
Please enter your choice: 5

Choose sorting option:
1. Ascending
2. Descending

Enter your choice: 1

Sorted Data in Ascending Order:
12, 21, 34, 43, 56, 78, 90
```

Descending order example:

``` text
90, 78, 56, 43, 34, 21, 12
```

## 6 --- Display Dataset Statistics

**Purpose:** Return and display multiple statistics from a single
user-defined function.

``` text
Please enter your choice: 6

Dataset Statistics:
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71
```

## 7 --- Exit Program

**Purpose:** Exit the application from the main menu.

``` text
Please enter your choice: 7

Thank you for using the Data Analyzer
and Transformer Program. Goodbye!
```

------------------------------------------------------------------------

## 📂 Project Structure

``` text
functional-Treat/
│
├── Project4.py
└── README.md
```

## ▶️ How to Run

1.  Install Python 3 on your computer.
2.  Clone or download this repository.
3.  Open the project folder in VS Code or Python IDLE.
4.  Run the following command in the terminal:

``` bash
python data_analyzer.py
```

5.  Select an option from the main menu and follow the instructions.

## ⚙️ Requirements

-   Python 3.x
-   VS Code or Python IDLE
-   No external Python libraries are required.

## 👨‍🏫 Credits

**Developed By:** Prince Shah

**Guided By:** Girish Gondaliya

**Project:** PR-4 --- Functional Treat

------------------------------------------------------------------------

::: {align="center"}
### Thank You for Visiting!

**Data Analyzer and Transformer**\
*Made with Python 🐍*
:::
