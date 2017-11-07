"""
Q1. Without using the infixToPostfix function, convert the following expression to postfix 10 + 3 * 5 / (16 - 4).
A. 10 + 3 * 5 / (16 - 4) <=> {10 + [(3 * 5) / (16 - 4)]} <=> {10 [(3 5) * (16 4)-   /]  +} = 10 3 5 * 16 4 - / +
(fully parenthesize and put the operators at the end of each parenthesis)

Q2. What is the result of evaluating the following: 17 10 + 3 * 9 / ==
A. 17 10 + 3 * 9 / ==  <=> [(17 + 10) * 3] / 9 == 3

Q3. Modify the infixToPostfix function so that it can convert the following expression: 5 * 3 ^ (4 - 2)

5 * 3 ^ (4 - 2) ==> {5 * [3 ^ (4 - 2)]} <=> {5 [3 (4 2 -) ^] *} = 5 3 4 2 - ^ *
"""