import cv2

def desenhar_caixas(image, boxes, cor=(0,0,255)):
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        cv2.rectangle(image, (x1, y1), (x2, y2), cor, 2)
        cv2.putText(image, f"{i}", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)
    return image

def aplicar_blur(image, boxes, ignorar_indices):
    result = image.copy()
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        if i not in ignorar_indices:
            roi = result[y1:y2, x1:x2]
            blur = cv2.GaussianBlur(roi, (51, 51), 0)
            result[y1:y2, x1:x2] = blur
    return result
