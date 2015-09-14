import re
from collections import deque

class Calculator:
    supported_operators = "*+-"

    def calculate(self, input_string):
        output = deque([])
        operators = []
        elems = self.__find_expression_elements(input_string)
        self.__parse_infix_notation(elems, output, operators)
        return self.__eval_rpn(output)

    def __find_expression_elements(self, input_string):
        regexp = "\d+|[{}]".format(self.supported_operators)
        elems = re.findall(regexp, input_string)
        if not elems:
            raise RuntimeError("No operands or operators provided")
        else: return elems

    def __parse_infix_notation(self, elements, output, operators):
        for e in elements:
            if e.isdigit():
                output.append(float(e))
            else:
                self.__append_operator(operators, output, e)

        while len(operators) > 0:
            output.append(operators.pop())

    def __eval_rpn(self, output):
        operands = []
        while len(output) > 0:
            token = output.popleft()
            if isinstance(token, float):
                operands.append(token)
            else:
                if token == "+": self.__add(operands)
                if token == "-": self.__subtract(operands)
                if token == "*": self.__multiply(operands)

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

    def __multiply(self, operands):
        if len(operands) < 2:
            raise RuntimeError("Multiplication requires 2 operands")
        else:
            result = operands.pop() * operands.pop()
            operands.append(result)
