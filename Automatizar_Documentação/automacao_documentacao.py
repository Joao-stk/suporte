import os
from tkinter import Tk, simpledialog
import subprocess
import base64

def txt_to_html():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        imagens_dir = os.path.join(base_dir, 'imagens')
        os.makedirs(imagens_dir, exist_ok=True)

        txt_file = os.path.join(base_dir, 'processo.txt')
        html_file = os.path.join(base_dir, 'documentacao.html')

        if not os.path.exists(txt_file):
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write("Edite este arquivo com o conteúdo da documentação. Use @nome_da_imagem para inserir imagens.\n")

        # CSS embutido
        css_embutido = '''
        <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            background: #fff;
            padding: 30px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        p {
            line-height: 1.6;
            margin: 10px 0;
            color: #000000;
            font-size: 18px;
        }
        .process-image {
            display: block;
            max-width: 100%;
            height: auto;
            margin: 20px auto;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        </style>
        '''

        # Mapeia imagens com base64
        img_map = {}
        for file in os.listdir(imagens_dir):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                name_no_ext, ext = os.path.splitext(file)
                path = os.path.join(imagens_dir, file)
                with open(path, 'rb') as img_f:
                    encoded = base64.b64encode(img_f.read()).decode('utf-8')
                    mime_type = f"image/{ext[1:].lower() if ext[1:].lower() != 'jpg' else 'jpeg'}"
                    data_uri = f"data:{mime_type};base64,{encoded}"
                    img_map[name_no_ext.lower()] = data_uri

        # Título da documentação
        Tk().withdraw()
        titulo = simpledialog.askstring("Título", "Digite o título da documentação:")

        subprocess.call(['notepad.exe', txt_file])

        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo or "Documentação do Processo"}</title>
    {css_embutido}
</head>
<body>
    <div class="container">
        <h1>{titulo or "Documentação do Processo"}</h1>
'''

        for line in lines:
            stripped = line.strip()
            if not stripped:
                html += "<br>\n"
                continue

            if stripped.startswith('*'):
                html += f"<h2>{stripped[1:].strip()}</h2>\n"
                continue

            palavras = stripped.split()
            linha_convertida = ""
            for palavra in palavras:
                if palavra.startswith('@'):
                    chave = palavra[1:].lower()
                    if chave in img_map:
                        img_src = img_map[chave]
                        linha_convertida += f'<img src="{img_src}" class="process-image" alt="{chave}"> '
                    else:
                        linha_convertida += palavra + " "
                else:
                    linha_convertida += palavra + " "

            html += f"<p>{linha_convertida.strip()}</p>\n"

        html += '''
    </div>
</body>
</html>'''

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"\n✅ HTML gerado com sucesso em: {html_file}")
        print("🖼️ As imagens foram embutidas no HTML e ele pode ser movido ou enviado sem a pasta 'imagens'.")

    except Exception as e:
        print(f"\n❌ Erro: {e}")

txt_to_html()

