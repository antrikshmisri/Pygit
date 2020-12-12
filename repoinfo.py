import os
mypath = os.getcwd()
infofile = mypath + '/.git/FETCH_HEAD'
import pygit
def takeInfo():
    print('No Existing repo info found\n')
    url = str(input('Enter the Github Repo URL: '))
    branch = str(input('Enter the branch: '))
    info = [url , branch]
    return info

def checkinfoInDir():
    if (os.path.exists(infofile)):
        print('Repo Info Found:-')
        with open(infofile, "r") as f:
            info = f.readlines()
            info = info[0].split()
            if ('branch' in info):
                branch = info[info.index('branch') + 1]
                url = info[info.index('branch') + 3]
                info = [url , branch]
    else:
        info = takeInfo()
    return info
