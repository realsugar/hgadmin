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

        realsugar = developers[0]
        self.assertEqual('realsugar', realsugar.login())

        magadan = developers[1]
        self.assertEqual('magadan', magadan.login())


class DevelopersWriterTest(unittest.TestCase):
    def test_htpasswd_command(self):
        developer = Developer()
        developer.set_login('realsugar')
        developer.set_password('A1aaaaa')
        command = DevelopersWriter.htpasswd_command(developer)
        expected = 'htpasswd -b ' + settings.PASSWORDS_PATH + ' realsugar A1aaaaa'
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
