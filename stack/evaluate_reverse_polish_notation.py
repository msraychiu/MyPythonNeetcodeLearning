def is_digit(s):
    try:
        complex(s)
        return True
    except ValueError:
        return False


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if is_digit(t):
                s.append(t)
            else:
                first_number = s.pop()
                second_number = s.pop()
                s.append(int(eval(str(second_number) + t + str(first_number))))
        return s.pop()
