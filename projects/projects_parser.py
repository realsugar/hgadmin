import os

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
    def parse_list(dictionary, list_name):
        items = dictionary[list_name].split(',')
        result = []
        for item in items:
            result.append(item.strip())
        return result

    @staticmethod
    def parse_project(full_path):
        hgrc = os.path.join(full_path, '.hg/hgrc')
        file = open(hgrc, 'r')
        lines =  file.readlines()
        file.close()
        dictionary = ProjectsParser.parse_lines(lines)
        return dictionary



        