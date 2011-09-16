from fabric.api import *
from datetime import datetime

env.datetime = datetime.now().strftime("%d-%m-%Y-%H-%M")


"""
Environments
"""
def production():
    env.hosts = ['root@mlsdev.com']
    env.settings = 'settings'
    env.path = "/var/www/hgm"


"""
Commands - deployment
"""
def deploy():
    require('settings', provided_by=[production])
    require('path', provided_by=[production])

    with(cd('%(path)s' % env)):
        update()

"""
Commands
"""
def update():
    run('hg update')
    run('apache2ctl restart')
