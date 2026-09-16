# docs/CARTE.md -- gabarit de départ, amendé à l'étape 4
# Carte LogWatch v0 - v1 du AAAA-MM-JJ (étape 1)
## Entrées et sorties

lit : le fichier de logs Apache (brut), la configuration (JSON), et les variables d'environnement (via .env) (et qui décide du chemin : l'option, .env, ou la valeur par défaut)
écrit : un fichier de rapport au format JSON horodaté dans le dossier spécifié
supprime : les anciens fichiers de rapports JSON présents dans le dossier `reports` qui dépassent la durée de rétention

## Les fonctions, dans l'ordre du fichier

Les quatorze lignes se generent, depuis logwatch/ :
Select-String -Path logwatch.py -Pattern '^def ' |
ForEach-Object { "| " + $_.Line.Substring(4).TrimEnd(':') + " | |" }
Coller le resultat sous l'en-tete, puis remplir la seule colonne rend.

| fonction                          |                   rend                                                                                            |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| charger_env(chemin=".env")        | sert a chercher le dossier .env, le parcours ligne par ligne et permet de stocker des variables de configuration  |  
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| charger_config(chemin)            | sert a charger le fichier "config.json" grâce a une bibliotheque par defaut (defaut est dans logwatch.py)         |
|                                   | si il n'y a pas deconfiguration déja existante.                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| parser_ligne(ligne)               | un dictionnaire à onze clés, ou None si la ligne n'a pas la forme attendue                                        |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| lire_log(chemin, encodage="utf-8")| lit les logs, met de coter les lignes ignorés(ligne avec defauts)                                                 |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|
| anonymiser_ip(ip)                 | sert a masquer le dernier octet d'une IPv4 : 203.0.113.7 -> 203.0.113.x (RGPD).                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|

## Les détections annoncées par le README (question 7)
| détection | fonction           | ce que le README lui demande (seuil, unité, « dès que » / « au moins » / « au-delà »)                           |
|-----------|--------------------|-----------------------------------------------------------------------------------------------------------------|
| D1        | d1_requetes_par_ip | Liste les `top_ips` (10) IP ayant fait le plus de requêtes avec succès (statut < 400).                          |
| D2        | d2_brute_force     | Alerte au-delà de `seuil_brute_force` (10) tentatives POST échouées (401/403) sur `url_login`.              |
| D3        | d3_scan            | Alerte dès que l'IP a testé au moins `seuil_scan` (5) URLs suspectes différentes (liste `MOTIFS_SCAN`). |
| D4        | d4_pic_trafic      | Alerte au-delà d'une moyenne de `seuil_pic` (100) requêtes par minute.                                      |
| D5        | d5_erreurs_5xx     | Alerte au-delà d'un ratio de `seuil_5xx` (0.5 soit 50%) de requêtes serveur en erreur (500-599).            |
| D6        | d6_purger_rapports | Supprime les rapports dès que leur ancienneté dépasse la limite fixée (censée être `retention_jours`).      |

## Points opaques (question 8)

-   Ligne 114 (dans `d4_pic_trafic`) : Que vaut le paramètre `fenetre_minutes` quand il est passé à la fonction ? Il est censé valoir `5` selon les paramètres par défaut, mais ce paramètre n'est jamais utilisé dans la fonction ! Le script calcule une moyenne globale par minute sur la totalité du fichier log au lieu d'observer une fenêtre glissante.

-   Ligne 132 (dans `d6_purger_rapports`) : Que vaut `limite_jours` quand `retention_jours` vaut `7` (la valeur par défaut) ? Il vaut 210 ! (`limite_jours = retention_jours * 30`). Le commentaire indique "retention exprimée en mois", ce qui est en contradiction totale avec le nom de la variable `retention_jours` qui sous-entend clairement des jours. Cela risque de conserver les logs liés aux IPs pendant 210 jours (presque 7 mois) au lieu des 7 jours prévus, ce qui pose un problème de conformité RGPD.