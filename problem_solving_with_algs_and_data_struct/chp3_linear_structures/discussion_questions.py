"""
Discussion Questions
--------------------
1. Convert the following values to binary using “divide by 2.” Show the stack of remainders.

- Convert integer 17_(10) into a binary number
==> 101001_(2) interpreted as: 1x2^0 + 0x2^1 + 0x2^2 + 1x2^3 + 0x2^4 + 1x2^5
17 // 2 = 8 rem = 1; 8 // 2 = 9 rem = 0; 9 // 2 = 4 rem = 1; 4 // 2 = 2 rem = 0; 2 // 2 = 1 rem = 0; 1 // 2 = 0 rem = 1

- Converting integer 45_(10) into a binary number
==> 101101_(2) interpreted as: 1x2^0 + 0x2^1 + 1x2^2 + 1x2^3 + 0x2^4 + 1x2^5
45 // 2 = 22 rem = 1; 22 // 2 = 11 rem = 0; 11 // 2 = 5 rem = 1; 5 // 2 = 2 rem = 1; 2 // 2 = 1 r = 0; 1 // 2 = 0 r = 1

- Converting decimal number 96_(10) into a binary number
==> 0000011_(2) interpreted as: 1x2^0 + 1x2^1 + 0x2^2 + 0x2^2 + 0x2^3 + 0x2^4 + 0x2^5
96 // 2 = 48 rem = 0; 48 // 2 = 24 rem = 0; 24 // 2 = 12 rem = 0; 12 // 2 = 6 rem = 0; 6 // 2 = 3 rem = 0;
3 // 2 = 1 rem = 1; 1 // 2 = 0 rem = 1


2. Convert the following infix expressions to prefix (use full parentheses):
(Prefix notation: All operators precede the two operands that they work on).

(A+B)*(C+D)*(E+F) ==> [(A+B)*(C+D)*(E+F)] ==> * * + A B + C D + E F

A+((B+C)*(D+E)) ==> {A+[(B+C)*(D+E)]} ==> + A * + B C + D E

A*B*C*D+E+F ==> {[(A*B*C*D)+E]+F} ==> + + * * * A B C D E F

3. Convert the above infix expressions to postfix (use full parentheses).
(III. Postfix notation: All operators come after the corresponding operands).

(A+B)*(C+D)*(E+F) ==> [(A+B)*(C+D)*(E+F)] ==> A B + C D + * E F + *

A+((B+C)*(D+E)) ==> {A+[(B+C)*(D+E)]} ==> A B C + D E + * +

A*B*C*D+E+F ==> {[(A*B*C*D)+E]+F} ==> A B * C * D * E + F +

4. Convert the above infix expressions to postfix using the direct conversion algorithm.
Show the stack as the conversion takes place.

5. Evaluate the following postfix expressions. Show the stack as each operand and operator is processed.
2 3 * 4 +
1 2 + 3 + 4 + 5 +
1 2 3 4 5 * + * +

6. The alternative implementation of the Queue ADT is to use a list such that the rear of the queue is at the end of
the list. What would this mean for Big-O performance?

7. What is the result of carrying out both steps of the linked list add method in reverse order?
What kind of reference results? What types of problems may result?

8. Explain how the linked list remove method works when the item to be removed is in the last node.

9. Explain how the remove method works when the item is in the only node in the linked list.

"""


"""Question 4. General Infix-to-Postfix Conversion:"""


class StackTopAtEnd:
    def __init__(self):
        self.items = []

    # tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    def is_empty(self):
        return self.items == []

    # returns the number of items on the stack. It needs no parameters and returns an integer.
    def size(self):
        return len(self.items)

    # adds a new item to the top of the stack. It needs the item and returns nothing.
    def push(self, item):
        self.items.append(item)

    # removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    def pop(self):
        return self.items.pop()

    # returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    def peek(self):
        return self.items[len(self.items) - 1]


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    operators_stack = StackTopAtEnd()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            operators_stack.push(token)
        elif token == ')':
            top_token = operators_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = operators_stack.pop()
        else:
            while (not operators_stack.is_empty()) and (prec[operators_stack.peek()] >= prec[token]):
                  postfix_list.append(operators_stack.pop())
            operators_stack.push(token)

    while not operators_stack.is_empty():
        postfix_list.append(operators_stack.pop())
    return " ".join(postfix_list)


"""Question 5. The evaluation of postfix expressions"""


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
    print(infix_to_postfix("( A + B ) * ( C + D ) * ( E + F )"))
    print(infix_to_postfix("A + ( ( B + C ) * ( D + E ) )"))
    print(infix_to_postfix("A * B * C * D + E + F"))

    print(postfix_eval("2 3 * 4 +"))
    print(postfix_eval("1 2 + 3 + 4 + 5 +"))
    print(postfix_eval("1 2 3 4 5 * + * +"))

main()