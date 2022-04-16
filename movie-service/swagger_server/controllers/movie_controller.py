import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util

from swagger_server.data.movies_data import movies_data

import mysql.connector
from mysql.connector import Error


def movie_get_by_id(movie_id):  # noqa: E501
    """Get movie information by given movie id

     # noqa: E501

    :param movie_id: Id of the movie
    :type movie_id: str

    :rtype: Movie
    """
    query='''SELECT * FROM movie WHERE movie_id={};'''.format(movie_id)
    result=db_access(query=query)
    return result
     
    '''
    if movie_id != "":
        for movie in movies_data:
            if movie["movie_id"] == movie_id:
                return movie

    return False
    '''

def movies_search(keyword="", limit=None):  # noqa: E501
    """Search for movies by given search parameters

     # noqa: E501

    :param keyword: Keyword that should be looked up in movie titles
    :type keyword: str
    :param limit: Number of movies to return
    :type limit: int

    :rtype: List[Movie]
    """

    query='''SELECT * FROM movie WHERE movie_title LIKE \'{}\' LIMIT {};'''.format('%' + keyword + '%', limit)
    result=db_access(query=query)
    return result

    '''
    movies = []

    if keyword != "" and limit != None:
        for movie in movies_data:
            if keyword in movie["movie_title"] and len(movies) < limit:
                movies.append(movie)

    return movies
    '''


def db_access(query='select database();'):  
    try:
        connection = mysql.connector.connect(host='database',
                                            database='mubi_data',
                                            user='user',
                                            password='user')                                  
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query)
            result = [dict((cursor.description[i][0], value) 
                            for i, value in enumerate(row)) 
                            for row in cursor.fetchall()]

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return result