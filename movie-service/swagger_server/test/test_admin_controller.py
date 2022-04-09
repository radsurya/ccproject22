# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_admin_add_movie(self):
        """Test case for admin_add_movie

        Add a new movie information
        """
        query_string = [('movie_title', 'movie_title_example'),
                        ('movie_title_language', 'movie_title_language_example'),
                        ('movie_image_url', 'movie_image_url_example'),
                        ('director_id', 'director_id_example'),
                        ('director_name', 'director_name_example'),
                        ('director_url', 'director_url_example')]
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/admin/add_movie',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_admin_delete_movie(self):
        """Test case for admin_delete_movie

        Deleting an existing movie data
        """
        response = self.client.open(
            '/fc44311/ccproject22/1.0.0/admin/delete_movie/{movie_id}'.format(movie_id='movie_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
