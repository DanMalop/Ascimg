import numpy as np
import cv2 as cv
import os


# funcion encargada de preparar la imagen, matriz blanco y negro, y reducir resolucion
def imgprepare(imgsrc: str, factorscaling: float) -> np.ndarray:
    img = cv.imread(imgsrc, cv.IMREAD_GRAYSCALE)
    assert img is not None, (
        f"Error: la imagen '{imgsrc}' no se encontró o no se pudo cargar"
    )
    res_img = cv.resize(
        img, None, fx=factorscaling, fy=factorscaling, interpolation=cv.INTER_CUBIC
    )
    return res_img


# funcion encargada de crear un archivo con el texto ASCII de la imagen
def output_file(output_path: str, ascii_img: list[str]):
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(output_path, "w") as f:
        for line in ascii_img:
            f.write(line + "\n")
    print(f"\nAscii art saved in: {output_path}")
