from models import Project

class ProjectsParser:
    @staticmethod
    def parse_lines(lines):
        result = {}
        for line in lines:
            split = line.split('=')
            if len(split) == 2:
                key = split[0].strip()
                value = split[1].strip()
                result[key] = value
        return result

    @staticmethod
    def parse_developers(dictionary, role_name):
        developers = dictionary[role_name].split(',')
        result = []
        for developer in developers:
            result.append(developer.strip())
        return result
        