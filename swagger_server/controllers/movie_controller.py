import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util

from swagger_server.data.movies_data import movies_data

def movie_get_by_id(movie_id):  # noqa: E501
    """Get movie information by given movie id

     # noqa: E501

    :param movie_id: Id of the movie
    :type movie_id: str

    :rtype: Movie
    """

    movie_found = False
    for movie in movies_data:
        if movie["movie_id"] == movie_id:
            movie_found = movie

    return movie_found


def movies_search(keyword=None, limit=None):  # noqa: E501
    """Search for movies by given search parameters

     # noqa: E501

    :param keyword: Keyword that should be looked up in movie titles
    :type keyword: str
    :param limit: Number of movies to return
    :type limit: int

    :rtype: List[Movie]
    """
    return 'do some magic!'
