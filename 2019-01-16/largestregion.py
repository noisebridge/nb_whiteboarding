from random import randint


def largest_region(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    largest = 0
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            largest = max(largest, flood_region(matrix[row][col], col, row, matrix, visited))
    
    return largest


def flood_region(tile, x, y, matrix, visited):
    size = 0

    if x >= 0 and y >= 0 and y < len(matrix) and \
       x < len(matrix[y]) and not visited[y][x] and matrix[y][x] == tile:
        visited[y][x] = True
        size += 1

        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            size += flood_region(tile, x + dx, y + dy, matrix, visited)

    return size


if __name__ == "__main__":
    matrix = [[randint(0, 2) for x in range(7)] for y in range(7)]
    
    for row in matrix:
        print(" ".join(map(str, row)))
    
    print(largest_region(matrix))
