import numpy as np
import cv2

def detO(mascara, objeto1, objeto2, imagem):
    img1 = cv2.cvtColor(mascara, cv2.COLOR_BGR2GRAY)
    objeto1 = cv2.cvtColor(objeto1, cv2.COLOR_BGR2GRAY)
    objeto2 = cv2.cvtColor(objeto2, cv2.COLOR_BGR2GRAY)
    a1, l1 = objeto1.shape
    a2, l2 = objeto2.shape
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    
    metodo = methods[1]

    resultado1 = cv2.matchTemplate(img1, objeto1, metodo)
    resultado2 = cv2.matchTemplate(img1, objeto2, metodo)
    minv1, maxv1, minl1, maxl1 = cv2.minMaxLoc(resultado1)
    minv2, maxv2, minl2, maxl2 = cv2.minMaxLoc(resultado2)
    if metodo in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location1 = minl1
        location2 = minl2
    else:
        location1 = maxl1
        location2 = maxl2

    bottomRight1 = (location1[0] + l1, location1[1] + a1)
    bottomRight2 = (location2[0] + l2, location2[1] + a2)
    cv2.rectangle(imagem, location1, bottomRight1, (0,0,255), 5)
    cv2.rectangle(imagem, location2, bottomRight2, (0,0,255), 5)
    return imagem
    # cv2.imshow('sera?', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# mascara = cv2.imread("screenshot1.png")
# ob1 = cv2.imread("objeto1.jpg")
# ob2 = cv2.imread("objeto2.jpg")

# detO(mascara, ob1, ob2)