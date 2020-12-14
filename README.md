# Pygit
## Installation:
<br/>

    pip install Pygitcli
    
## Here is an example that shows how you can run git commands:-

    #example code
    import pygitcli
    git = pygitcli.Git()
    git.init()
    # if no argument is passed to add , it deafults the arg to all
    git.add('filename')
    git.commit('commit message')
    git.push()
    

### Pygit intelligently detects if the project is already configured with a github repository, If it finds the repository , it automatically adds them to the Git class.

<br/>
<hr/>

### If you want to override the arguments of the Git class  pass the url , branch to the class in the following way:-

    #override the args of Git
    import pygitcli
    git = pygitcli.Git('repo url' , 'branch name')
    git.init()
    git.add('filename')
    git.commit('commit message')
    git.push()
