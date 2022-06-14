import movies

def test_create_new_movie():
	id = "001"
	type = "DVD"
	name = "Legends of Fei"
	date = "2021"
	
	movies.new_movie(id, type, name, date)

	assert movies.movie[id] == [type, name, date]

def test_create_new_client():
	id = "001"
	name = "Legends of Fei"
	phone = "31 9586 0236"
	
	movies.new_client(id, name, phone)

	assert movies.client[id] == [name, phone]

def test_create_new_rent():
	id = "001"
	client = "001"
	movie = "001"
	
	movies.rent(id, client, movie)

	assert movies.rents[id] == [client, movie]