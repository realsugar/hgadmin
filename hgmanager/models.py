from hgmanager.developers_parser import DevelopersParser
from hgmanager.developers_writer import DevelopersWriter

class Developer:
    __login = None
    __password = None

    @staticmethod
    def all():
        list = DevelopersParser.parse()
        result = []
        for login in list:
            developer = Developer()
            developer.set_login(login)
            result.append(developer)
        return result

    @staticmethod
    def get_by_login(login):
        result = None
        developers = Developer.all()
        for developer in developers:
            if developer.login() == login:
                result = developer
                break
        return result

    def get_edit_url(self):
        return '/developer/edit/%s' % self.login()

    def save(self):
        DevelopersWriter.update(self)

    def login(self):
        return self.__login

    def set_login(self, new_login):
        self.__login = new_login

    def password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def __unicode__(self):
        return self.login()

    
class Project:
    pass
