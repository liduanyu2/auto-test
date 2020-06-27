#coding=utf-8
import configparser
class readIni(object):

    def __init__(self,file_name=None,node=None,key=None):
        if file_name==None:
            file_name=("D:/py/auto/auto-test/test/config/LocalElement.ini")
        if node==None:
            self.node="LoginElement"
        self.conf=self.load_ini(file_name)

    def load_ini(self,file_name):
        conf=configparser.ConfigParser()
        conf.read(file_name)
        return conf

    def get_value(self,key):
        data=self.conf.get(self.node,key)
        return data

if __name__=="__main__":
    read_init=readIni()
    print(read_init.get_value("user_name"))