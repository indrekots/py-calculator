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
                if len(operators) > 0:
                    output.append(operators.pop())
                operators.append(e)

        while len(operators) > 0:
            output.append(operators.pop())

        return self.parseRPN(output.popleft(), output.popleft(), output.popleft(), output)

    def parseRPN(self, op1, op2, op, rest):
        if op == "+": result = op1 + op2
        if op == "-": result = op1 - op2
        if len(rest) > 0:
            return self.parseRPN(result, rest.popleft(), rest.popleft(), rest)
        else:
            return result
