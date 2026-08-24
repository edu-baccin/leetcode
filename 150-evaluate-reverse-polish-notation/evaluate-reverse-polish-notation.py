class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = int()
        b = int()
        result = int()
        storage = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                storage.append(int(token))
            elif len(storage) > 1:
                b = int(storage.pop())
                a = int(storage.pop())
                if token == "+":
                    storage.append(result + (a + b))
                elif token == "-":
                    storage.append(result + (a - b))
                elif token == "*":
                    storage.append(result + (a * b))
                elif token == "/":
                    storage.append(result + int(a / b))
        return storage[0]
            