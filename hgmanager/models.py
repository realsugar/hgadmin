
class Developer:
    __login = None
    __password = None

    @staticmethod
    def all():
        return DevelopersParser.parse()

    def save(self):
        DevelopersWriter.write(self)

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
