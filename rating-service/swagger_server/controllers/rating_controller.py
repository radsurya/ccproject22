import connexion
import six

from swagger_server import util

from swagger_server.data.movies_data import movies_data
from swagger_server.data.ratings_data import ratings_data


def movies_add_movie_rating(movie_id, critic, user_id, user_trialist=None, user_subscriber=None, user_eligible_for_trial=None):  # noqa: E501
    """Adds a rating to an existing movie

     # noqa: E501

    :param movie_id: Id of the movie
    :type movie_id: str
    :param critic: Critic for a movie
    :type critic: str
    :param user_id: Mubi user id
    :type user_id: str
    :param user_trialist: Is user trialist
    :type user_trialist: bool
    :param user_subscriber: Is user a subscriber
    :type user_subscriber: bool
    :param user_eligible_for_trial: Is user eligible for trial
    :type user_eligible_for_trial: bool

    :rtype: bool
    """

    # Add rating if movie and required params exits
    if movie_id != "" and movie_exists_by_id(movie_id) and critic != "" and user_id != "":
        # TODO Add rating into BD
        return True

    return False


def rating_edit_movie_rating(movie_id, rating_id, user_id, rating_url=None, rating_score=None, critic=None, critic_likes=None, critic_comments=None, user_trialist=None, user_subscriber=None, user_eligible_for_trial=None):  # noqa: E501
    """Updates a rating of an existing movie

     # noqa: E501

    :param movie_id: Id of the movie
    :type movie_id: str
    :param rating_id: Rating id of the movie
    :type rating_id: str
    :param user_id: Mubi user id
    :type user_id: str
    :param rating_url: Url of the rating on the movie
    :type rating_url: str
    :param rating_score: Rating score
    :type rating_score: int
    :param critic: Critic for a movie
    :type critic: str
    :param critic_likes: Number of critic likes on a movie
    :type critic_likes: int
    :param critic_comments: Number of critic comments on a movie
    :type critic_comments: int
    :param user_trialist: Is user trialist
    :type user_trialist: bool
    :param user_subscriber: Is user a subscriber
    :type user_subscriber: bool
    :param user_eligible_for_trial: Is user eligible for trial
    :type user_eligible_for_trial: bool

    :rtype: bool
    """
    
    # Edit rating if movie and rating exists
    if movie_id != "" and movie_exists_by_id(movie_id) and rating_exists_by_id(rating_id):
        # TODO Edit/Save rating into BD
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

def rating_exists_by_id(rating_id):
    """
    Check if rating exists by given id
    Return True if exists, False otherwise.
    """
    for r in ratings_data:
        if r['rating_id'] == rating_id:
            return True
    return False