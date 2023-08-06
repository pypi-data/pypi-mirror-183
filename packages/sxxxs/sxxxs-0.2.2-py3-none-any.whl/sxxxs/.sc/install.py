from shortcut import *
import os
cwd=os.path.dirname(__file__)


createMenuShortCut(name='sc', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/sc.svg', terminal=True)
createDesktopShortCut(name='sc', command=f'{cwd}/venv/bin/python {cwd}/main.py', icon=f'{cwd}/sc.svg', terminal=True)