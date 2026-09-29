class Solution:

    def hasValidPath(self, grid: list[list[str]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        length = m + n - 1

        if length % 2 == 1:
            return False

        memo = {}

        def dfs(i, j, balance):

            # Process current cell
            if grid[i][j] == '(':
                new_balance = balance + 1
            else:
                new_balance = balance - 1

            # Balance can never be negative
            if new_balance < 0:
                return False

            # Remaining cells after current cell
            remaining = (m - 1 - i) + (n - 1 - j)

            # We don't have enough ')' to close all '('
            if new_balance > remaining:
                return False

            # Reached bottom-right
            if i == m - 1 and j == n - 1:
                return new_balance == 0

            state = (i, j, new_balance)

            if state in memo:
                return memo[state]

            # Move DOWN
            if i + 1 < m:
                if dfs(i + 1, j, new_balance):
                    memo[state] = True
                    return True

            # Move RIGHT
            if j + 1 < n:
                if dfs(i, j + 1, new_balance):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0, 0)