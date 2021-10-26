# Pygit
[![Downloads](https://pepy.tech/badge/pygitcli)](https://pepy.tech/project/pygitcli) <br />
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
## Installation:
<br/>

```bash
pip install Pygitcli
```
<br/>

## Here is an example code to perform various git commands:-
```python
"""
===============
Pygitcli
===============
This example shows how to use the Pygitcli module. We will demonstrate how 
to perform various git commands.
First, some imports.
"""
from Pygitcli.git import Git

###############################################################################
# Now let's initialize the Git class 
# We need to provide the path to the target directory

git = Git(r'D:\test_directory')

###############################################################################
# Next we will initialize an empty git directory in the target directory

repo_info = ['https://github.com/test_user/test_repo.git', 'master']
git.init_repo(repo_info)

###############################################################################
# Next, we'll perform various git commands

git.add('test_file.txt')
git.commit('test_file.txt')
git.pull(repo_info)
git.push(repo_info)

###############################################################################
# There are some utility functions in the Git class as well

git.create_readme() # creates a README.md in the target directory

# Set remote URL, branch
git.set_remote(url='https://github.com/test_user/test_repo.git')
git.set_branch(branch='master', new=True) # If the branch already exists set new to False

# Get remote repository information (URL, branch)
url = git.get_remote()
branch = git.get_branch()
```

<br/>
<hr/>
