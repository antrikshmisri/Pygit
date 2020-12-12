from subprocess import call
from sys import platform as _platform
import repoinfo
info = repoinfo.checkinfoInDir()

class Git:
    @classmethod
    def __init__(self , url:str=info[0] , branch=info[1]):
        if(url == ''):
            print('URL arg cannot be empty')
            return
        if(branch == ''):
            print('Branch not passed , using master as default')
        if('n' in info):
            info.remove('n')
            self.url = info[0]
            self.branch = info[1]

        self.url = url
        self.branch = branch
    @classmethod
    def init(self):
        call('git init')
    @classmethod
    def add(self , filename:str = '.'):
        if(filename == ''):
            print('Filename not passed , adding all files by default')
            return
        call('git add ' + filename)
    @classmethod
    def commit(self , message:str):
        if(message == '' ):
            print('Message not passed , need a message for commit')
            return
        call('git commit -m "' + message + '"')
    @classmethod
    def pull(self):
        call('git pull')
    @classmethod
    def push(self):
        print('git push -u ' + self.url+ ' ' + self.branch)