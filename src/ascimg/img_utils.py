import numpy as np
import cv2 as cv

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

