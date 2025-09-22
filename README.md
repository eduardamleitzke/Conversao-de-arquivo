# Conversor XPT para CSV

Um programa simples em Python para **converter arquivos `.XPT` (SAS Transport)** em **`.CSV`**, facilitando a manipulação dos dados em Excel ou outras ferramentas que leem CSV.

## Funcionalidades

- Converte arquivos `.XPT` para `.CSV`.
- Mantém os nomes das colunas originais.
- Processo rápido e direto.

## Requisitos

- Python 3.8+
- Biblioteca `pyreadstat`

Instalação da dependência:

```bash
pip install pyreadstat
```

Como Usar:

Coloque o arquivo .XPT na mesma pasta do script ou informe o caminho completo.

Execute o script Python:

python convert.py

O arquivo .CSV será gerado com o mesmo nome do arquivo original, mas com extensão .csv.

Exemplo de uso:

```python
import pyreadstat

#Lê o arquivo XPT
df, meta = pyreadstat.read_xport("DEMO_I.xpt")

#Salva como CSV
df.to_csv("DEMO_I.csv", index=False)

print("✅ Conversão concluída: DEMO_I.csv foi criado com sucesso.")
```

## Licença
Mit license
