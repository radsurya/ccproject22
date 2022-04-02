# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMovieController(BaseTestCase):
    """MovieController integration test stubs"""

    def test_movie_get_by_id(self):
        """Test case for movie_get_by_id

        Get movie information by given movie id
        """
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/movie/get_by_id/{movie_id}'.format(movie_id='movie_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_movies_search(self):
        """Test case for movies_search

        Search for movies by given search parameters
        """
        query_string = [('keyword', 'keyword_example'),
                        ('limit', 56)]
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/movies/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
