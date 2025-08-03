import numpy as np
import cv2 as cv
import argparse as ap
import os
import sys
# Importamos numpy para tratamiento de datos y cv2 para tratamiento de imagenes


# funcion encargada de preparar la imagen, matriz blanco y negro, y reducir resolucion
def imgprepare(imgsrc: str, factorscaling: float) -> np.ndarray:
    img = cv.imread(imgsrc, cv.IMREAD_GRAYSCALE)
    assert img is not None, (
        f"Error: la imagen '{imgsrc}' no se encontró o no se pudo cargar"
    )
    res_img = cv.resize(
        img, None, fx=factorscaling, fy=factorscaling, interpolation=cv.INTER_CUBIC
    )
    # print(res_img)
    return res_img


# funcion encargada de transformar la matriz de pixeles en una matriz de caracteres
def asciiconv(img: np.ndarray, asciichars: list[str], invert=False) -> list[str]:
    # los caracteres se ordenan del mas oscuro al mas claro
    asciichars = asciichars if invert else asciichars[::-1]
    num_chars = len(asciichars)
    # se determina el rango de cada nivel de brillo
    light_range = 255 // num_chars
    ascii_img = ["```"]
    for row_pixels in img:
        asciirow = []
        for pixel_value in row_pixels:
            # se determina el nivel de brillo del pixer de acuerdo a cuantos rangos de brillo caben en su valor
            index = min(pixel_value // light_range, num_chars - 1)
            asciirow.append(asciichars[index])
        ascii_img.append("".join(asciirow))
    ascii_img.append("```")

    return ascii_img


# funcion encargada de crear un archivo con el texto ASCII de la imagen
def output_file(output_path: str, ascii_img: list[str]):
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_path, "w") as f:
        for line in ascii_img:
            f.write(line + "\n")
    print(f"\nAscii art saved in: {output_path}")


def main():
    parser = ap.ArgumentParser(
        prog="ascimg",
        description="Asciimg lets you see all your images on the terminal with ASCII characters",
        epilog="If you need more information visit our Github site",
    )

    # ruta de la imagen que se quiere visualizar
    parser.add_argument("filesource", type=str, help="Path to the image file (e.g., 'monio.png').")
    # escala de la imagen, esto permite cambiar la resolucion para mejorar la visualizacion en la terminal
    # Requiere un numero int o float como argumento
    parser.add_argument(
        "-s",
        "--scale",
        default=0.3,
        help="""Scale factor to resize the image before conversion.
        A smaller value (e.g., 0.05) produces denser ASCII art.
        Default: 0.3""",
        type=float,
    )
    # Permite cambiar el orden de los caranteres de mas oscuro a claro para adaptarse a diferentes tonalidades del fondo de la terminal
    # Requiere Truo o False como argumento
    parser.add_argument("-i", "--invert", default=False, type=bool,
                        help="""Inverts the order of ASCII characters. Lighter characters
                        will be used for darker pixels and vice versa.""")
    # genera un archivo con los caracteres de la imagen, requiere el nombre del archivo deseado como argumento
    parser.add_argument("-o", "--output", type=str,
                        help="""Path to the file where the ASCII art will be saved.
                        If not specified, it will be printed to the console.""")

    args = parser.parse_args()

    # lista de caracteres que representan los niveles de luz
    asciichars = ["▓", "▒", "░", "*", ".", " "]
    try:
        imgprosc = imgprepare(str(args.filesource), float(args.scale))
        ascii_output = asciiconv(imgprosc, asciichars, args.invert)

        if args.output:
            output_file(args.output, ascii_output)
        else:
            for line in ascii_output:
                print(line)

    except AssertionError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
