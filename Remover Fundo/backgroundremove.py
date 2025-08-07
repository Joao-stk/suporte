from rembg import remove
from PIL import Image
import os

# Cria um diretório de saída para as imagens processadas
output_directory = 'output_images'
os.makedirs(output_directory, exist_ok=True)

# Lê os nomes das imagens a partir do arquivo txt
try:
    with open('imagens.txt', 'r') as file:
        image_paths = [line.strip() for line in file if line.strip()]  # Lê cada linha e remove espaços em branco
except FileNotFoundError:
    print("Erro: O arquivo 'imagens.txt' não foi encontrado.")
    exit(1)
except Exception as e:
    print(f"Erro ao ler o arquivo 'imagens.txt': {e}")
    exit(1)

# Processa cada imagem da lista
for input_image_path in image_paths:
    try:
        # Tente abrir a imagem
        image = Image.open(input_image_path)
        print(f"Processando '{input_image_path}'...")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_image_path}' não foi encontrado.")
        continue  # Continua com a próxima imagem
    except Exception as e:
        print(f"Erro ao abrir a imagem '{input_image_path}': {e}")
        continue

    try:
        # Tente remover o fundo
        output = remove(image)
    except Exception as e:
        print(f"Erro ao remover o fundo da imagem '{input_image_path}': {e}")
        continue

    try:
        # Tente salvar a imagem resultante com um novo nome no diretório de saída
        output_image_path = os.path.join(
            output_directory,
            f"{os.path.splitext(os.path.basename(input_image_path))[0]}semfundo.png"
        )
        output.save(output_image_path)
        print(f"Imagem salva com sucesso em '{output_image_path}'")
    except Exception as e:
        print(f"Erro ao salvar a imagem '{input_image_path}': {e}")
