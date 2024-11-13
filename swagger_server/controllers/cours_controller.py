import connexion
import six

from swagger_server import util


def courses_course_id_delete(courseId):  # noqa: E501
  "delete": {
          "summary": "Supprimer un cours",
          "tags": [
            "Cours"
          ]
  }
    return 'do some magic!'


def courses_course_id_get(courseId):  # noqa: E501
  "get": {
          "summary": "Obtenir un cours spécifique",
          "tags": [
            "Cours"
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


def courses_course_id_put(courseId):  # noqa: E501
  "put": {
          "summary": "Mettre à jour un cours",
          "tags": [
            "Cours"
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


def courses_get():  # noqa: E501
  "get": {
          "summary": "Obtenir la liste des cours",
          "tags": [
            "Cours"
          ]
  }
  

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def courses_post():  # noqa: E501
"post": {
          "summary": "Créer un nouveau cours",
          "tags": [
            "Cours"
          ]
          }
     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
