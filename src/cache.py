from movie import *
from beer import *
import redis

# Opening a Connection to Redis
cache = redis.Redis(
    host='',
    port=0
    )


# Return the output if the input is found in the database
# Return None otherwise
def in_cache(key):
    value = cache.get(key)
    return value


# Add a new set of input/output to the database
# Default expire time of 24hr
def cache_set(key, value, expire=86400):
    cache.set(key, value)
    cache.expire(key, expire)


# Make calls to the APIs
def api_query(movie_name):
    try:
        movie = five_rec(movie_name)
        beer = get_beer()
        return (movie + " --> " + beer)
    except:
        return "Movie not found!"


# Return the input if it is found in the database
# If not, query the APIs and add the results to the
# database and return the querried results
def process_input(movie_name):
    cached = in_cache(movie_name)
    if not cached:
        output = api_query(movie_name)
        cache_set(movie_name, output)
        return output
    else:
        time_left = cache.ttl(movie_name)
        return "({}) {}".format(time_left, cached.decode('utf-8'))

