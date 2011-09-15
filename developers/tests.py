import re
import unittest2 as unittest
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpRequest
import developers
from developers.validators import developer_exists_validator
from developers_parser import DevelopersParser
from developers_writer import DevelopersWriter
from views import *
import settings
from mock import Mock, sentinel, patch
from forms import DeveloperAddForm

# Fixtures
PASSWORDS = "passwords"


class DevelopersParserTest(unittest.TestCase):
    def test_parse_developers(self):
        developers = DevelopersParser.parse_developers(settings.FIXTURE_PATH + PASSWORDS)
        self.assertEquals(2, len(developers))
        self.assertEqual('realsugar', developers[0])
        self.assertEqual('magadan', developers[1])



class DevelopersWriterTest(unittest.TestCase):
    def setUp(self):
        self.developer = Mock()
        self.developer.login.return_value = 'realsugar'
        self.developer.password.return_value = 'A1aaaaa'

    def test_htpasswd_update_command(self):
        command = DevelopersWriter.htpasswd_update_command(self.developer)
        expected = 'htpasswd -b ' + settings.PASSWORDS_PATH + ' realsugar A1aaaaa'
        self.developer.assert_has_calls([('login',), ('password',)], any_order=True)
        self.assertEqual(expected, command)

    def test_htpasswd_delete_command(self):
        command = DevelopersWriter.htpasswd_delete_command(self.developer)
        expected = 'htpasswd -D ' + settings.PASSWORDS_PATH + ' realsugar'
        self.developer.assert_has_calls([('login',)])
        self.assertEqual(expected, command)

        

class DeveloperValidatorTest(unittest.TestCase):
    @patch.object(Developer, 'get_by_login')
    def test_developer_exists(self, get_by_login):
        get_by_login.return_value = 'realsugar'
        self.assertRaises(ValidationError, developer_exists_validator, 'realsugar')
        get_by_login.assert_called_once_with('realsugar')

    @patch.object(Developer, 'get_by_login')
    def test_developer_does_not_exist(self, get_by_login):
        get_by_login.return_value = None
        self.assertIsNone(developer_exists_validator('valera'))
        get_by_login.assert_called_once_with('valera')


#
# Tests for views
#

class DeveloperViewTest(unittest.TestCase):
    def test_developer_add_GET(self):
        request = Mock()
        request.POST = None
        response = developer_add(request)

        self.assertEqual(200, response.status_code)
        pattern = '<form action="%s" method="post">' % reverse(developer_add)
        self.assertIsNotNone(re.search(pattern, response.content))





