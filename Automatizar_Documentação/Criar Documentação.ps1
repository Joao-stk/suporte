# Executar o script Python "transf_interna.py" na mesma pasta deste script PowerShell

# Obter o diretório atual onde está este script .ps1
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Caminho completo para o arquivo Python
$pythonScript = Join-Path $scriptDir "automacao_documentacao.py"

# Executar o script Python
python $pythonScript
