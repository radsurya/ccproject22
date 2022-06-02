# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase

import requests






'''
URL = "http://localhost:8081/fc44311/ccproject22/1.0.0/movie/get_by_id/"
movie_id = "1"
PARAMS = {'movie_id':movie_id}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
'''

class TestMovieController(BaseTestCase):
    """MovieController integration test stubs"""

    def __init__(self,*args, **kwargs):#self,**kwargs
        super(BaseTestCase, self).__init__(*args,**kwargs)
        self.valid_id='1'
        self.invalid_id='-1'
        self.search_term='the'
        self.limit='5'
        self.invalid_limit='-1'
        self.unfindable_keyword='string that no tittle will contain'
        self.keyword='the'

    def test_movie_get_by_id_valid_id(self):
        url = "http://localhost:8081/fc44311/ccproject22/1.0.0/movie/get_by_id/"
        url=url+'{}'.format(self.valid_id)
        response = requests.get(url = url)
        self.assert200(response,'Response body is : {}'.format(response.json()))

        response = response.json()
        movie_id_reponse=response[0]['movie_id']
        self.assertEqual(movie_id_reponse, self.valid_id, "Did not find the correct record")
    
    def test_movie_get_by_id_invalid_id(self):
        url = "http://localhost:8081/fc44311/ccproject22/1.0.0/movie/get_by_id/"
        url=url+'{}'.format(self.invalid_id)
        response = requests.get(url = url)
        self.assert200(response,'Response body is : {}'.format(response.json()))
        response = response.json()     
        self.assertEqual(response, [], "Unintended output")
    

    def test_movie_search_valid_keyword(self):
        url = "http://localhost:8081/fc44311/ccproject22/1.0.0/movies/search?keyword={}&limit={}"
        url=url.format(self.keyword, self.limit)
        response = requests.get(url = url)

        # Check that the response code is 200
        self.assert200(response,'Response body is : {}'.format(response.json()))

        response = response.json()
        response_length=len(response)
        # Check that no more than limit results were returned
        self.assertLessEqual(response_length, int(self.limit), 
            'Limit of results was succeeded: {} > {}'.format(response_length, self.limit))
        
        # Check that all results contain the keyword
        keyword_in_all_responses=True
        for r in response:
            if not self.keyword in r['movie_title']:
                keyword_in_all_responses=False
        
        self.assertEqual(keyword_in_all_responses, False, "Keyword was not found in all results.")
    
    def test_movie_search_unfindable_keyword(self):
        url = "http://localhost:8081/fc44311/ccproject22/1.0.0/movies/search?keyword={}&limit={}"
        url=url.format(self.unfindable_keyword, self.limit)
        response = requests.get(url = url)

        # Check that the response code is 200
        self.assert200(response,'Response body is : {}'.format(response.json()))

        response = response.json()
        self.assertEqual(response, [], "Unintended output")
    
    '''
     # throws error
    def test_movie_search_invalid_limit(self):
        url = "http://localhost:8081/fc44311/ccproject22/1.0.0/movies/search?keyword={}&limit={}"
        url=url.format(self.unfindable_keyword, self.limit)
        response = requests.get(url = url)
        #response = response.json()
        self.assertEqual(response, 400, "Wrong error code")
    '''                               


if __name__ == '__main__':
    import unittest
    unittest.main()
