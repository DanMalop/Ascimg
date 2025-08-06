import os
import config as cf

# funcion encargada de crear un archivo con el texto ASCII de la imagen
def output_file(output_path: str, ascii_img: list[str]):
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_path, "w") as f:
        for line in ascii_img:
            f.write(line + "\n")
    print(f"\nAscii art saved in: {output_path}")

def print_color(text: str, color: str):
    color_low = lower(color.strip())
    color_print = ''

    if color_low == 'red':
        color_print = cf.RED
    elif color_low == 'blue':
        color_print = cf.BLUE
    elif color_low == 'green':
        color_print = cf.GREEN
    elif color_low == 'yellow':
        color_print = cf.YELLOW
    else:
        color_print = ''
    print(color_print + text + cf.NC)
