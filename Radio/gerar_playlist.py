import os
import random

# Caminho base: a pasta onde o script está rodando
base_dir = os.path.dirname(os.path.abspath(__file__))

# Subpastas relativas
pasta_musicas = os.path.join(base_dir, "musicas")
pasta_vinhetas = os.path.join(base_dir, "vinhetas")
playlist_saida = os.path.join(base_dir, "playlist_mixxx.m3u")

# Extensões aceitas
extensoes = ('.mp3', '.wav', '.ogg')

# Caminhos relativos (usados no .m3u)
musicas = [os.path.join("musicas", f) for f in os.listdir(pasta_musicas) if f.lower().endswith(extensoes)]
vinhetas = [os.path.join("vinhetas", f) for f in os.listdir(pasta_vinhetas) if f.lower().endswith(extensoes)]

# Debug
print(f"{len(musicas)} músicas encontradas.")
print(f"{len(vinhetas)} vinhetas encontradas.")

# Embaralha músicas e vinhetas
random.shuffle(musicas)
random.shuffle(vinhetas)

# Gera a playlist com vinheta a cada 5 músicas
playlist = []
contador = 0
vinheta_index = 0

for musica in musicas:
    playlist.append(musica)
    contador += 1
    if contador == 5:
        contador = 0
        if vinhetas:
            playlist.append(vinhetas[vinheta_index % len(vinhetas)])
            vinheta_index += 1

# Escreve a playlist em formato M3U
with open(playlist_saida, 'w', encoding='utf-8') as f:
    f.write("#EXTM3U\n")
    for item in playlist:
        f.write(item.replace("\\", "/") + "\n")  # usa "/" para compatibilidade

print("✅ Playlist criada com sucesso:", playlist_saida)
