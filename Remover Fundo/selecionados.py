import os

# Cria um arquivo de saída
output_file = 'imagens.txt'

# Nome do próprio script e outros arquivos a serem ignorados
ignored_files = {'backgroundremove.py', 'automa.bat', output_file, os.path.basename(__file__)}

# Caminho da pasta onde os arquivos estão localizados
directory = os.getcwd()  # Diretório atual

# Lista para armazenar os nomes dos arquivos que não serão ignorados
file_names = []

# Itera sobre os arquivos no diretório
for file_name in os.listdir(directory):
    # Verifica se o arquivo deve ser ignorado
    if file_name not in ignored_files and os.path.isfile(os.path.join(directory, file_name)):
        file_names.append(file_name)

# Salva os nomes dos arquivos no arquivo de saída
try:
    with open(output_file, 'w') as f:
        for name in file_names:
            f.write(name + '\n')
    print(f"Lista de arquivos salva em '{output_file}' com sucesso.")
except Exception as e:
    print(f"Erro ao salvar a lista de arquivos: {e}")
