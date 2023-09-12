import networkx as nx
import wikipediaapi
import requests

NAMES = [
            "Romolo", 
            "Cesare", 
            "Dante Alighieri", 
            "Leonardo Da Vinci", 
            "Benito Mussolini", 
            "Umberto II di Savoia", 
            "Rita Levi Montalcini", 
            "Silvio Berlusconi", 
            "Mario Draghi"
        ]

KEYWORDS = [
            "scoperta", "scoperto", 
            "contribuito", 
            "premiato", "premiata", "premio", 
            "riconosciuto"
            ]

# Creazione un wikipedia api wrapper
wiki = wikipediaapi.Wikipedia(
        language='it',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

def getPageRank(name):

    # Creazione grafo vuoto
    G = nx.DiGraph()

    # Recupero pagina Wikipedia 
    page = wiki.page(name)

    # Aggiunta nodi
    G.add_nodes_from([page.title])

    # Recupero link interni alla pagina
    for link in page.links.items():
        G.add_nodes_from([link[0]])
        G.add_edge(page.title, link[0])

    # Calcolo PageRank
    pr = nx.pagerank(G)

    # Estrazione PageRank 
    for node, score in pr.items():
        if node == name:
            return node, score

def getPageViews(name):

    # Formattazione necessaria per la wikimedia API
    title = name.replace(" ", "_")

    # Costruzione url, recupera le visite alla pagina wikipedia effettuate da utenti reali, nel mese di marzo 2023
    url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/it.wikipedia.org/all-access/user/{title}/monthly/20230301/20230331'

    # Headers necessari per l'API
    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}
    
    # Recupero dei dati
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Estrazione numero di visite
    return data['items'][0]['views']

def getKeywordsCount(name):
    
    count = 0

    # Estrazione testo
    pagetext = wiki.page(name).text

    # Aggiornamento contatore
    for word in KEYWORDS:
        if word in pagetext.split():
            count += 1

    return count

def sortByPageRank(e):
    return e['pagerank']

def sortByPageViews(e):
    return e['pageviews']

def sortByTotalPoints(e):
    return e['rank_total']

candidates = []

for name in NAMES:
    node, score = getPageRank(name)
    views = getPageViews(name)
    keywords = getKeywordsCount(name)
    dic = dict(name=name, pagerank=score, pageviews=views, keywords=keywords)
    candidates.append(dic)


# Assegnazione punteggio per pageviews
# pageviews alto - punteggio alto
candidates.sort(reverse=True, key=sortByPageViews)
i = 0
for candidate in candidates:
    candidate['pageviewPoints'] = len(NAMES)-i
    i += 1 


# Assegnazione punteggio per pagerank
# pagerank basso - punteggio alto
candidates.sort(key=sortByPageRank)
i = 0
for candidate in candidates:
    candidate['pagerankPoints'] = len(NAMES)-i
    i += 1   


# Calcolo punteggio totale
# punti pagerank + punti pageviews + 2 punti per ogni keyword
for candidate in candidates:
    candidate['rank_total'] = candidate['pageviewPoints'] + candidate['pagerankPoints'] + (2*candidate['keywords'])

# print(candidates)

# Stampa della classifica
candidates.sort(reverse=True, key=sortByTotalPoints) 
i = 1
print("Classifica Borda Ranking:")
for candidate in candidates:
    print(f"{i}) {candidate['name']}: {candidate['rank_total']} punti")
    i += 1