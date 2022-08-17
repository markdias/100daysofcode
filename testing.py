from random import Random, random


class Epv():

    def __init__(self, baseurl) -> None:
        self.version = 1.0
        self.baseurl = baseurl
        self.concurrent = 0

   

    def new_session(self,**kw):
        if kw.get('version') == None:
            self.version = self.version
        else:
            self.version = kw.get('version')
        if kw.get('concurrent') == None:
            self.concurrent = self.concurrent
        else:
            self.concurrent = kw.get('concurrent')
        
        token = '47685y435hu4i35hi435'

        return token

    def get_user(self, username,  token = new_session):
        self.token = token
        self.username = username
        return username, token
  
epv = Epv(baseurl='https://epv.corp.bloomberg.com')


print(epv.get_user('user'))




