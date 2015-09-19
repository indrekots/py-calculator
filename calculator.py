import re
from collections import deque

class Calculator:
    ops_avail = {
        "^": {"precedence": 4, "assoc": "right", "func": lambda x, y: x ** y},
        "*": {"precedence": 3, "assoc": "left", "func": lambda x, y: x * y},
        "/": {"precedence": 3, "assoc": "left", "func": lambda x, y: x / y},
        "+": {"precedence": 2, "assoc": "left", "func": lambda x, y: x + y},
        "-": {"precedence": 2, "assoc": "left", "func": lambda x, y: x - y}
    }

    def calculate(self, input_string):
        output = deque([])
        operators = []
        elems = self.__find_exp_elems(input_string)
        self.__parse_infix_notation(elems, output, operators)
        return self.__eval_rpn(output)

    def __find_exp_elems(self, input_string):
        elems = re.findall(self.__build_regexp(), input_string)
        if not elems:
            raise RuntimeError("No operands or operators provided")
        else: return elems

    def __build_regexp(self):
        base = "\d+|[{0}{1}]"
        return base.format("".join(self.ops_avail.keys()), "\(\)")

    def __parse_infix_notation(self, elements, output, operators):
        for e in elements:
            if e.isdigit():
                output.append(float(e))
            elif e == "(":
                operators.append(e)
            elif e == ")":
                self.__pop_operators_until_left_paren(operators, output)
            else:
                self.__append_operator(operators, output, e)

        while len(operators) > 0:
            if operators[-1] == "(":
                raise RuntimeError("Mismatching parenthesis")
            output.append(operators.pop())

    def __pop_operators_until_left_paren(self, operators, output):
        paren_found = False
        while len(operators) > 0:
            if operators[-1] == "(":
                paren_found = True
                operators.pop()
                break
            else:
                output.append(operators.pop())

        if paren_found == False:
            raise RuntimeError("Mismatching parenthesis")

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

    def __append_operator(self, operators, output, op1):
        while len(operators) > 0:
            op2 = operators[-1]
            if self.__should_pop_op_off_stack(op1, op2):
                output.append(operators.pop())
            else: break

        operators.append(op1)

    def __should_pop_op_off_stack(self, op1, op2):
        return op2 != "(" and \
               ((self.__is_left_associative(op1) and
                self.__op_precedence(op1) <= self.__op_precedence(op2)) or \
               (self.__is_right_associative(op1) and
                self.__op_precedence(op1) < self.__op_precedence(op2)))

    def __is_left_associative(self, op):
        return self.ops_avail[op]["assoc"] == "left"

    def __is_right_associative(self, op):
        return self.ops_avail[op]["assoc"] == "right"

    def __op_precedence(self, op):
        return self.ops_avail[op]["precedence"]

    def __eval_operator(self, token, operands):
        if len(operands) < 2:
            raise RuntimeError("Operator requires 2 operands")
        else:
            func = self.ops_avail[token]["func"]
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(func(op1, op2))
