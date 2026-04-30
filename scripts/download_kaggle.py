import os

os.makedirs("data", exist_ok=True)

os.system(
    "kaggle datasets download -d patelris/formula-1-complete-dataset-1950-2026 -p data/ --unzip"
)

print("Dataset atualizado com sucesso!")
