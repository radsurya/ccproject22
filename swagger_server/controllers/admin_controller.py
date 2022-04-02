import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util


def admin_add_movie(movie):  # noqa: E501
    """Add a new movie information

     # noqa: E501

    :param movie: ID related to the movie on Mubi
    :type movie: dict | bytes

    :rtype: bool
    """
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def admin_delete_movie(movie_id):  # noqa: E501
    """Deleting an existing movie data

     # noqa: E501

    :param movie_id: ID related to the movie on Mubi
    :type movie_id: str

    :rtype: bool
    """
    return 'do some magic!'
