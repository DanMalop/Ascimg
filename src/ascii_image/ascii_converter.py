import numpy as np

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

