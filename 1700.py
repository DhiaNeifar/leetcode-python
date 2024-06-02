def countStudents(students, sandwiches):
    squares = sum(students)
    circulars = len(students) - squares
    for food in sandwiches:
        if food and squares:
            squares -= 1
        elif not food and circulars:
            circulars -= 1
        else:
            return squares + circulars
    return 0


if __name__ == '__main__':
    students_ = [1, 1, 1, 0, 0, 1]
    sandwiches_ = [1, 0, 0, 0, 1, 1]
    print(countStudents(students_, sandwiches_))
