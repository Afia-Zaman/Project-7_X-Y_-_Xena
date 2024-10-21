# AFIA ZAMAN
# create a function to draw X using symbol and size

def draw_x(symbol, size):
    bounds = size * 2 + 1
    x = ""
    for row in range(size + 1):
        for col in range(bounds):
            if row == col or col == bounds - row - 1:
                x += symbol
            else:
                x += " "
        x += "\n"
    for row in range(size + 1, bounds):
        for col in range(bounds):
            if row == col or col == bounds - row - 1:
                x += symbol
            else:
                x += " "
        x += "\n"
    return x

# Function to draw a person with a face
def draw_person_with_face(face, symbol, size):
    face_symbols = {"cute": "^.^", "meh":  ".-.", "wow": "@~@", "neutral": "*_*"}

    if face in face_symbols:
        face_symbol = face_symbols[face]
        x = draw_x(symbol, size)
        x_lines = x.splitlines()
        face_lines = face_symbol.splitlines()

        for x in range(len(face_lines)):
            spaces = " " * ((size * 2 + 1 - len(face_lines[x])) // 2)
            print(spaces + face_lines[x] + spaces)

        for x_line in x_lines:
            print(x_line)

# Function to draw Y using symbol and size
def draw_y(symbol, size):
    bounds = size * 2 + 1
    y = ""
    for row in range(size + 1):
        for col in range(bounds):
            if row == col or col == bounds - row - 1:
                y += symbol
            else:
                y += " "
        y += "\n"
    for row in range(size):
        y += " " * size + symbol + "\n"
    return y

# Main function with extension
def main():

# Take input for size, symbol, drawing_type
    size = int(input("Enter size : "))
    if 1 <= size <= 10:
        symbol = input("Enter symbol: ")
        drawing_type = input("Will you draw a letter or a person? ")

        if drawing_type == "letter":
            letter = input("Enter x or y: ")
            if letter == "x":
                x = draw_x(symbol, size)
                print()
                print(x)

            elif letter == "y":
                y = draw_y(symbol, size)
                print()
                print(y)

        elif drawing_type == "person":
            emotion = input("Enter your emotion: ")
            print()
            draw_person_with_face(emotion, symbol, size)

    else:
        print("Invalid, enter a valid size.")
main()
