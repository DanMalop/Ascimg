from common.config import DEFAULT_SCALE
import argparse as ap


def console_input():
    parser = ap.ArgumentParser(
        prog="ascimg",
        description="Asciimg lets you see all your images on the terminal with ASCII characters",
        epilog="If you need more information visit our Github site",
    )

    # ruta de la imagen que se quiere visualizar
    parser.add_argument(
        "filesource", type=str, help="Path to the image file (e.g., 'monio.png')."
    )
    # escala de la imagen, esto permite cambiar la resolucion para mejorar la visualizacion en la terminal
    # Requiere un numero int o float como argumento
    parser.add_argument(
        "-s",
        "--scale",
        default=DEFAULT_SCALE,
        help="""Scale factor to resize the image before conversion.
        A smaller value (e.g., 0.05) produces denser ASCII art.
        Default: 0.3""",
        type=float,
    )
    # Permite cambiar el orden de los caranteres de mas oscuro a claro para adaptarse a diferentes tonalidades del fondo de la terminal
    # Requiere Truo o False como argumento
    parser.add_argument(
        "-i",
        "--invert",
        default=False,
        type=bool,
        help="""Inverts the order of ASCII characters. Lighter characters
                        will be used for darker pixels and vice versa.""",
    )
    # genera un archivo con los caracteres de la imagen, requiere el nombre del archivo deseado como argumento
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="""Path to the file where the ASCII art will be saved.
                        If not specified, it will be printed to the console.""",
    )
    # color de los caracteres de la imagen
    parser.add_argument("-c", "--color", type=str, default="white")

    return parser.parse_args()
