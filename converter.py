import pyreadstat

# Lê o arquivo XPT
df, meta = pyreadstat.read_xport("DEMO_I.xpt")

# Salva como CSV
df.to_csv("DEMO_I.csv", index=False)

print("✅ Conversão concluída: DEMO_I.csv foi criado com sucesso.")
