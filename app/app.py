import pandas as pd
from util import calculate_coordinate_diff

# Import file data to dataframe
df = pd.read_csv('../data/input.txt', sep=' ')

current_coordinates = (0, 0, 0)

# calculate coordinate difference after row and add to current coordinates
for row in df.itertuples():
    coordinate_modifier = calculate_coordinate_diff(row.direction, row.distance, current_coordinates[2])
    current_coordinates = tuple(a + b for a, b in zip(current_coordinates, coordinate_modifier))

#display results
coordinates_multiplied = current_coordinates[0] * current_coordinates[1]
print(f'Your final horizontal distance is {current_coordinates[0]} from start, at a depth of {current_coordinates[1]}')
print(f'Your coordinates multiplied come out to: {coordinates_multiplied}')