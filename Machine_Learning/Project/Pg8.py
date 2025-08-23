set1 = {"Inception", "Interstellar", "The Dark Knight", "Parasite", "Joker"}

set2 = {"Parasite", "Joker", "Avengers", "Titanic", "The Matrix"}

common_movies = set1.intersection(set2)

unique_to_A = set1.difference(set2)

suggested_for_A = set2.difference(set1)

print("Movies both have watched:", common_movies)
print("Movies unique to User A:", unique_to_A)
print("Suggested movies for User A:", suggested_for_A)
