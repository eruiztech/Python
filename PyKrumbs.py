#!/usr/bin/python

from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
import urllib.request, json, time

# Create ElasticSearch object to connect to database
es = Elasticsearch()
# Create a movies index with give structure by 'body={}'
es.indices.create(index="movies", body={"mappings": {"movie": {"properties": {"title": {"type": "text"}, "rating": {"type": "double"}}}}}, ignore=400)

# Url to crawl
url = 'http://www.ondvdreleases.com/'

page = urllib.request.urlopen(url)
# Create a BeautifulSoup object to allow parsing of html
soup = BeautifulSoup(page.read(), "html.parser")
# Match all <a> elements with the class attribute = 'tit'
matches = soup.findAll('a', attrs={'class':'tit'})

for m in matches:
    if m.text.strip() != "":
        # Query API for more data
        api = "http://www.omdbapi.com/?t=" + m.text + "&y=&plot=short&r=json&tomatoes=true"
        # Format the api url to replace space with %20, for compatibility
        api = api.replace(" ", "%20")

        # Open the web page with the specified client
        req = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)

        # Decoded the response and parse to JSON
        data = json.loads(response.read().decode('utf-8'))

        # Create ElasitcSearch document in the database, ignore 409 errors when the document exists
        es.create(index="movies", doc_type="movie", id=data['imdbID'], body={'title': data['Title'], 'rating': float(data['imdbRating']), "Genre": [item.strip() for item in data['Genre'].split(',')], "Hi" : "world"}, ignore=409)
