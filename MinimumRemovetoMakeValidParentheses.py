class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            # For each characters
            for c in string:
                # If it has open parenthesis the total should be += 1
                if c == open_symbol:
                    balance += 1
                # If it reaches the closing parenthesis but the balance is zero, it should be deleteted
                if c == close_symbol:
                    if balance == 0:
                        continue
                    # Else Subtract total by -1
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        # Send the normal order
        s = delete_invalid_closing(s, "(", ")")
        #Send the reversed order
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]