import os
import projects
import settings


class Project:
    name = None

    @staticmethod
    def all():
        result = []
        for path in os.listdir(settings.REPOS_ROOT):
            full_path = os.path.join(settings.REPOS_ROOT, path)
            if os.path.isdir(full_path) and not path.startswith('.'):
                project = Project()
                project.name = path
                result.append(project)
                
        return result

