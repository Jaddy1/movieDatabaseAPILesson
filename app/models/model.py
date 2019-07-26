from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '166d285b00c7c31afd5fc98b33fec846'

from tmdbv3api import Movie

movie = Movie()

def userSearch(movieName):
    search = movie.search(movieName)
    # for res in search:
    #     print(res.id)
    #     print(res.title)
    #     print(res.overview)
    #     print(res.poster_path)
    return search[2].title
    
    
# userSearch('The Avengers')