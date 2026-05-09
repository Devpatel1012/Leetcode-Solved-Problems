class Solution(object):
    def rotateGrid(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        layers = min(rows, cols) // 2

        for layer in range(layers):

            elements = []

            # Top row
            for col in range(layer, cols - layer):
                elements.append(grid[layer][col])

            # Right column
            for row in range(layer + 1, rows - layer - 1):
                elements.append(grid[row][cols - layer - 1])

            # Bottom row
            for col in range(cols - layer - 1, layer - 1, -1):
                elements.append(grid[rows - layer - 1][col])

            # Left column
            for row in range(rows - layer - 2, layer, -1):
                elements.append(grid[row][layer])

            # Rotate layer
            rotation = k % len(elements)
            rotated = elements[rotation:] + elements[:rotation]

            idx = 0

            # Fill Top row
            for col in range(layer, cols - layer):
                grid[layer][col] = rotated[idx]
                idx += 1

            # Fill Right column
            for row in range(layer + 1, rows - layer - 1):
                grid[row][cols - layer - 1] = rotated[idx]
                idx += 1

            # Fill Bottom row
            for col in range(cols - layer - 1, layer - 1, -1):
                grid[rows - layer - 1][col] = rotated[idx]
                idx += 1

            # Fill Left column
            for row in range(rows - layer - 2, layer, -1):
                grid[row][layer] = rotated[idx]
                idx += 1

        return grid