# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSancesController(BaseTestCase):
    """SancesController integration test stubs"""

    def test_courses_course_id_sessions_get(self):
        """Test case for courses_course_id_sessions_get

        Obtenir les séances d'un cours
        """
        response = self.client.open(
            '/courses/{courseId}/sessions'.format(courseId=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_course_id_sessions_post(self):
        """Test case for courses_course_id_sessions_post

        Créer une nouvelle séance pour un cours
        """
        response = self.client.open(
            '/courses/{courseId}/sessions'.format(courseId=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_course_id_sessions_session_id_put(self):
        """Test case for courses_course_id_sessions_session_id_put

        Mettre à jour une séance
        """
        response = self.client.open(
            '/courses/{courseId}/sessions/{sessionId}'.format(courseId=None, sessionId=None),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
