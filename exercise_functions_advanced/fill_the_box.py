def fill_the_box(heigth, width, breadth, *args):
    volume = heigth * width * breadth
    content = 0
    cubes = 0
    for el in args:
        if el != 'Finish':
            cubes += int(el)

    for _ in range(len(args)):
        current_cube = args[_]
        if current_cube == 'Finish':
            break
        if content < volume:
            if current_cube <= volume - content:
                content += current_cube
            else:
                content += volume - content
                break

    if content < volume:
        return f"There is free space in the box. You could put {volume - content} more cubes."
    else:
        return f"No more free space! You have {cubes - volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
