import pmd
import csv

from git import Repo

def cloner_repo(url, chemin_destination):
  Repo.clone_from(url, chemin_destination)

# Exemple d'utilisation
url_repo = "https://github.com/user/repo.git"
chemin_destination = "C:/Users/norhe/pfaa"
cloner_repo(url_repo, chemin_destination)


def analyser_projet(chemin_projet):
  # Configurez les règles PMD
  regles = pmd.PMDConfiguration()
  regles.rule_sets = "rulesets/java/quickstart.xml"

  # Analysez le projet
  rapport = pmd.Report.run(chemin_projet, config=regles)

  # Extrayez les informations sur les code smells
  smells = []
  for violation in rapport.violations:
    smells.append({
      "fichier": violation.filename,
      "ligne": violation.beginline,
      "type": violation.rule.name,
      "gravite": violation.priority.name,
      "description": violation.message
    })
    with open("smells.csv", "w", newline="") as fichier_csv:
         writer = csv.DictWriter(fichier_csv, fieldnames=smells[0].keys())
         writer.writeheader()
         writer.writerows(smells)
         
chemin_base = "C:/Users/norhe/data/code smell"
for i, url_repo in enumerate(urls_repos):
    chemin_projet = f"{chemin_base}/projet_{i+1}"
    cloner_repo(url_repo, chemin_projet)
    analyser_projet(chemin_projet)

if __name__ == "__main__":
  main()
