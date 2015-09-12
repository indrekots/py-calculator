import re
from collections import deque

class Calculator:
    def calculate(self, input_string):
        elems = re.findall('\d+|[+-]', input_string)
        output = deque([])
        operators = []
        for e in elems:
            if e.isdigit():
                output.append(float(e))
            else:
                self.__append_operator(operators, output, e)

        while len(operators) > 0:
            output.append(operators.pop())

        return self.__eval_rpn(output)

    def __eval_rpn(self, output):
        operands = []
        while len(output) > 0:
            token = output.popleft()
            if isinstance(token, float):
                operands.append(token)
            else:
                if token == "+": self.__add(operands)
                if token == "-": self.__subtract(operands)

        if len(operands) == 1:
            return operands.pop()
        else: raise RuntimeError("Input has too many values")

    def __append_operator(self, operators, output, elem):
        if len(operators) > 0:
            output.append(operators.pop())
        operators.append(elem)

    def __add(self, operands):
        if len(operands) < 2:
            raise RuntimeError("Addition requires 2 operands")
        else:
            result = operands.pop() + operands.pop()
            operands.append(result)

    def __subtract(self, operands):
        if len(operands) < 2:
            raise RuntimeError("Subtraction requires 2 operands")
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(op1 - op2)
