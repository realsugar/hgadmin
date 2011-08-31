import settings
from subprocess import call

class DevelopersWriter:
    @staticmethod
    def htpasswd_update_command(developer):
        command = 'htpasswd -b %s %s %s' % (settings.PASSWORDS_PATH,
                                            developer.login(),
                                            developer.password())
        return command

    @staticmethod
    def htpasswd_delete_command(developer):
        command = 'htpasswd -D %s %s' % (settings.PASSWORDS_PATH,
                                            developer.login())
        return command

    @staticmethod
    def update(developer):
        command = DevelopersWriter.htpasswd_update_command(developer)
        return call(command.split(' '))

    @staticmethod
    def delete(developer):
        command = DevelopersWriter.htpasswd_delete_command(developer)
        return call(command.split(' '))