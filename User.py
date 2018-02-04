class User:
    def __init__(self,name,username,email,birthday,password):
        self.__name = name
        self.__username = username
        self.__email = email
        self.__birthday = birthday
        #self.__gender = gender
        self.__password = password
        #self.about = ''
#NAME
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
#USERNAME
    def get_username(self):
        return self.__username
    def set_username(self,username):
        self.__username = username
#PASSWORD
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password = password
#EMAIL
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email
#ABOUT
#    def get_about(self):
#        return self.__about
#    def set_about(self,about):
#        self.__about = about
#BIRTHDAY
    def get_birthday(self):
        return self.__birthday
    def set_birthday(self,birthday):
        self.__birthday = birthday
#GENDER
    #def get_gender(self):
    #    return self.__gender
    #def set_gender(self,birthday):
    #    self.__gender = birthday