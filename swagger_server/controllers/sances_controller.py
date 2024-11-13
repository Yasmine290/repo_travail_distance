import connexion
import six

from swagger_server import util


def courses_course_id_sessions_get(courseId):  # noqa: E501
    "get": {
          "summary": "Obtenir les séances d'un cours",
          "tags": [
            "Séances"
          ]
    }

     # noqa: E501

    :param courseId: 
    :type courseId: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        courseId = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def courses_course_id_sessions_post(courseId):  # noqa: E501
    "post": {
          "summary": "Créer une nouvelle séance pour un cours",
          "tags": [
            "Séances"
          ]
          }

     # noqa: E501

    :param courseId: 
    :type courseId: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        courseId = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def courses_course_id_sessions_session_id_put(courseId, sessionId):  # noqa: E501
    "put": {
          "summary": "Mettre à jour une séance",
          "tags": [
            "Séances"
          ]
    }

     # noqa: E501

    :param courseId: 
    :type courseId: dict | bytes
    :param sessionId: 
    :type sessionId: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        courseId = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        sessionId = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
