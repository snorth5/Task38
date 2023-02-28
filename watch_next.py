import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

#Building movie list from text file
movie_list=[]
with open('movies.txt','r') as f:
    for line in f:
        list_items = line.split(' :')
        list_items[0]=list_items[0].strip()
        list_items[1]=list_items[1].strip()
        movie_list.append(list_items)

# Sentence to compare
planet_hulk = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

model_sentence = nlp(planet_hulk)

# For each movie in list, calculating similarity for it's first element (movie description) to the model sentence.
# Appending this similarity score to a new 3rd element [2] for each movie in the list.
for movie in movie_list:
    similarity = nlp(movie[1]).similarity(model_sentence)
    movie.append(similarity)

# Sorting the list of movies by their similarity scores (element [2])
movie_list.sort(key=lambda x: x[2], reverse=True)

# Print out the label of the most similar movie:
print(f"The user should watch {movie_list[0][0]} next as it is considered the most similar.")