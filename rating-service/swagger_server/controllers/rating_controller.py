import connexion
import six
import random
import string

from swagger_server import util

from swagger_server.data.movies_data import movies_data
from swagger_server.data.ratings_data import ratings_data

import mysql.connector
from mysql.connector import Error


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

    query='SELECT * FROM movie WHERE movie_id=\'{}\';'.format(movie_id)
    result=db_access(query=query)

    if result == []:
        return 'Movie not in database'
    else:
        numbers = string.digits
        user_id='user_'+''.join([random.choice(numbers) for i in range(10)])

        letters = string.ascii_letters+string.digits
        rating_id=''.join(random.choice(letters) for i in range(10))

        val = (movie_id, rating_id, critic, user_id, user_trialist, user_subscriber, user_eligible_for_trial)
        query_insert='INSERT INTO rating (movie_id, rating_id, critic, user_id, user_trialist, user_subscriber, user_eligible_for_trial) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        result=db_access(query=query_insert,params=val)

        query_get_inserted_id='SELECT rating_id FROM rating WHERE rating_id=\'{}\';'.format(rating_id)
        result=db_access(query=query_get_inserted_id)
        return result



    '''
    # Add rating if movie and required params exits
    if movie_id != "" and movie_exists_by_id(movie_id) and critic != "" and user_id != "":
        # TODO Add rating into BD
        return True

    return False
    '''


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
        
    dict_val={
        'rating_url':rating_url,
        'rating_score':rating_score,
        'critic':critic,
        'critic_likes':critic_likes,
        'critic_comments':critic_comments,
        'user_trialist':user_trialist,
        'user_subscriber':user_subscriber,
        'user_eligible_for_trial':user_eligible_for_trial,
    }

    val=[]
    query='UPDATE rating SET '
    for key,value in dict_val.items():
        if value != None:
            query=query+'{}=%s, '.format(key)
            val.append(value)
    # deleting last comma
    query = query[:-2] + ' '
    query=query+'WHERE rating_id=%s'
    val.append(rating_id)
    val=tuple(val)
    
    result=db_access(query=query, params=val)
    return result

    '''
    # Edit rating if movie and rating exists
    if movie_id != "" and movie_exists_by_id(movie_id) and rating_exists_by_id(rating_id):
        # TODO Edit/Save rating into BD
        return True
    return False
    '''

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


def db_access(query='select database();', params=None):  
    try:
        connection = mysql.connector.connect(host='database',
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