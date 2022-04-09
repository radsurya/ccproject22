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

    if movie_id != "":
        for movie in movies_data:
            if movie["movie_id"] == movie_id:
                return movie

    return False


def movies_search(keyword="", limit=None):  # noqa: E501
    """Search for movies by given search parameters

     # noqa: E501

    :param keyword: Keyword that should be looked up in movie titles
    :type keyword: str
    :param limit: Number of movies to return
    :type limit: int

    :rtype: List[Movie]
    """

    movies = []

    if keyword != "" and limit != None:
        for movie in movies_data:
            if keyword in movie["movie_title"] and len(movies) < limit:
                movies.append(movie)

    return movies
