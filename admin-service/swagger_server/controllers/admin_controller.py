import connexion
import six

from swagger_server import util

from swagger_server.data.movies_data import movies_data


def admin_add_movie(movie_title, movie_title_language, movie_image_url=None, director_id=None, director_name=None, director_url=None):  # noqa: E501
    """Add a new movie information

     # noqa: E501

    :param movie_title: Title of the movie
    :type movie_title: str
    :param movie_title_language: Language of title of the movie
    :type movie_title_language: str
    :param movie_image_url: Image url of the movie
    :type movie_image_url: str
    :param director_id: Title of the movie
    :type director_id: str
    :param director_name: Title of the movie
    :type director_name: str
    :param director_url: Director url
    :type director_url: str

    :rtype: bool
    """

    if movie_title != "":
        movie_exists = movie_exists_by_title(movie_title)
        if not movie_exists:
            # TODO Add movie into DB
            return True

    return False


def admin_delete_movie(movie_id):  # noqa: E501
    """Deleting an existing movie data

     # noqa: E501

    :param movie_id: ID related to the movie on Mubi
    :type movie_id: str

    :rtype: bool
    """

    if movie_id != "":
        movie_exists = movie_exists_by_id(movie_id)
        if movie_exists:
            # TODO Delete movie from DB
            return True

    return False


def movie_exists_by_title(movie_title):
    """
    Check if movie exists by given title
    Return True if exists, False otherwise.
    """
    for movie in movies_data:
        if movie['movie_title'] == movie_title:
            return True
    return False


def movie_exists_by_id(movie_id):
    """
    Check if movie exists by given id
    Return True if exists, False otherwise.
    """
    for movie in movies_data:
        if movie['movie_id'] == movie_id:
            return True
    return False
