"""
analizar_resultados.py

Calcula las métricas estándar de una simulación de phishing (Open Rate,
Click Rate, PSR / Credential Submission Rate, Report Rate) a partir de los
CSV exportados directamente desde GoPhish.

USO
---
    python analizar_resultados.py archivo1.csv archivo2.csv ...
    python analizar_resultados.py data/*.csv
    python analizar_resultados.py data/*.csv --out resumen.csv

El ciclo (1 o 2) se detecta automáticamente si el nombre del archivo contiene
"ciclo 1" / "ciclo_1" / "ciclo1" (o su equivalente con 2). Si no lo detecta,
lo muestra como "N/A" y solo entra en el detalle por archivo, no en el
consolidado por ciclo.
"""

import argparse
import csv
import re
from pathlib import Path

# GoPhish reporta el "status" como el punto más avanzado alcanzado por el
# usuario. Este orden permite calcular tasas acumulativas: si hizo clic,
# también se cuenta como que abrió el correo.
STATUS_RANK = {
    "Email Sent": 0,
    "Email Opened": 1,
    "Clicked Link": 2,
    "Submitted Data": 3,
}


def detectar_ciclo(nombre_archivo: str) -> str:
    m = re.search(r"ciclo[_\s]*([12])", nombre_archivo, re.IGNORECASE)
    return f"Ciclo {m.group(1)}" if m else "N/A"


def analizar_csv(ruta: Path) -> dict:
    """Lee un export de GoPhish y devuelve los conteos y tasas de esa campaña."""
    sent = opened = clicked = submitted = reported = 0

    with ruta.open(newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            sent += 1
            rank = STATUS_RANK.get(fila.get("status", ""), 0)
            if rank >= 1:
                opened += 1
            if rank >= 2:
                clicked += 1
            if rank >= 3:
                submitted += 1
            if fila.get("reported", "").strip().lower() == "true":
                reported += 1

    def pct(n):
        return round(100 * n / sent, 1) if sent else 0.0

    return {
        "archivo": ruta.name,
        "ciclo": detectar_ciclo(ruta.name),
        "sent": sent,
        "opened": opened,
        "clicked": clicked,
        "submitted": submitted,
        "reported": reported,
        "open_rate": pct(opened),
        "click_rate": pct(clicked),
        "psr": pct(submitted),
        "report_rate": pct(reported),
    }


def imprimir_tabla(filas):
    columnas = ["archivo", "ciclo", "sent", "opened", "clicked", "submitted",
                "reported", "open_rate", "click_rate", "psr", "report_rate"]
    ancho = {c: max(len(c), max(len(str(f[c])) for f in filas)) for c in columnas}

    print("\n=== Detalle por campaña ===")
    print(" | ".join(c.ljust(ancho[c]) for c in columnas))
    print("-+-".join("-" * ancho[c] for c in columnas))
    for f in filas:
        print(" | ".join(str(f[c]).ljust(ancho[c]) for c in columnas))


def imprimir_consolidado_por_ciclo(filas):
    ciclos = {}
    for f in filas:
        c = ciclos.setdefault(f["ciclo"], dict(sent=0, opened=0, clicked=0, submitted=0, reported=0))
        for k in ("sent", "opened", "clicked", "submitted", "reported"):
            c[k] += f[k]

    print("\n=== Consolidado por ciclo ===")
    for ciclo, c in sorted(ciclos.items()):
        sent = c["sent"]

        def pct(n):
            return round(100 * n / sent, 1) if sent else 0.0

        print(f"{ciclo}: Sent={sent}  Open Rate={pct(c['opened'])}%  "
              f"Click Rate={pct(c['clicked'])}%  PSR={pct(c['submitted'])}%  "
              f"Report Rate={pct(c['reported'])}%")


def guardar_csv(filas, ruta_salida: str):
    columnas = ["archivo", "ciclo", "sent", "opened", "clicked", "submitted",
                "reported", "open_rate", "click_rate", "psr", "report_rate"]
    with open(ruta_salida, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(filas)
    print(f"\n[OK] Resumen guardado en {ruta_salida}")


def main():
    parser = argparse.ArgumentParser(
        description="Calcula Open/Click/PSR/Report Rate a partir de CSV exportados de GoPhish.")
    parser.add_argument("csvs", nargs="+", help="Uno o más archivos CSV de resultados de GoPhish")
    parser.add_argument("--out", help="Ruta opcional para guardar la tabla resumen en un CSV")
    args = parser.parse_args()

    filas = [analizar_csv(Path(p)) for p in args.csvs]

    imprimir_tabla(filas)
    imprimir_consolidado_por_ciclo(filas)

    if args.out:
        guardar_csv(filas, args.out)


if __name__ == "__main__":
    main()
