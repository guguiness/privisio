import cv2
from detectors.placa_detector import PlacaDetector
from detectors.rosto_detector import RostoDetector
from utils.image_utils import desenhar_retangulos, borrar_nao_selecionados


def main():
    # imagem_path = input("Digite o caminho da imagem: ")
    imagem_path = "inputs/pessoas_2.jpg"
    image = cv2.imread(imagem_path)
    if image is None:
        print("Imagem não encontrada.")
        return

    placa_detector = PlacaDetector()
    rosto_detector = RostoDetector()

    detections = []

    try:
        detections += placa_detector.detectar(image)
    except Exception as e:
        print(f"Erro na detecção de placas: {e}")

    try:
        detections += rosto_detector.detectar(image)
    except Exception as e:
        print(f"Erro na detecção de rostos: {e}")

    if not detections:
        print("Nenhum objeto detectado.")
        return

    preview = image.copy()
    desenhar_retangulos(preview, detections)
    cv2.imshow("Detecções - pressione qualquer tecla para continuar", preview)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\nSelecione os índices dos objetos que você deseja manter visíveis.")
    for i, (tipo, x1, y1, x2, y2) in enumerate(detections):
        print(f"{i}: {tipo}")

    print("Ex: 0,2,4   (os demais serão borrados)")
    print("Ou pressione ENTER para borrar todos.")

    selecionados_input = input("Índices a manter: ").strip()
    if selecionados_input:
        try:
            selecionados = list(map(int, selecionados_input.split(",")))
        except:
            print("Formato inválido. Nenhum objeto será mantido.")
            selecionados = []
    else:
        selecionados = []

    borrada = borrar_nao_selecionados(image.copy(), detections, selecionados)
    output_path = "outputs/imagem_borrada.jpg"
    cv2.imwrite(output_path, borrada)

    print(f"\nImagem borrada salva como: {output_path}")
    cv2.imshow("Imagem Final", borrada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
