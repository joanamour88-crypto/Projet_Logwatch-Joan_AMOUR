from logwatch import lire_log
NOM_JOURNAL = "dix-echecs.log"
##################### Etape 3: Script d'exploration #####################
############## exo 1 ###################
sample_log, ignoree = lire_log("sample-logs.log")
print(f"il y a {len(sample_log)} lignes dans le fichier de log.")
#print(sample_log)

############## exo 2 ###################

#par_famille = {}
#for code in sample_log:
#    if code['statut'] in [200, 201, 202, 203, 204, 205, 206]:
#        par_famille[code['statut']] = par_famille.get(code['statut'], 0) + 1
#    elif code['statut'] in [300, 301, 302, 303, 304, 305, 306, 307, 308]:
#        par_famille[code['statut']] = par_famille.get(code['statut'], 0) + 1
#    elif code['statut'] in [400, 401, 402, 403, 404, 405, 406, 407, 408]:
#        par_famille[code['statut']] = par_famille.get(code['statut'], 0) + 1
#    elif code['statut'] in [500, 501, 502, 503, 504, 505, 506, 507, 508]:
#        par_famille[code['statut']] = par_famille.get(code['statut'], 0) + 1

#print(par_famille)
#print(sum(par_famille.values()))


par_famille = {}
for entree in sample_log:
    famille = str(entree['statut'])[:1] + "xx"   # 404 -> "4xx"
    par_famille[famille] = par_famille.get(famille, 0) + 1

print(par_famille)
print(sum(par_famille.values()), len(sample_log))

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

##################### Etape 4: Ticket: le pic que D4 ne voit pas #####################
############## exo 1 ###################
par_minute = {}
for entree in sample_log:
    minute = entree['date'][:17]
    par_minute[minute] = par_minute.get(minute, 0) + 1


minute_max = None
for minute, n in par_minute.items():
    if minute_max is None or n > par_minute[minute_max]:
        minute_max = minute

print(f"Minute la plus chargée : {minute_max} avec {par_minute[minute_max]} requêtes")
######## demande de verification par claude (Sonnet 5.5) ###############################
print("verification : " + str(sum(par_minute.values())) + " / " + str(len(sample_log)))

############### exo 2 ###################
fenetre_minutes = 5   # vérifie la valeur dans le README (D4)

par_fenetre = {}
for entree in sample_log:
    date = entree['date']
    minute = int(date[15:17])
    debut = minute - minute % fenetre_minutes
    cle = f"{date[:14]}:{debut:02d}"
    par_fenetre[cle] = par_fenetre.get(cle, 0) + 1

fenetre_max = None
for fenetre, n in par_fenetre.items():
    if fenetre_max is None or n > par_fenetre[fenetre_max]:
        fenetre_max = fenetre

print(f"Fenêtre la plus chargée : {fenetre_max} avec {par_fenetre[fenetre_max]} requêtes")

# 1. la somme des fenêtres = nombre de requêtes lues
print("vérification : " + str(sum(par_fenetre.values())) + " / " + str(len(sample_log)))

# 2. la fenêtre max contient la minute max de la question 1, avec un compte >= au sien
print("vérification : " + str(par_fenetre[fenetre_max]) + " >= " + str(par_minute[minute_max]))
debut_fenetre = int(fenetre_max[15:17])
minute_pic = int(minute_max[15:17])
print(fenetre_max[:14] == minute_max[:14] and debut_fenetre <= minute_pic < debut_fenetre + fenetre_minutes)

################# exo 3 ###################
# Documentation

################# exo 4 ###################
nb_requetes = sum(par_minute.values())   
nb_minutes = len(par_minute)             
charge = nb_requetes / nb_minutes
print(f"charge recalculée : {round(charge, 1)}")

############################### Etape 5: Tickets : les erreurs serveurs, et dix mots de passe #############################
############## exo 1 ###################
nb_requetes = len(sample_log)
nb_5xx = par_famille.get("5xx", 0)
part = nb_5xx / nb_requetes
print(f"Part des 5xx : {part:.1%}")

############## exo 2 ###################
sample_essai, ignorees = lire_log(NOM_JOURNAL)
print(f"Il y a {len(sample_essai)} échecs de connexion dans le fichier {NOM_JOURNAL}.")
par_ip = {}
for entree in sample_essai:
    par_ip[entree['ip']] = par_ip.get(entree['ip'], 0) + 1
print("Essai brute force :", par_ip)