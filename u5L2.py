
def read_image_file(filename):
    try:
        # Open the file for reading
        with open(filename, "r") as fh:
            # Read and process the first line (dimensions and number of colors)
            dimensions = fh.readline().strip()
            cols, rows, num_colors = map(int, dimensions.split())

            print(f"Dimensions: {cols} columns x {rows} rows")
            print(f"Number of colors: {num_colors}")

            # Read and process the color definitions
            color_defs = {}
            for _ in range(num_colors):
                color_line = fh.readline().strip()
                sym, _, color = color_line.split()
                if sym == "~":
                    sym = " "  # Replace tilde with space
                color_defs[sym] = color

            print("\nColor definitions:")
            for sym, color in color_defs.items():
                print(f"{sym}: {color}")

          
            print("\nImage data:")
            image_data = []
            for _ in range(rows):
                line = fh.readline().strip()
                image_data.append(line)
                print(line)

        
        return cols, rows, color_defs, image_data

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


filename = "smiley_emoji_mod.xpm"
read_image_file(filename)
