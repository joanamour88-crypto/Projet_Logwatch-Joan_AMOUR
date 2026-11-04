# docs/REGISTRE.md -- ouvert à l'étape 2, complété aux étapes 3 et 4, arrêté à l'étape 5, fermé ligne à ligne à l'étape 6
# Registre des défauts LogWatch - N défaut(s) ouvert(s) au AAAA-MM-JJ
| n° | date       | symptôme observé                                          | fonction suspectée | état  |
|----|------------|-----------------------------------------------------------|--------------------|--------|
| B1 | AAAA-MM-JJ | test_d1_somme_egale_total_lines rouge : attendu 6, reçu 3 | ...                | ouvert |
| B2 | AAAA-MM-JJ | test_d3_ignore_url_legitime rouge : attendu [], reçu ...  | ...                | ouvert |
## B1 - <le symptôme, en cinq mots>
Test en échec : test_d1_somme_egale_total_lines
Attendu / reçu : 6 / 3
Fonction visée : d1_requetes_par_ip, ligne 116 (logwatch.py)
Cause racine : if e["statut"] < 400:
Correction prévue : if e["statut"] : #< 400:
(étape 6) Correctif : commit <hash>, <auteur>, le AAAA-MM-JJ
Vérifié par : <nom>, sur <le cas éprouvé, différent de celui du test>
## B2 - <un seuil trop petit !>
Test en échec : test_d3_ignore_url_legitime
Attendu / reçu : []
Fonction visée : d3_scan, ligne 142
Cause racine : if len(urls) >= seuil:
Correction prévue : if len(urls) <= seuil:
(étape 6) Correctif : commit <hash>, <auteur>, le AAAA-MM-JJ
Vérifié par : <nom>, sur <le cas éprouvé, différent de celui du test>