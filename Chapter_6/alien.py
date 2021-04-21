alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")

#Move the alient to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alient.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

alien_1 = {'color': 'green', 'points': 5}
print(alien_1)

del alien_1['points']
print(alien_1)
