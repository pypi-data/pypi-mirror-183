import eel
from shortcut import *
from tkinter.filedialog import askopenfilename , askdirectory
import os
import sys

########################################################################################################

cwd=os.path.dirname(__file__)
home=os.getenv('HOME')

########################################################################################################
eel.init(f'{cwd}/web', allowed_extensions=['.js', '.html','.css'])
########################################################################################################
runners = {'python':'python' , 'enaml':'enaml-run','bash':'bash' , 'sh':'sh' , 'xonsh':'xonsh' , 'fish':'fish'}
########################################################################################################

########################################################################################################

########################################################################################################
@eel.expose
def getFilePath(filePath=home):
    filePath = askopenfilename(title='select app',initialdir=filePath)
    return filePath

@eel.expose
def getIconPath(iconPath=home):
    iconPath = askopenfilename(title='select icon',initialdir=iconPath)
    return iconPath

@eel.expose
def getInterpreterPath(interpreterPath=home):
    interpreterPath = askdirectory(title='select venv',initialdir=interpreterPath)
    return interpreterPath

@eel.expose
def make(name,filePath,iconPath,interpreterPath,cmd,ccmd,typ,runner,is_terminal,categories,places,argv):
    runners['python'] = interpreterPath.removesuffix('/bin')+'/bin/python' if interpreterPath.strip() else 'python'
    command = ''
    match typ:
        case 'binary':
            command = ccmd + ' ' + filePath
        case _:
            match cmd:
                case 'defaults':
                    command = runners[runner] + ' ' + filePath
                case _:
                    command = ccmd + ' ' + filePath
    command = f'{command} {argv}'
    if 'menu' in places:
        createMenuShortCut(name=name,command=command,icon=iconPath,terminal=is_terminal,categories=categories)
    if 'desktop' in places:
        createDesktopShortCut(name=name,command=command,icon=iconPath,terminal=is_terminal,categories=categories)
########################################################################################################

########################################################################################################

if __name__ == "__main__":

    eel.start('index.html' , size = (300, 650), position = (800, 200))