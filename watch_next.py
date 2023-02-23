# Import spacy module to compute similarity
import spacy

# Load md model to
nlp = spacy.load('en_core_web_md')


# Create function with description as the parameter
def find_most_similar_movie(description):
    # Initialise variable as empty to keep track of the movie with the highest similarity
    most_similar_movie = ""
    # Initialise as 0 to find the movie with the highest similarity score
    max_similarity = 0
    with open('movies.txt', 'r') as file:
        for line in file:
            movie_info = line.strip().split(':')
            curr_movie_title = movie_info[0].strip()
            curr_movie_description = movie_info[1].strip()
            # compute similarity between curr_movie_description and description
            similarity = nlp(description).similarity(nlp(curr_movie_description))
            # If similarity is more than the current max similarity,
            if similarity > max_similarity:
                most_similar_movie = curr_movie_title
                # then new max similarity is similarity
                max_similarity = similarity
    return most_similar_movie


# Variable to contain string of movie description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live " \
              "in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator."

# call the function
similar_movie = find_most_similar_movie(description)

print("Recommended watch:", similar_movie)
