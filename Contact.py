class Contact:
    def __init__(self):
        self.__name = ''
        self.__email = ''
        self.__subject = ''
        self.__message = ''

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message

    #def set_name(self,name):
     #   self.__name = name

    #def set_email(self,email):
    #    self.__email = email

    #def set_subject(self,subject):
    #    self.__subject = subject

    #def set_message(self,message):
    #    self.__message = message