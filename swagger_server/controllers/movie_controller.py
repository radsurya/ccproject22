import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util


def movie_get_by_id(movie_id):  # noqa: E501
    """Get movie information by given movie id

     # noqa: E501

    :param movie_id: Id of the movie
    :type movie_id: str

    :rtype: Movie
    """
    return 'do some magic!'


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
