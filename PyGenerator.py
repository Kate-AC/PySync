import os.path

class PyGenerator:

  def generate(self, json):
    self.json = json

    return ' '.join([
      'rsync',
      self.json['option'],
      self.__getSsh(),
      self.__getIncludes(),
      self.__getExcludes(),
      self.json['current'],
      self.__getTarget()
    ])

  def __getSsh(self):
    home = os.path.expanduser('~')
    ssh  = ' '.join([
      'ssh',
      '-p',
      self.json['port'],
      '-i',
      home + '/.ssh/' + self.json['key']
    ])
    return '-e "' + ssh + '"'

  def __getIncludes(self):
    includes = ''
    for include in self.json['includes']:
      includes += ' --include=' + include
    return includes


  def __getExcludes(self):
    excludes = ''
    for exclude in self.json['excludes']:
      excludes += ' --exclude=' + exclude
    return excludes

  def __getTarget(self):
    return ''.join([
      self.json['user'],
      '@',
      self.json['domain'],
      ':',
      self.json['path']
    ])

