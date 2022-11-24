def tempCharg(site):
    import requests
    import time

    debut = time.time()
    requests.get(site)
    temps= time.time() - debut
    return temps

def affiche(site,temps):
    print(f"Temps de Chargement de {site} {temps}")


affiche("https://www.google.com/",tempCharg("https://www.google.com/"))
affiche("https://www.ynet.com/",tempCharg("https://www.ynet.com/"))
affiche("https://www.imdb.com/",tempCharg("https://www.imdb.com/"))






