# docs/REGISTRE.md -- ouvert à l'étape 2, complété aux étapes 3 et 4, arrêté à l'étape 5, fermé ligne à ligne à l'étape 6
# Registre des défauts LogWatch - N défaut(s) ouvert(s) au AAAA-MM-JJ
| n° | date       | symptôme observé                                             | fonction suspectée | état   |
|----|------------|--------------------------------------------------------------|--------------------|--------|
| B1 | AAAA-MM-JJ | test_d1_somme_egale_total_lines rouge : attendu 6, reçu 3    | d1_requetes_par_ip | ouvert |
| B2 | AAAA-MM-JJ | test_d3_ignore_url_legitime rouge : attendu [], reçu ...     | d3_scan            | ouvert |
| B3 | 2026-11-11 | seuil_pic dépassé mais D4 affiche alerte=False (max 170/min) | d4_pic_trafic      | ouvert |
| B4 | 2026-11-25 | rapport vieilli de 8 jours non purgé : D6 rapports purges : 0| d6_purger_rapports | ouvert |


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
## B3 : D4 compare la charge moyenne par minute au seuil, pas la fenêtre la plus chargée
Date : 11/11/2026
Symptôme : ma fenêtre la plus chargée compte 190 requêtes, seuil_pic = 100,
  la ligne D4 affiche « alerte=false (max 170/min) » : le seuil est dépassé
  mais aucune alerte n'est levée.
Fonction suspectée : d4_pic_trafic
Comparaison au seuil : ligne 11, « charge > seuil_pic ».
Cette valeur est : charge (ligne 8), la moyenne des comptes par minute
  (statistics.mean), et non le compte d'une fenêtre ni le maximum.
Paramètres :
  - entrees : lu ligne 4
  - seuil_pic : lu ligne 11
  - fenetre_minutes : jamais
État : ouvert (non corrigé)

## B4 - D6 garde des rapports trop vieux
Date : 25/11/2026
Symptôme : rapport-20260916-103658.json vieilli à -8 jours (LastWriteTime 17/11/2026 13:42),
  second lancement : « D6 rapports purges : 0 ». Le même test à -400 jours purge bien (1).
README (retention_jours) : <phrase recopiée>
Fonction visée : d6_purger_rapports, ligne <n> : <ligne qui calcule la limite>
Cause racine : limite_jours = retention_jours * 30
  (jours traités comme des mois : seuil réel = retention_jours x 30 jours)
Correction prévue : limite_jours = retention_jours
Preuve : sortie terminal D6 + contenu de essais/ après le second lancement
État : ouvert (non corrigé)