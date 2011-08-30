import settings
from subprocess import call

class DevelopersWriter:
    @staticmethod
    def htpasswd_command(developer):
        command = 'htpasswd -b %s %s %s' % (settings.PASSWORDS_PATH,
                                            developer.login(),
                                            developer.password())
        return command

    @staticmethod
    def write(developer):
        command = DevelopersWriter.htpasswd_command(developer)
        return call([command])
