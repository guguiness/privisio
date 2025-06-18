import cv2

def desenhar_retangulos(image, detections):
    for i, (tipo, x1, y1, x2, y2) in enumerate(detections):
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 6)
        label = f"{i}: {tipo}"
        cv2.putText(image, label, (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    return image

def borrar_nao_selecionados(image, detections, selecionados):
    for i, (_, x1, y1, x2, y2) in enumerate(detections):
        if i not in selecionados:
            roi = image[y1:y2, x1:x2]
            blur = cv2.GaussianBlur(roi, (201, 201), 0)
            image[y1:y2, x1:x2] = blur
    return image

def carregar_imagem(caminho):
    image = cv2.imread(caminho)
    if image is None:
        raise FileNotFoundError()

    return image