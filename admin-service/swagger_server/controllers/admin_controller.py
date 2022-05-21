import connexion
import six
import random
import string

from swagger_server import util

from swagger_server.data.movies_data import movies_data

import mysql.connector
from mysql.connector import Error


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



    letters = string.ascii_letters+string.digits
    movie_id=''.join(random.choice(letters) for i in range(10))
    
    val = (movie_id,movie_title, movie_title_language, movie_image_url, director_id, director_name, director_url)
    query_insert="INSERT INTO movie (movie_id, movie_title, movie_title_language, movie_image_url, director_id, director_name, director_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    result=db_access(query=query_insert,params=val)

    query_get_inserted_id='SELECT movie_id FROM movie WHERE movie_id=\'{}\';'.format(movie_id)
    result=db_access(query=query_get_inserted_id)
    return result

    '''
    if movie_title != "":
        movie_exists = movie_exists_by_title(movie_title)
        if not movie_exists:
            # TODO Add movie into DB
            return True
    '''

    return False


def admin_delete_movie(movie_id):  # noqa: E501
    """Deleting an existing movie data

     # noqa: E501

    :param movie_id: ID related to the movie on Mubi
    :type movie_id: str

    :rtype: bool
    """

    query='DELETE FROM movie WHERE movie_id = \'{}\';'.format(movie_id)
    result=db_access(query=query)
    return result

    '''
    if movie_id != "":
        movie_exists = movie_exists_by_id(movie_id)
        if movie_exists:
            # TODO Delete movie from DB
            return True

    return False
    '''

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



def db_access(query='select database();', params=None):  
    try:
        connection = mysql.connector.connect(host='mysql',
                                            database='mubi_data',
                                            user='user',
                                            password='user')                                  
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(query,params=params)
            result = [dict((cursor.description[i][0], value) 
                            for i, value in enumerate(row)) 
                            for row in cursor.fetchall()]
            connection.commit()

    except Error as e:
        result=str(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            return result