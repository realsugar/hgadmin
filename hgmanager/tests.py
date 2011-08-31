import unittest
import os
from developers_parser import DevelopersParser
from developers_writer import DevelopersWriter
from projects_parser import ProjectsParser
from models import Developer
import settings

# Fixtures
PASSWORDS = "passwords"
HGRC = "hgrc"


def fixture_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures/').replace('\\','/')


class DevelopersParserTest(unittest.TestCase):

    def test_parse_developers(self):
        developers = DevelopersParser.parse_developers(fixture_path() + PASSWORDS)
        self.assertEquals(2, len(developers))
        self.assertEqual('realsugar', developers[0])
        self.assertEqual('magadan', developers[1])


class DevelopersWriterTest(unittest.TestCase):
    def setUp(self):
        self.developer = Developer()
        self.developer.set_login('realsugar')
        self.developer.set_password('A1aaaaa')

    def test_htpasswd_update_command(self):
        command = DevelopersWriter.htpasswd_update_command(self.developer)
        expected = 'htpasswd -b ' + settings.PASSWORDS_PATH + ' realsugar A1aaaaa'
        self.assertEqual(expected, command)

    def test_htpasswd_delete_command(self):
        command = DevelopersWriter.htpasswd_delete_command(self.developer)
        expected = 'htpasswd -D ' + settings.PASSWORDS_PATH + ' realsugar'
        self.assertEqual(expected, command)


class ProjectsParserTest(unittest.TestCase):
    def setUp(self):
        self.file = open(fixture_path() + HGRC, 'r')
        self.lines =  self.file.readlines()
        self.file.close()
        self.dictionary = ProjectsParser.parse_lines(self.lines)

    def test_parse_contact(self):
        self.assertEqual('Anton Sakharov', self.dictionary.get('contact'))

    def test_parse_description(self):
        self.assertEqual('HGM - Mercurial Web Management Application', self.dictionary.get('description'))

    def test_parse_readers(self):
        readers = ProjectsParser.parse_developers(self.dictionary, 'allow_read')
        self.assertTrue('realsugar' in readers)

    def test_parse_pushers(self):
        pushers = ProjectsParser.parse_developers(self.dictionary, 'allow_push')
        self.assertTrue('magadan' in pushers)
        self.assertTrue('realsugar' in pushers)
        

class ProjectsWriterTest(unittest.TestCase):
    pass


class ProjectTest(unittest.TestCase):
    pass

