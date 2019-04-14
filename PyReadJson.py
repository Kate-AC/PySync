import json

class PyReadJson:

  def readJson(self, path = '.'):
    try:
      fileName  = path + '/pysync.json'
      file      = open(fileName, 'r')
      self.json = json.load(file)
    except:
      print('Error: Incorrect pysync.json path.')

  def getJson(self):
    return self.json

