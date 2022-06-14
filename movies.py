import os

movie = {}
client = {}
rents = {}

def new_movie(id, type, name, release_date):
	movie[id] = [type, name, release_date]

def list_movies():
	for id, content in client.items():
		print ("\nID: " + id +  "\nType: " + content[0] + "\nName: " + content[1] + "\nRelease Date: " + content[2])

def new_client(id, name, phone):
	client[id] = [name, phone]

def list_clients():
	for id, content in movie.items():
		print ("\nID: " + id +  "\nName: " + content[0] + "\nPhone Number: " + content[1])

def rent(id, client, movie):
	rents[id] = [client, movie]

def list_rents():
	for id, content in rent.items():
		print ("\nID: " + id +  "\nClient: " + content[0] + "\nMovie: " + content[1])
