class User:
    def __init__(self,name,username,birthdate,email,password):
        self.__name = name
        self.__username = username
        self.__birthdate = birthdate
        self.__email = email
        self.__password = password

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
#BIRTHDATE
    def get_birthdate(self):
        return self.__birthdate
    def set_birthdate(self,birthdate):
        self.__birthdate = birthdate
#EMAIL
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email = email


