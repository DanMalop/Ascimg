import os
import common.config as cf


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
    color_low = color.strip().lower()

    for i in range(len(cf.COLORS[0])):
        if color_low == cf.COLORS[0][i]:
            color_print = cf.COLORS[1][i]
            break

    print(color_print + text + cf.COLORS[1][-1])
