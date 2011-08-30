from hgmanager.models import Developer
import settings

class DevelopersParser:
    @staticmethod
    def parse_developers(path):
        result = []
        file = open(path, 'r')
        for line in file:
            login = line.split(':')[0]
            if (login):
                developer = Developer()
                developer.set_login(login)
                result.append(developer)
        return result

    @staticmethod
    def parse():
        return DevelopersParser.parse_developers(settings.PASSWORDS_PATH)