from django.contrib import messages
from mock import Mock, patch
import unittest2 as unittest
from projects.models import Project
from projects.projects_parser import ProjectsParser
import settings
from views import *

# Fixtures
HGRC = "hgrc"


class ProjectsParserTest(unittest.TestCase):
    def setUp(self):
        self.file = open(settings.FIXTURE_PATH + HGRC, 'r')
        self.lines =  self.file.readlines()
        self.file.close()
        self.dictionary = ProjectsParser.parse_lines(self.lines)

    def test_parse_contact(self):
        self.assertEqual('Anton Sakharov', self.dictionary.get('contact'))

    def test_parse_description(self):
        self.assertEqual('HGM - Mercurial Web Management Application', self.dictionary.get('description'))

    def test_parse_readers(self):
        readers = ProjectsParser.parse_list(self.dictionary, 'allow_read')
        self.assertTrue('realsugar' in readers)

    def test_parse_pushers(self):
        pushers = ProjectsParser.parse_list(self.dictionary, 'allow_push')
        self.assertTrue('magadan' in pushers)
        self.assertTrue('realsugar' in pushers)


class ProjectsWriterTest(unittest.TestCase):
    pass


class ProjectTest(unittest.TestCase):
    pass


class ProjectViewTest(unittest.TestCase):
    @patch.object(Project, 'all')
    def test_project_list_no_projects_yet(self, all_projects):
        all_projects.return_value = []
        response = projects_list(None)
        all_projects.assert_called_once()

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(-1, response.content.find('No repositories yet.'))

    @patch.object(Project, 'get_by_name')
    def test_project_details_not_found(self, get_by_name):
        get_by_name.return_value = None
        self.assertRaises(Http404, project_details, request=None, name='bitbucket')
        get_by_name.assert_called_once_with('bitbucket')


    @patch.object(messages, 'error')
    def test_developer_delete_not_implemented(self, error_mock):
        request = Mock()
        response = project_delete(request, 'bitbucket')
        error_mock.assert_called_once_with(request, 'This feature is to be implemented.')
        self.assertEqual(200, response.status_code)



