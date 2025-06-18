# 🛡️ Privisio

Privisio é uma aplicação Python para **identificação e ocultação automática de informações sensíveis** (como **placas de carro** e **rostos**) em imagens. O usuário pode selecionar quais objetos manter visíveis e exportar uma versão da imagem com os demais borrados.

💡 Interface com **Tkinter** (GUI simples), mas também suporta execução via console.

---

## ✅ Requisitos

- Python 3.10+ (projeto testado com Python **3.13**)
- pip (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

---

## 📦 Instalação

### 1. Clone o projeto (ou baixe como ZIP)
```bash
git clone https://github.com/seu-usuario/privisio.git
cd privisio
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
---

## 🖼️ Como Usar

### Opção 1 - Executar com Interface Gráfica (Tkinter)

#### 1. Execute o projeto
```bash
python main.py
```

#### 2. Processar imagem

- Clique em "Carregar imagem" para selecionar um arquivo .jpg.
- Clique em "Analisar" para detectar placas e rostos na imagem carregada.
- Marque os objetos que devem permanecer visíveis.
- Clique em "Gerar resultado" para salvar a imagem borrada.
- Use o botão "Refazer" para iniciar outra análise do zero.

### Opção 2 - Executar no Console (modo texto)

#### 1. No arquivo main.py, altere a última linha para:
```bash
main_console()
```

#### 2. Execute o projeto
```bash
python main.py
```

---

## ❓ Problemas Comuns
- Imagem não carregada? Verifique se o caminho está correto ou se o nome do arquivo tem acentos/espaços.
- Erro ao importar cv2? Certifique-se de que o OpenCV foi instalado corretamente.
- Tela branca na interface? Alguns widgets só aparecem após a imagem ser carregada e analisada.
