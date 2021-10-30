import os
from os.path import join
from subprocess import PIPE, Popen, call

from .colors import logcolors


class Git:
    """Perform various git commands through a script

    Attributes
    ----------
    current_directory: str
        current directory
    path: str
        target path
    git_path: str
        path of .git folder in the target path
    git_command: str
        git command boilerplate to include target/.git path
    """

    def __init__(self, path):
        self.current_directory = os.getcwd()
        self.path = path
        self.git_path = join(self.path, '.git')
        self.git_command = f'git --git-dir={self.git_path} --work-tree={self.path}'

    def init(self):
        """Initializes git repository by calling git init
        """
        os.chdir(self.path)
        call(f'git init')
        os.chdir(self.current_directory)

    def create_readme(self):
        """Creates README.md if during the git repository initialization
        """
        readme_path = os.path.join(self.path, 'README.md')
        dir = self.path.split('\\')[-1]
        with open(readme_path, 'w') as readme:
            readme.write(f'# {dir}')
            readme.close()

    def add(self, file):
        """Stages a changed file by calling git add <filename>

        Parameters
        ----------
        file: str
            filename that needs to be staged
        """
        # perform git add on file
        call(f'{self.git_command} add {file}')

    def commit(self, msg):
        """Commits the changed file with a message by calling git commit -m <message>

        Parameters
        ----------
        msg: str
            commit the changed file with the specified message
        """
        # if msg == -r reject commit
        if(msg == '-r'):
            return False
        # else execute git commit for the file
        else:
            try:
                call(f'{self.git_command} commit -m "{msg}" {self.path}')
                return True
            except Exception as e:
                print(f"{logcolors.ERROR} {e} {logcolors.ENDC}")
                return False

    def set_remote(self, url):
        """Set the remote repository to the specified URL

        Parameters
        ----------
        url: str
            URL of the remote repository
        """
        call(f'{self.git_command} remote add origin {url}')

    def set_branch(self, branch, new=True):
        """Set the working branch to the specified branch

        Parameters
        ----------
        branch: str
            Working branch 
        """
        if new:
            call(f'{self.git_command} branch -M {branch}')
        else:
            call(f'{self.git_command} checkout {branch}')

    def pull(self, info):
        """Pull changes from remote repository

        Parameters
        ----------
        info: list
            first element contains URL, seconds contains branch
        """
        _url, _branch = info
        call(f'{self.git_command} pull {_url} {_branch}')

    def push(self, info):
        """Push the staged and commited changes to the remote URL/branch

        Parameters
        ----------
        info: list
            first element contains URL, seconds contains branch
        """
        _url, _branch = info
        call(f'{self.git_command} push -u {_url} {_branch}')

    def get_remote(self):
        """Get the remote URL from the local directory
        """
        remote = Popen(f'{self.git_command} config --get remote.origin.url',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return remote

    def get_branch(self):
        """Get the working branch from the local directory
        """
        branch = Popen(f'{self.git_command} rev-parse --symbolic-full-name HEAD',
                       stdout=PIPE).stdout.read().decode('utf-8')
        return branch

    def init_repo(self, info):
        """If directory is git initialized, perform starting git commands

        Parameters
        ----------
        info: list
            First element contains URL, second contains branch
        """
        url, branch = info
        self.init()
        self.create_readme()
        self.add('.')
        self.commit('initial commit')
        self.set_branch(branch)
        self.set_branch(url)
        self.pull(info)
        self.push(info)
