import turtle

def plotIt(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

def read_xpm_file(filename):
    try:
        with open(filename, 'r') as file:
            cols, rows, num_colors = map(int, file.readline().strip().split())
            color_map = {}
            for _ in range(num_colors):
                parts = file.readline().strip().split(maxsplit=2)
                sym = parts[0]
                color_string = parts[-1]
                color_map[sym] = color_string
            image_data = [file.readline().strip() for _ in range(rows)]
        return cols, rows, color_map, image_data
    except FileNotFoundError:
        print("Error: File not found.")
        exit()  # Exit the program if file is not found

def plot_image(T, cols, rows, color_map, image_data, rotate=False):
    turtle.tracer(0, 0)
    T.hideturtle()
    for row in range(rows):
        for col in range(cols):
            symbol = image_data[row][col]
            color = color_map.get(symbol, "black")
            x = col - cols // 2
            y = rows // 2 - row
            if rotate:
                x, y = -x, -y
            plotIt(T, x * 10, y * 10, 5, color)
    turtle.update()

def main():
    turtle.bgcolor("gray40")
    t = turtle.Turtle()

    # Ask for the file name
    filename = input("Enter the XPM file name (e.g., smiley_emoji_mod.xpm or rocky_bullwinkle_mod.xpm): ")

    # Read the XPM file
    cols, rows, color_map, image_data = read_xpm_file(filename)

    
    rotate = input("Would you like to rotate the image? (yes/no): ").strip().lower() == 'yes'

    # Plot the image
    plot_image(t, cols, rows, color_map, image_data, rotate)

    turtle.done()

if __name__ == "__main__":
    main()
