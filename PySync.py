import sys
from PyExecutor import PyExecutor
from PyReadJson import PyReadJson

args  = sys.argv

try:
  if 2 > len(args):
    raise Exception

  path = args[1]

  if 3 > len(args):
    order = ''
  else:
    order = args[2]

  pyReadJson = PyReadJson()
  pyReadJson.readJson(path)
  pyExecutor = PyExecutor()
  pyExecutor.setJson(pyReadJson.getJson())

  if 'deploy' == order:
    print(pyExecutor.getCommand())
    pyExecutor.deploy()
  else:
    print('Usable args.')
    print('  deploy: Execute rsync command.')
except:
  print('Error: Incorrect ssh directory path.')

