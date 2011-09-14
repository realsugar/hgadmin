import unittest2 as unittest
from projects.projects_parser import ProjectsParser
import settings


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
