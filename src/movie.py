from tmdbv3api import Movie
from tmdbv3api import TMDb

tmdb = TMDb()
tmdb.api_key = '' #removed

movie = Movie()

def closest_name(name, count=1):
    lst = movie.search(name)
    ret = []
    for x in range(count):
        ret.append((lst[x].title, lst[x].id))
    return ret

def five_rec(name):
    ext = closest_name(name)[0]
    rec = movie.recommendations(movie_id=ext[1])
    return "Recommendations for movie <{}>: {}.".format(ext[0].upper(), ''.join([x+', ' for x in [x.title for x in rec[:5]]])[:-2])
