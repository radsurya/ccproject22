# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestRatingController(BaseTestCase):
    """RatingController integration test stubs"""

    def test_movies_add_movie_rating(self):
        """Test case for movies_add_movie_rating

        Adds a rating to an existing movie
        """
        query_string = [('movie_id', 'movie_id_example'),
                        ('critic', 'critic_example'),
                        ('user_id', 'user_id_example'),
                        ('user_trialist', true),
                        ('user_subscriber', true),
                        ('user_eligible_for_trial', true)]
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/rating/add_movie_rating',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rating_edit_movie_rating(self):
        """Test case for rating_edit_movie_rating

        Updates a rating of an existing movie
        """
        query_string = [('movie_id', 'movie_id_example'),
                        ('rating_id', 'rating_id_example'),
                        ('rating_url', 'rating_url_example'),
                        ('rating_score', 56),
                        ('critic', 'critic_example'),
                        ('critic_likes', 56),
                        ('critic_comments', 56),
                        ('user_id', 'user_id_example'),
                        ('user_trialist', true),
                        ('user_subscriber', true),
                        ('user_eligible_for_trial', true)]
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/rating/edit_movie_rating',
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
