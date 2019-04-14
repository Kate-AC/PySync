import json
import subprocess
from PyGenerator import PyGenerator

class PyExecutor:

  def __init__(self):
    self.pyGenerator = PyGenerator()

  def setJson(self, json):
    self.json = json

  def getJson(self):
    return self.json

  def getCommand(self):
    return self.pyGenerator.generate(self.getJson())

  def deploy(self):
    try:
      print(self.getCommand())
      subprocess.check_call(self.getCommand(), shell=True)
      print('Success!')
    except:
      print('Error!')

