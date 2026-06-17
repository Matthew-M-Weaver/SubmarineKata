VERTICAL_DIRECTIONS = {
    "up": -1,
    "down": 1
}

def calculate_coordinate_diff(direction, distance):
    if direction in VERTICAL_DIRECTIONS.keys():
        return (0, VERTICAL_DIRECTIONS[direction] * distance)
    else:
        return (distance, 0)