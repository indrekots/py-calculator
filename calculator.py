import re
from collections import deque

class Calculator:
    supported_operators = {
        "*": {"precedence": 3, "assoc": "left"},
        "/": {"precedence": 3, "assoc": "left"},
        "+": {"precedence": 2, "assoc": "left"},
        "-": {"precedence": 2, "assoc": "left"}
    }

    def calculate(self, input_string):
        output = deque([])
        operators = []
        elems = self.__find_exp_elems(input_string)
        self.__parse_infix_notation(elems, output, operators)
        return self.__eval_rpn(output)

    def __find_exp_elems(self, input_string):
        regexp = "\d+|[{}]".format("".join(self.supported_operators.keys()))
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
            if self.__is_operand(token):
                operands.append(token)
            else: self.__eval_operator(token, operands)

        if len(operands) == 1:
            return operands.pop()
        else: raise RuntimeError("Input has too many values")

    def __is_operand(self, token):
        return isinstance(token, float)

    def __eval_operator(self, token, operands):
        if token == "+": self.__add(operands)
        elif token == "-": self.__subtract(operands)
        elif token == "*": self.__multiply(operands)
        elif token == "/": self.__divide(operands)

    def __append_operator(self, operators, output, op1):
        while len(operators) > 0:
            op2 = operators[-1]
            if self.__should_pop_op_off_stack(op1, op2):
                output.append(operators.pop())
            else: break

        operators.append(op1)

    def __should_pop_op_off_stack(self, op1, op2):
        return (self.__is_left_associative(op1) and
                self.__op_precedence(op1) <= self.__op_precedence(op2)) or \
               (self.__is_right_associative(op1) and
                self.__op_precedence(op1) < self.__op_precedence(op2))

    def __is_left_associative(self, op):
        return self.supported_operators[op]["assoc"] == "left"

    def __is_right_associative(self, op):
        return self.supported_operators[op]["assoc"] == "right"

    def __op_precedence(self, op):
        return self.supported_operators[op]["precedence"]

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

    def __divide(self, operands):
        if len(operands) < 2:
            raise RuntimeError("Division requires 2 operands")
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(op1 / op2)
