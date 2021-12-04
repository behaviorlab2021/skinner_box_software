def distance_from_center (point_x, point_y, center_x, center_y, aspect_ratio):

    return ((point_x - center_x) * aspect_ratio **2 + (point_y - center_y)**2 ) ** 0.5

print(type(distance_from_center(1,1,1.3,1.6,1)))

