Direction = 0 # 0 is North, 1 = East, 2 = South, 3 = West, and divide (with remainder) by 4 after each direction change, remainder is the new direction
current_pos = (0, 0)

# Get input for directions then remove commas and split into a list based on spaces
inp = input("What is the input? ")
commaless = inp.replace(",", "")
streets = commaless.split()

# Loop through the list and update direction and position for each value
for i in streets:
    # Instead of calling for a value multiple times per i, call once here
    x = int(i[1:])

    # If we turn 90 degrees right, this function goes
    if i[0] == 'R':
        Direction += 1
        # Brute force all 4 positions
        if Direction == 1:
            current_pos = tuple(map(lambda i, j: i + j, current_pos, (x, 0)))
        if Direction == 2:
            current_pos = tuple(map(lambda i, j: i - j, current_pos, (0, x)))
        if Direction == 3:
            current_pos = tuple(map(lambda i, j: i - j, current_pos, (x, 0)))
        if Direction == 4:
            Direction = 0 # To keep things simple, only resets direction upon an extreme
            current_pos = tuple(map(lambda i, j: i + j, current_pos, (0, x)))

    # If we turn 90 degrees left, this function goes
    if i[0] == 'L':
        Direction += -1
        # Brute force all 4 positions
        if Direction == -1:
            Direction = 3 # To keep things simple, only resets direction upon an extreme
            current_pos = tuple(map(lambda i, j: i - j, current_pos, (x, 0)))
        if Direction == 0:
            current_pos = tuple(map(lambda i, j: i + j, current_pos, (0, x)))
        if Direction == 1:
            current_pos = tuple(map(lambda i, j: i + j, current_pos, (x, 0)))
        if Direction == 2:
            current_pos = tuple(map(lambda i, j: i - j, current_pos, (0, x)))

(x, y) = current_pos
print(x + y) #Print out distance away 
