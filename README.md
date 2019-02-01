# EulerProblems

Some solutions to problems from Project Euler (56 and 98) using Python.

## Overview: 

The attached Python files solve problem [#56](https://projecteuler.net/problem=56) and [#98](https://projecteuler.net/problem=98) from [Project Euler](https://projecteuler.net/archives). The accompanying text file is necessary for #98.

## Explanation:

Here is a step-by-step explanation of what happens in each python file:

### Problem #56
1) Import necessary packages, start a timer, and pass initial parameter to wrapper function
2) The wrapper function loops through all possible bases ("a" in "a^b") and calls into geometricSum 
3) geometricSum is a fast way of computing a^1,a^2,...a^b
4) For each possible exponent of the base, geometricSum calls digitSum which simply adds up the digits for that number (e.g. 1234 -> 1+2+3+4 = 10)
5) Max Digital Sum is returned and printed with the time (should finish in ~.15s, under Project Euler's suggested goal of 1s)

### Problem #98
1) Import necessary packages, start a timer, and pass file_path to handler function
2) Find all anagrams in word file, and store them in a dictionary
where the key is the sorted version of the word (thus all anagrams will have that same key)
3) For each entry in the dictionary where there are at least two anagrams, find the largest number
that is a perfect square, and also perfectly maps to those anagrams
4) Return the largest number out of all those entries, print it, stop the timer and print the total time 
(should finish in ~.13s, under Project Euler's suggested goal of 1s)


## Instructions for Running: 

(#98 only)

1) Either save the attached "words.txt" file in the same location as Euler98.py

OR

2) You will need to navigate to [this](https://projecteuler.net/problem=98) link and right click to save the "words.txt" file. Save this
where you saved the Python file, so that when you run in your IDE the .py file can find the .txt file
locally. 

*Disclaimer: I could have used the Python library "urllib" to simply retrieve the text file from the web page, but 
Project Euler seems to modify their site often and thus the static link could easily break.*
