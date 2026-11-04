from logwatch import lire_log

############## exo 1 ###################
sample_log, ignoree = lire_log("sample-logs.log")
print(f"il y a {len(sample_log)} lignes dans le fichier de log.")
#print(sample_log)

############## exo 2 ###################

compteur = {}
for code in sample_log:
    if code['statut'] in [200, 201, 202, 203, 204, 205, 206]:
        compteur[code['statut']] = compteur.get(code['statut'], 0) + 1
    elif code['statut'] in [300, 301, 302, 303, 304, 305, 306, 307, 308]:
        compteur[code['statut']] = compteur.get(code['statut'], 0) + 1
    elif code['statut'] in [400, 401, 402, 403, 404, 405, 406, 407, 408]:
        compteur[code['statut']] = compteur.get(code['statut'], 0) + 1
    elif code['statut'] in [500, 501, 502, 503, 504, 505, 506, 507, 508]:
        compteur[code['statut']] = compteur.get(code['statut'], 0) + 1

print(compteur)
print(sum(compteur.values()))

############## exo 3 ###################
# D1 de base donne 559 requetes  
compteur_ip = {}
for code in sample_log:
    adresse_ip = code['ip']
    compteur_ip[adresse_ip] = compteur_ip.get(adresse_ip, 0) + 1

print(len(compteur_ip))
print(compteur_ip)
print(sum(compteur_ip.values()))

############## exo 4 ###################
compteur_ipignoree = {}
for code in sample_log:
    if code['methode'] == 'POST' and code['url'] == '/login' and code['statut'] in [401, 403]:
        adresse_ip = code['ip']
        compteur_ipignoree[adresse_ip] = compteur_ipignoree.get(adresse_ip, 0) + 1

print(sum(compteur_ipignoree.values()))

############## exo 5 ###################
par_minutes = {}
for code in sample_log:
    date = code['date'][:17]
    par_minutes[date] = par_minutes.get(date, 0) + 1


nb_requete_min = None
for requete, count in par_minutes.items():
    if nb_requete_min is None or count > nb_requete_min:
        nb_requete_min = count

print(f"La durée minimale des requêtes est : {nb_requete_min}")

