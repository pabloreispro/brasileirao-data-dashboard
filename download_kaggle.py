import os

os.makedirs("data", exist_ok=True)

os.system(
    "kaggle datasets download -d ricardomattos05/jogos-do-campeonato-brasileiro -p data/ --unzip"
)

print("Dataset atualizado com sucesso!")
