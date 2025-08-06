from ascimg import input, output, ascii_converter, img_utils
from common.config import ASCIICHARS
import sys


def main():
    args = input.console_input()

    # lista de caracteres que representan los niveles de luz
    try:
        imgprosc = img_utils.imgprepare(args.filesource, args.scale)
        ascii_output = ascii_converter.asciiconv(imgprosc, ASCIICHARS, args.invert)

        if args.output:
            output.output_file(args.output, ascii_output)
        else:
            for line in ascii_output:
                output.print_color(line, args.color)

    except AssertionError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
