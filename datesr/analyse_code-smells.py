import pmd
import csv
import os

def analyser_projet(chemin_projet, chemin_sortie):

  regles = pmd.PMDConfiguration()
  regles.rule_sets = "rulesets/java/quickstart.xml"

  # Analysez le projet
  rapport = pmd.Report.run(chemin_projet, config=regles)

  # Extrayez les métriques de code
  metrics = {
    "nombre_fichiers": rapport.files_analyzed,
    "nombre_violations": len(rapport.violations),
    
  }

  # Extrayez les types de code smells et leur nombre d'occurrences
  types_de_smells = {}
  for violation in rapport.violations:
    type_de_smell = violation.rule.name
    if type_de_smell not in types_de_smells:
      types_de_smells[type_de_smell] = 0
    types_de_smells[type_de_smell] += 1

  # Enregistrez les métriques dans un fichier CSV
  with open(os.path.join(chemin_sortie, "metrics.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=metrics.keys())
    writer.writeheader()
    writer.writerow(metrics)

  # Enregistrez les types de code smells et leurs occurrences dans un fichier CSV
  with open(os.path.join(chemin_sortie, "types_de_smells.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Type de code smell", "Nombre d'occurrences"])
    for type_de_smell, nombre in types_de_smells.items():
      writer.writerow([type_de_smell, nombre])

def main():
  # Chemin du projet à analyser
  chemin_projet = "C:/Users/norhe/pfaa"

  # Chemin du dossier pour enregistrer les données
  chemin_sortie = "C:/Users/norhe/data/code smell"

  # Analyser le projet et extraire les données
  analyser_projet(chemin_projet, chemin_sortie)

if __name__ == "__main__":
  main()