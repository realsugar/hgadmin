import os
from projects_parser import ProjectsParser
import settings


class Project:
    name = None
    full_path = None
    description = None
    contact = None
    allow_archive = []
    allow_push = []
    allow_read = []
    push_ssl = 'false'


    @staticmethod
    def all():
        result = []
        project_dir_list = sorted(os.listdir(settings.REPOS_ROOT))
        for path in project_dir_list:
            full_path = os.path.join(settings.REPOS_ROOT, path)
            if os.path.isdir(full_path) and not path.startswith('.'):
                project = Project()

                project.name = path
                project.full_path = full_path

                attrs = ProjectsParser.parse_project(full_path)
                project.description = attrs.get('description', '')
                project.contact = attrs.get('contact', '')

                project.allow_archive = ProjectsParser.parse_list(attrs, 'allow_archive')
                project.allow_read = ProjectsParser.parse_list(attrs, 'allow_read')
                project.allow_push = ProjectsParser.parse_list(attrs, 'allow_push')

                result.append(project)
                
        return result

    @staticmethod
    def get_by_name(project_name):
        for project in Project.all():
            if project.name == project_name:
                return project
        return None

    def html_allow_archive(self):
        return ', '.join(self.allow_archive)

