## Problem 0: Create a GitHub Repository
This GitHub repository was created by Samantha Pohitakis, a current student in CS:3980:001. This repository holds the code and plot of the first homework assignment in CS:3980:001.


## Problem 1: Python Programming Basics
The echo.py file was created to simulate an echoing effect of user input. The code is shown in the image below.

<img width="500" alt="Screenshot 2024-01-31 at 4 41 54 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/3235b8f0-2aea-4ce8-aeb1-2fb05c76e805">

The echo function takes in the text to be echoed and the number of times it should be echoed. It prints the echoes and returns a "." when finished. When the program is run, it asks the user to yell something at a mountain and waits for user input. 

With the input "Helloooo", the code outputs the text below.

<img width="600" alt="Screenshot 2024-01-31 at 4 01 48 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/e7689c9c-c248-4801-a73f-ecad08506b35">

With the input "echo 123", the code outputs the text below.

<img width="600" alt="Screenshot 2024-01-31 at 4 03 21 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/847db042-16e2-4170-9b8d-e5c85dfca20a">


With the input "samantha pothtitakis", the code outputs the text below:

<img width="600" alt="Screenshot 2024-01-31 at 4 15 47 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/0011bfcf-a185-46d7-8314-9abee58f7555">


## Problem 2: Python Decorator Implementation
The fib.py file implements a function (fib) that uses recursion to calculate the Fibonacci sequence. A timer function was implemented to track the time it takes for the function to calculate each Fibonacci sequence number. The code for both functions is shown below.
<img width="500" alt="Screenshot 2024-01-31 at 4 30 09 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/00abb82f-b010-4753-91d2-3926a606e1f1">

The 'fib' function takes in an integer and returns the number at that index of the Fibonacci sequence. The timer function takes in a function and returns a wrapper function that will have the same name and docstring as the function it is wrapping. 
fib(100) is run when the user runs the program directly and the ending of the output is shown in the image below. 

<img width="500" alt="Screenshot 2024-01-31 at 4 36 58 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/798cde4c-51f5-4ef3-888b-691962e8f997">

The time it takes for each fib(x) function to run is printed because of the decorator timer function.

#### Graphing
The 'times' array stores the time it takes for each function call of 'fib'. This array is used to create a graph using matplotlib in the fibTimePlot.py file. 

<img width="500" alt="Screenshot 2024-01-31 at 4 50 13 PM" src="https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/839ab07e-071d-4304-a72c-b57a2ebfdb16">



This code plots the time it took for each function to run against its function call. The plot is shown below.

![FibonacciTimeGraph](https://github.com/samanthapoth/TopicsInCS1HW1/assets/90707077/bb8779c2-2cc3-484e-8840-7855cdfad75d)

As shown in the graph above, the 'fib' function calls with larger inputs take more time. Because the function calculates the sequence recursively, each function call with a higher input depends on the previous two function calls until 1 and 0. This is why the time increases as the input for the 'fib' function increases. The use of the @lru_cache decorator significantly reduces the computation time. lru_cache stores the results of the most recent 128 function calls. When the 'fib' function is called, it checks to see if the input it is trying to calculate with has been recently called and pulls the result from the cache instead of recomputing. 
