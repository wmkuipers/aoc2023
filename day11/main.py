import sys

def read_grid_from_file(filename):
    """Reads the grid from a file and returns it as a list of lists."""
    with open(filename) as file:
        return [list(line.strip()) for line in file]

def find_empty_rows_and_columns(grid):
    """Finds and returns empty rows and columns in the grid."""
    empty_rows = [r for r in range(len(grid)) if all(cell != '#' for cell in grid[r])]
    empty_columns = [c for c in range(len(grid[0])) if all(grid[r][c] != '#' for r in range(len(grid)))]
    return empty_rows, empty_columns

def get_occupied_cells(grid):
    """Returns a list of coordinates for cells that are occupied (marked with '#')."""
    return [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#']

def calculate_total_distance(occupied_cells, empty_rows, empty_columns, part2):
    """Calculates the total distance based on occupied cells, empty rows/columns, and part flag."""
    expansion_factor = 10**6 - 1 if part2 else 1
    total_distance = 0

    for i, (r1, c1) in enumerate(occupied_cells):
        for r2, c2 in occupied_cells[i:]:
            distance = abs(r2 - r1) + abs(c2 - c1)

            # Adjust distance for empty rows and columns
            distance += sum(expansion_factor for er in empty_rows if min(r1, r2) <= er <= max(r1, r2))
            distance += sum(expansion_factor for ec in empty_columns if min(c1, c2) <= ec <= max(c1, c2))

            total_distance += distance

    return total_distance

def main():
    filename = sys.argv[1]
    grid = read_grid_from_file(filename)

    # Ensure all rows have the same number of columns
    assert all(len(row) == len(grid[0]) for row in grid), "Grid rows have inconsistent lengths"

    empty_rows, empty_columns = find_empty_rows_and_columns(grid)
    occupied_cells = get_occupied_cells(grid)

    for part2 in [False, True]:
        total_distance = calculate_total_distance(occupied_cells, empty_rows, empty_columns, part2)
        print(total_distance)

if __name__ == "__main__":
    main()
