import os

movie = {}
client = {}
rent = {}

def new_movie():
	print (	' Create a new Movie' )
	id = input ("ID: ")
	type = input("Type: ")
	name = input ("Name: ")
	release_date = input ("Release Date: ")

	movie[id] = [type, name, release_date]

def list_movies():
	for id, content in client.items():
		print ("\nID: " + id +  "\nType: " + content[0] + "\nName: " + content[1] + "\nRelease Date: " + content[2])

def new_client():
	print (	' Create a new Client' )
	id = input ("ID: ")
	name = input ("Name: ")
	phone = input ("Phone Number: ")

	client[id] = [name, phone]

def list_clients():
	for id, content in movie.items():
		print ("\nID: " + id +  "\nName: " + content[0] + "\nPhone Number: " + content[1])

def rent():
	print (	' Create a new Rent' )
	id = input ("ID: ")
	client = input ("Client ID: ")
	movie = input ("Movie ID: ")

	rent[id] = [client, movie]

def list_rents():
	for id, content in rent.items():
		print ("\nID: " + id +  "\nClient: " + content[0] + "\nMovie: " + content[1])


on = True
while on == True:
	print (" Pick 1 if you wanna create a new Movie\n Pick 2 if you wanna create a new Client\n Pick 3 if you wanna create e new Rent\n Pick 4 if you wanna list the movies\n Pick 5 if you wanna list the clients\n Pick 6 if you wanna list the rents\n Pick 7 if you wanna leave\n")
	option = int(input('Pick a number from 1 to 7:'))

	match option:
		case 1:
			new_movie()
		case 2:
			new_client()
		case 3:
			rent()
		case 4:
			list_movies()
		case 5:
			list_clients()
		case 6:
			list_rents()
		case 7:
			on = False
