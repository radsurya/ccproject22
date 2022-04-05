import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util

from swagger_server.data.movies_data import movies_data
from flask import make_response, abort

def admin_add_movie(movie):  # noqa: E501
    """Add a new movie information

     # noqa: E501

    :param movie: Movie data to be added
    :type movie: dict | bytes

    :rtype: bool
    """
    
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())

    movie_title = movie.get("movie_title", None)

    # Does the movie exist already?
    exists=_check_if_exists(movie_title)
    if not exists:
        # movies_data.append(movie)
        return True, 200

    # Otherwise, they exist, that's an error
    else:
        # Not sure about if we need the abort but it is used in tutorial
        # abort(400,False)
        return False,400
    return True


def admin_delete_movie(movie_id):  # noqa: E501
    """Deleting an existing movie data

     # noqa: E501

    :param movie_id: ID related to the movie on Mubi
    :type movie_id: str

    :rtype: bool
    """

    movie_found = False
    for movie in movies_data:
        if movie['movie_id'] == movie_id:
            movie_found = True
            #TODO Delete in DB
            return movie_found,202

    return movie_found,204


def _get_movie_idx(movie_id):
    '''
    Find movie index
    '''
    for idx,movie in enumerate(movies_data):
        if movie['movie_id']==movie_id:
            return idx


def _check_if_exists(movie_title):
    '''
    If movie is in db return True
    '''
    exists=False
    for movie in movies_data:
        if movie['movie_title']==movie_title:
            exists=True
    return exists


'''
if __name__=='__main__':
    movie={
        "average_rating": 10,
        "director_id": "11337",
        "director_name": "J.K. Rowling",
        "director_url": "http://mubi.com/cast/jkowling",
        "movie_id": "4",
        "movie_image_url": "https://images.mubicdn.net/images/film/1066/cache-8564-1481540828/image-w1280.jpg",
        "movie_popularity": 5,
        "movie_release_year": 2005,
        "movie_title": "Harry Potter 1",
        "movie_title_language": "en",
        "movie_url": "http://mubi.com/films/rowlig-harry-potter-1"
    }

    response0,response1=admin_add_movie(movie)

    print(response0)
    print(response1)
'''

