#coding=utf-8
import configparser
class ReadIni(object):

    def __init__(self,file_name=None,node=None,key=None):
        if file_name==None:
            file_name=("C:/Users/Administrator/Desktop/auto-test/test/config/LocalElement.ini")
        if node==None:
            self.node="LoginElement"
        self.conf=self.load_ini(file_name)

    def load_ini(self,file_name):
        conf=configparser.ConfigParser()
        conf.read(file_name,"utf-8")
        return conf

    def get_value(self,key):
        data=self.conf.get(self.node,key)
        return data

if __name__=="__main__":            #if __name=="__main__"，在自己执行时执行，     #__name__代表当前场景，自己时为__main__外部时为__read_ini__ ?
    read_init=ReadIni()
    print(read_init.get_value("username"))