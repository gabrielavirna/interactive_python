"""
 Infix, Prefix and Postfix Expressions
 ======================================

 Expression formats:

I. Infix notation:  The operator is in between the two operands that it is working on.
------------------

E.g. B * C
The variable B is being multiplied by the variable C (operator * appears between them in the arithmetic expression).

E.g. A + B * C
-> Ambiguity: The operators + and * still appear between the operands, but which operands do they work on?
The precedence order for arithmetic operators places multiplication and division above addition and subtraction.
Only the presence of parentheses can change the order. (higher to lower, left-to-right ordering or associativity).

-> Using operator precedence: B and C are multiplied first, and A is then added to that result.
(A + B) * C would force the addition of A and B to be done first before the multiplication.
In expression A + B + C, by precedence (via associativity), the leftmost + would be done first.

-> Fully parenthesized expression
=> no confusion regarding the order of the operations (one pair of parentheses for each operator)
The parentheses dictate the order of operations => no ambiguity; no need to remember any precedence rules.

E.g. A + B * C + D can be rewritten as ((A + (B * C)) + D)
To show that the multiplication happens first, followed by the leftmost addition.

E.g. A + B + C + D can be written as (((A + B) + C) + D) since the addition operations associate from left to right.


II. Prefix notation: All operators precede the two operands that they work on.
--------------------


III. Postfix notation: All operators come after the corresponding operands.
----------------------

Infix Expression	Prefix Expression	Postfix Expression
A + B	                + A B	                A B +
A + B * C	            + A * B C	            A B C * +

(A + B) * C	            * + A B C	            A B + C *

A + B * C + D	        + + A * B C D	        A B C * + D +
(A + B) * (C + D)	    * + A B + C D	        A B + C D + *
A * B + C * D	        + * A B * C D	        A B * C D * +
A + B + C + D	        + + + A B C D	        A B + C + D +


Conversion of Infix Expressions to Prefix and Postfix
=======================================================

I. The first technique:
----------------------
Fully parenthesize the expression using the order of operations.
Then move the enclosed operator to the position of either the left (prefix) or the right parenthesis (postfix) .

E.g. A + B * C can be written as (A + (B * C)) to show explicitly that multiplication has precedence over the addition.
Note that each parenthesis pair also denotes the beginning & the end of an operand pair with the operator in the middle.

Prefix notation: (A + (B * C)) => + A * B C
Postfix notation: (A + (B * C)) => A B C * +

E.g. (((A + B) * C) - ((D - E) * (F + G)))
Prefix: - * + A B C * - D E + F G
Postfix: A B + C * D E - F G + * -

II. General Infix-to-Postfix Conversion:
----------------------------------------
Develop an algorithm to convert any infix expression to a postfix expression.
Note: Only the operators change position. The order of the operators in the original expression is reversed in postfix.

Process the expression: Save the operators somewhere. The order of them may need to be reversed due to their precedence.
Reversal of order => use a stack to keep the operators until they are needed.
The top of the stack will always be the most recently saved operator.
When reading a new operator, check how that one compares in precedence with the operators, if any, already on stack.

Assume
The infix expression: a string of tokens delimited by spaces.
The operator tokens: *, /, +, and -, along with the left and right parentheses, ( and ).
The operand tokens: the single-character identifiers A, B, C, and so on.
The postifx order: a string of tokens.

Steps:
------
Create an empty stack called operators_stack for keeping operators. Create an empty list for output.
Convert the input infix string to a list by using the string method split.
Scan the token list from left to right.
If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the operators_stack.
If the token is a right parenthesis, pop the operators_stack until the corresponding left parenthesis is removed.
Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the operators_stack. However, first remove any operators already
on the operators_stack that have higher or equal precedence and append them to the output list.
When the input expression has been completely processed, check the operators_stack.
Any operators still on the stack can be removed and appended to the end of the output list.

Use a dictionary called precedence to hold the precedence values for the operators.
This dictionary will map each  operator to an integer that can be compared against the precedence levels of other
operators (arbitrarily used the integers 3, 2, and 1). The left parenthesis will receive the lowest value possible.
This way any operator that is compared against it will have higher precedence and will be placed on top of it.


* Postfix Evaluation
====================
E.g. processing the postfix expression: 4 5 6 * +
As you scan the postfix expression, it is the operands that must wait, not the operators (conversion algorithm above).
Whenever an operator is seen on the input, the two most recent operands will be used in the evaluation.
As you scan the expression from left to right, you first encounter the operands 4 and 5. At this point, you are still
unsure what to do with them until you see the next symbol. Placing each on the stack ensures that they are available
if an operator comes next. The next symbol is another operand. So, as before, push it and check the next symbol.
Now we see an operator, * =>  the two most recent operands need to be used in a multiplication operation.
By popping the stack twice, we can get the proper operands and then perform the multiplication (the result: 30).
Place this result back on the stack so that it can be used as an operand for the later operators in the expression.
When the final operator is processed => only one value left on stack. Pop & return it as the result of the expression.

Assume:

The postfix expression: a string of tokens delimited by spaces.
The operators: *, /, +, and - .
The operands: single-digit integer values.
The output will be an integer result.

Steps:
------
Create an empty stack called operands_stack.
Convert the string to a list by using the string method split.
Scan the token list from left to right.
If the token is an operand, convert it from a string to an integer and push the value onto the operands_stack.
If the token is an operator, *, /, +, or -, it will need 2 operands. Pop the operands_stack twice. First pop is the 2nd
operand & second pop is the 1st operand. Perform the arithmetic operation. Push the result back on the operands_stack.
When the input expression has been completely processed, result is on stack. Pop the operands_stack & return the value.

A helper function doMath is defined & takes 2 operands and an operator & then performs the proper arithmetic operation.

"""

from projects.interactive_python.problem_solving_with_alg_and_data_struct import StackTopAtEnd


# General Infix-to-Postfix Conversion:
def infix_to_postfix(infix_expr):

    precedence = {}
    precedence["^"] = 4
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    operators_stack = StackTopAtEnd()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            operators_stack.push(token)
        elif token == ")":
            top_stack = operators_stack.pop()
            while token is not "(":
                postfix_list.append(top_stack)
        else:
            while not operators_stack.is_empty() and precedence[operators_stack.peek()] >= precedence[token]:
                postfix_list.append(operators_stack.pop())
            operators_stack.push(token)

    while not operators_stack.is_empty():
        postfix_list.append(operators_stack.pop())
    return " ".join(postfix_list)


# The evaluation of postfix expressions
def postfix_eval(postfix_expression):
    operands_stack = StackTopAtEnd()
    token_list = postfix_expression.split()

    for token in token_list:
        if token in "0123456789":
            operands_stack.push(int(token))
        else:
            operand2 = operands_stack.pop()
            operand1 = operands_stack.pop()
            result = do_math(token, operand1, operand2)
            operands_stack.push(result)
    return operands_stack.pop()


def do_math(operator, operand1, operand2):
    if operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2


def main():

    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(postfix_eval('7 8 + 3 2 + /'))
    print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))


# main()
# class Test(unittest.TestCase):
#     def test_infix_to_postfix(self):
#         self.assertEqual(infix_to_postfix("( A + B ) * ( C + D )"), "A B + C D + *")
#
#     def test_infix_to_postfix2(self):
#         self.assertEqual(infix_to_postfix("( A + B ) * C"), "A B C * +")
#
#     def test_postfix_eval(self):
#         self.assertEqual(postfix_eval('7 8 + 3 2 + /'), 3)
#
# if __name__ == '__main__':
#     unittest.main()


