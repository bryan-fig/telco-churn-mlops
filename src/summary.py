from pathlib import Path
import csv

# Resolver la ruta del CSV a partir de la ubicación de este archivo.
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "data" / "telco_sample.csv"

with DATA_PATH.open("r", encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

total = len(rows)
churned = sum(row["Churn"] == "Yes" for row in rows)

print(f"Clientes en la muestra: {total}")
print(f"Clientes con Churn = Yes: {churned}")
print("Resumen inicial del proyecto Telco Customer Churn")
