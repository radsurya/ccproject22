# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Rating(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, movie_id: str=None, rating_id: str=None, rating_url: str=None, rating_score: int=None, rating_timestamp_utc: str=None, critic: str=None, critic_likes: int=None, critic_comments: int=None, user_id: str=None, user_trialist: bool=None, user_subscriber: bool=None, user_eligible_for_trial: bool=None):  # noqa: E501
        """Rating - a model defined in Swagger

        :param movie_id: The movie_id of this Rating.  # noqa: E501
        :type movie_id: str
        :param rating_id: The rating_id of this Rating.  # noqa: E501
        :type rating_id: str
        :param rating_url: The rating_url of this Rating.  # noqa: E501
        :type rating_url: str
        :param rating_score: The rating_score of this Rating.  # noqa: E501
        :type rating_score: int
        :param rating_timestamp_utc: The rating_timestamp_utc of this Rating.  # noqa: E501
        :type rating_timestamp_utc: str
        :param critic: The critic of this Rating.  # noqa: E501
        :type critic: str
        :param critic_likes: The critic_likes of this Rating.  # noqa: E501
        :type critic_likes: int
        :param critic_comments: The critic_comments of this Rating.  # noqa: E501
        :type critic_comments: int
        :param user_id: The user_id of this Rating.  # noqa: E501
        :type user_id: str
        :param user_trialist: The user_trialist of this Rating.  # noqa: E501
        :type user_trialist: bool
        :param user_subscriber: The user_subscriber of this Rating.  # noqa: E501
        :type user_subscriber: bool
        :param user_eligible_for_trial: The user_eligible_for_trial of this Rating.  # noqa: E501
        :type user_eligible_for_trial: bool
        """
        self.swagger_types = {
            'movie_id': str,
            'rating_id': str,
            'rating_url': str,
            'rating_score': int,
            'rating_timestamp_utc': str,
            'critic': str,
            'critic_likes': int,
            'critic_comments': int,
            'user_id': str,
            'user_trialist': bool,
            'user_subscriber': bool,
            'user_eligible_for_trial': bool
        }

        self.attribute_map = {
            'movie_id': 'movie_id',
            'rating_id': 'rating_id',
            'rating_url': 'rating_url',
            'rating_score': 'rating_score',
            'rating_timestamp_utc': 'rating_timestamp_utc',
            'critic': 'critic',
            'critic_likes': 'critic_likes',
            'critic_comments': 'critic_comments',
            'user_id': 'user_id',
            'user_trialist': 'user_trialist',
            'user_subscriber': 'user_subscriber',
            'user_eligible_for_trial': 'user_eligible_for_trial'
        }
        self._movie_id = movie_id
        self._rating_id = rating_id
        self._rating_url = rating_url
        self._rating_score = rating_score
        self._rating_timestamp_utc = rating_timestamp_utc
        self._critic = critic
        self._critic_likes = critic_likes
        self._critic_comments = critic_comments
        self._user_id = user_id
        self._user_trialist = user_trialist
        self._user_subscriber = user_subscriber
        self._user_eligible_for_trial = user_eligible_for_trial

    @classmethod
    def from_dict(cls, dikt) -> 'Rating':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The rating of this Rating.  # noqa: E501
        :rtype: Rating
        """
        return util.deserialize_model(dikt, cls)

    @property
    def movie_id(self) -> str:
        """Gets the movie_id of this Rating.


        :return: The movie_id of this Rating.
        :rtype: str
        """
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id: str):
        """Sets the movie_id of this Rating.


        :param movie_id: The movie_id of this Rating.
        :type movie_id: str
        """

        self._movie_id = movie_id

    @property
    def rating_id(self) -> str:
        """Gets the rating_id of this Rating.


        :return: The rating_id of this Rating.
        :rtype: str
        """
        return self._rating_id

    @rating_id.setter
    def rating_id(self, rating_id: str):
        """Sets the rating_id of this Rating.


        :param rating_id: The rating_id of this Rating.
        :type rating_id: str
        """

        self._rating_id = rating_id

    @property
    def rating_url(self) -> str:
        """Gets the rating_url of this Rating.


        :return: The rating_url of this Rating.
        :rtype: str
        """
        return self._rating_url

    @rating_url.setter
    def rating_url(self, rating_url: str):
        """Sets the rating_url of this Rating.


        :param rating_url: The rating_url of this Rating.
        :type rating_url: str
        """

        self._rating_url = rating_url

    @property
    def rating_score(self) -> int:
        """Gets the rating_score of this Rating.


        :return: The rating_score of this Rating.
        :rtype: int
        """
        return self._rating_score

    @rating_score.setter
    def rating_score(self, rating_score: int):
        """Sets the rating_score of this Rating.


        :param rating_score: The rating_score of this Rating.
        :type rating_score: int
        """

        self._rating_score = rating_score

    @property
    def rating_timestamp_utc(self) -> str:
        """Gets the rating_timestamp_utc of this Rating.


        :return: The rating_timestamp_utc of this Rating.
        :rtype: str
        """
        return self._rating_timestamp_utc

    @rating_timestamp_utc.setter
    def rating_timestamp_utc(self, rating_timestamp_utc: str):
        """Sets the rating_timestamp_utc of this Rating.


        :param rating_timestamp_utc: The rating_timestamp_utc of this Rating.
        :type rating_timestamp_utc: str
        """

        self._rating_timestamp_utc = rating_timestamp_utc

    @property
    def critic(self) -> str:
        """Gets the critic of this Rating.


        :return: The critic of this Rating.
        :rtype: str
        """
        return self._critic

    @critic.setter
    def critic(self, critic: str):
        """Sets the critic of this Rating.


        :param critic: The critic of this Rating.
        :type critic: str
        """

        self._critic = critic

    @property
    def critic_likes(self) -> int:
        """Gets the critic_likes of this Rating.


        :return: The critic_likes of this Rating.
        :rtype: int
        """
        return self._critic_likes

    @critic_likes.setter
    def critic_likes(self, critic_likes: int):
        """Sets the critic_likes of this Rating.


        :param critic_likes: The critic_likes of this Rating.
        :type critic_likes: int
        """

        self._critic_likes = critic_likes

    @property
    def critic_comments(self) -> int:
        """Gets the critic_comments of this Rating.


        :return: The critic_comments of this Rating.
        :rtype: int
        """
        return self._critic_comments

    @critic_comments.setter
    def critic_comments(self, critic_comments: int):
        """Sets the critic_comments of this Rating.


        :param critic_comments: The critic_comments of this Rating.
        :type critic_comments: int
        """

        self._critic_comments = critic_comments

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Rating.


        :return: The user_id of this Rating.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Rating.


        :param user_id: The user_id of this Rating.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def user_trialist(self) -> bool:
        """Gets the user_trialist of this Rating.


        :return: The user_trialist of this Rating.
        :rtype: bool
        """
        return self._user_trialist

    @user_trialist.setter
    def user_trialist(self, user_trialist: bool):
        """Sets the user_trialist of this Rating.


        :param user_trialist: The user_trialist of this Rating.
        :type user_trialist: bool
        """

        self._user_trialist = user_trialist

    @property
    def user_subscriber(self) -> bool:
        """Gets the user_subscriber of this Rating.


        :return: The user_subscriber of this Rating.
        :rtype: bool
        """
        return self._user_subscriber

    @user_subscriber.setter
    def user_subscriber(self, user_subscriber: bool):
        """Sets the user_subscriber of this Rating.


        :param user_subscriber: The user_subscriber of this Rating.
        :type user_subscriber: bool
        """

        self._user_subscriber = user_subscriber

    @property
    def user_eligible_for_trial(self) -> bool:
        """Gets the user_eligible_for_trial of this Rating.


        :return: The user_eligible_for_trial of this Rating.
        :rtype: bool
        """
        return self._user_eligible_for_trial

    @user_eligible_for_trial.setter
    def user_eligible_for_trial(self, user_eligible_for_trial: bool):
        """Sets the user_eligible_for_trial of this Rating.


        :param user_eligible_for_trial: The user_eligible_for_trial of this Rating.
        :type user_eligible_for_trial: bool
        """

        self._user_eligible_for_trial = user_eligible_for_trial
