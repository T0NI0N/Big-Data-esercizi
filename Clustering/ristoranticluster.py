import requests
import json

from pyclustering.cluster import kmedoids
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

# TripAdvisor API endpoint
url = "https://tripadvisor16.p.rapidapi.com/api/v1/hotels/searchHotelsByLocation"

# Cerca hotel a Varese
querystring = {
	"latitude":"45.820599",
	"longitude":"8.825058",
	"checkIn":"2023-05-19",
	"checkOut":"2023-05-19",
	"pageNumber":"1",
	"currencyCode":"EUR"
}

# Headers necessari
headers = {
	"X-RapidAPI-Key": "d95a0315camsh2f1ceab8ae9ba47p12ab8cjsnb57b5b47ccd6",
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
}

# Ottenimento dati hotels
response = requests.get(url, headers=headers, params=querystring)
data = response.json()
hotels = data["data"]["data"]

# Preparazione dataset
# Estrazione numero di recensioni e voto medio
hotels_param = []

for hotel in hotels:
	#item = dict(id=hotel['id'], name=hotel['title'].split(' ', 1)[1], ratingCount=hotel['bubbleRating']['count'].replace(',','.'), rating=hotel['bubbleRating']['rating'])
	item = [float(hotel['bubbleRating']['count'].replace(',','')), float(hotel['bubbleRating']['rating'])]
	hotels_param.append(item)

dataset = np.array(hotels_param)

# Scaliamo i dati per una maggiore accuratezza
# I valori di voto e num. recensioni sono molto distanti tra loro
ss = StandardScaler()
dataset_scaled = ss.fit_transform(dataset)

# Numero di cluster
kmeans = KMeans(n_clusters=3, n_init='auto')

# Fit del modello
kmeans.fit(dataset_scaled)

# Predizione cluster
predictions = kmeans.predict(dataset_scaled)

# Centroidi
centroids = kmeans.cluster_centers_

# Stampa risultati
print("Cluster predictions:", predictions)
print("Centroids:", centroids)


# Costruzione grafico 
# Centroidi e cluster
plt.scatter(dataset_scaled[:, 0], dataset_scaled[:, 1], c=predictions)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='r')

plt.xlim(dataset_scaled[:,0].min()-0.5, dataset_scaled[:,0].max()+0.5)
plt.ylim(dataset_scaled[:,1].min()-0.5, dataset_scaled[:,1].max()+0.5)

plt.xlabel(f"Numero recensioni (scalato)")
plt.ylabel("Voto medio (scalato)")

plt.show()