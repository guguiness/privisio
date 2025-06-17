import cv2
from detectors.placa_detector import PlacaDetector
from utils.image_utils import desenhar_caixas, aplicar_blur


def main():
    # path_imagem = input("Digite o caminho da imagem: ")
    path_imagem = "inputs/carros_1.jpg"
    imagem = cv2.imread(path_imagem)
    detector = PlacaDetector()
    caixas = detector.detectar(imagem)

    if not caixas:
        print("Nenhuma placa detectada.")
        return

    imagem_com_caixas = desenhar_caixas(imagem.copy(), caixas)
    cv2.imwrite("outputs/saida_com_caixas.jpg", imagem_com_caixas)
    print("Placas detectadas. Visualize o arquivo 'saida_com_caixas.jpg'.")

    print("\nSelecione as placas que você deseja manter visíveis (separadas por vírgula):")
    for i, box in enumerate(caixas):
        print(f"{i}: {box}")

    indices = input("Índices selecionados (ex: 0,2): ")
    indices_selecionados = set(map(int, indices.strip().split(",")))

    imagem_final = aplicar_blur(imagem.copy(), caixas, indices_selecionados)
    cv2.imwrite("outputs/imagem_final.jpg", imagem_final)
    print("Imagem final salva como 'imagem_final.jpg'.")


if __name__ == "__main__":
    main()
