import connexion
import six

from swagger_server.models.rating import Rating  # noqa: E501
from swagger_server import util


def movies_add_movie_rating(rating):  # noqa: E501
    """Adds a rating to an existing movie

     # noqa: E501

    :param rating: Rating object data
    :type rating: dict | bytes

    :rtype: bool
    """
    if connexion.request.is_json:
        rating = Rating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def rating_edit_movie_rating(rating):  # noqa: E501
    """Updates a rating of an existing movie

     # noqa: E501

    :param rating: Rating object data
    :type rating: dict | bytes

    :rtype: bool
    """
    if connexion.request.is_json:
        rating = Rating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
