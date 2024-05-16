import cv2
import numpy as np

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("Erro ao carregar as imagens.")
        return

    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    _, img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    _, img2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

    dist = np.linalg.norm(img1 - img2)

    print(f"A distância entre as imagens é: {dist}")

compare_images('imagem1.png', 'imagem2.png')