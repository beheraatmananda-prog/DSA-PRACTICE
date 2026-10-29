class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(m):
            for c in range(n):

                live_neighbors = 0

                # Count live neighbors
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1

                # Live cell
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2

                # Dead cell
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 3

        # Convert temporary values to final values
        for r in range(m):
            for c in range(n):

                if board[r][c] == 2:
                    board[r][c] = 0

                elif board[r][c] == 3:
                    board[r][c] = 1