class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        while len(tokens)>0:
            token = tokens.pop(0)
            if token not in ["+", "*", "-", "/"]:
                numberStack.append(int(token))
            else:
                ar2 = int(numberStack.pop())
                ar1 = int(numberStack.pop())
                if token == "+":
                    #print("ADD: ", ar1, ar2)
                    numberStack.append(ar1+ar2)
                if token == "-":
                    #print("SUB: ", ar1, ar2)
                    numberStack.append(ar1-ar2)
                if token == "*":
                    #print("MUL: ", ar1, ar2)
                    numberStack.append(ar1*ar2)
                if token == "/":
                    #print("DIV: ", ar1, ar2)
                    numberStack.append(int(ar1/ar2))

            if len(tokens) == 0:
                break

        return numberStack.pop()