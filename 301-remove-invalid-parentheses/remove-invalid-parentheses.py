class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def backtrack(index, left, right, path):

            if left == 0 and right == 0:
                remaining = s[index:]

                candidate = path + remaining

                if is_valid(candidate):
                    result.add(candidate)

                return

            if index == len(s):
                return

            ch = s[index]

            if ch == '(' and left > 0:
                backtrack(
                    index + 1,
                    left - 1,
                    right,
                    path
                )

            if ch == ')' and right > 0:
                backtrack(
                    index + 1,
                    left,
                    right - 1,
                    path
                )

            backtrack(
                index + 1,
                left,
                right,
                path + ch
            )

        backtrack(0, left_remove, right_remove, "")

        return list(result)