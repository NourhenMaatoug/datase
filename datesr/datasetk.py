import pmd
import csv
import os

cloner_repo(url_repo, chemin_destination)

def analyser_projet(chemin_projet, chemin_sortie):

    regles = pmd.PMDConfiguration()
    regles.rule_sets = "rulesets/java/quickstart.xml" 
    rapport = pmd.Report.run(chemin_projet, config=regles)
    metrics = {
    "nombre_fichiers": rapport.files_analyzed,
    "nombre_violations": len(rapport.violations),
    # Ajoutez d'autres métriques selon vos besoins (lignes de code, complexité, etc.)
  }
    # Extrayez les informations sur les code smells
    smells = []
    for violation in rapport.violations:
        smells.append({
            "fichier": violation.filename,
            "ligne": violation.beginline,
            "type": violation.rule.name,
            "gravite": violation.priority.name,
            "description": violation.message,
            })
        # Enregistrez les métriques dans un fichier CSV
        with open(os.path.join(chemin_sortie, "metrics.csv"), "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=metrics.keys())
            writer.writeheader()
            writer.writerow(metrics)
            # Enregistrez les informations sur les smells dans un fichier CSV
        with open(os.path.join(chemin_sortie, "smells.csv"), "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=smells[0].keys())
            writer.writeheader()
            writer.writerows(smells)

def main():
    chemin_projet = "C:/Users/norhe/pfaa"
    chemin_sortie = "C:/Users/norhe/sortier"

    analyser_projet(chemin_projet, chemin_sortie)

if __name__ == "__main__":
    main()