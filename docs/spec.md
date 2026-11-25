# Spécification LogWatch - créée le 2026-11-18
Amendements : (date) - (ce qui change et pourquoi)

Prérequis communs : sample-logs.log et config.json du kit.
Étape commune : python logwatch.py

## D1 - Somme par IP
| Cas     | Id    | Prérequis                      | Étape | Résultat attendu                                                         | Obtenu | Statut |
|---------|-------|--------------------------------|-------|--------------------------------------------------------------------------|--------|--------|
| nominal | D1-01 | sample-logs.log, config du kit | ...   | somme des comptes par IP = requêtes lues = N (explorer.py, fonction ...) |        |        |
| limite  | D1-02 | (à définir)                    | ...   | (chiffre)                                                                |        |        |
| erreur  | D1-03 | une ligne mal formée           | ...   | ligne ignorée, comptée dans « ignorées » (chiffre)                       |        |        |

## D2 - Brute force
(même tableau, trois cas)
...
## D7 - Requêtes lentes
(même tableau, trois cas)