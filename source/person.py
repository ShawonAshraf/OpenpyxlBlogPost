class Person:
    def __init__(self, name, address, email):
        self.__name = name
        self.__address = address
        self.__email = email

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def __str__(self):
        return 'Name : ' + self.getName() + '\nAddress : ' + self.getAddress()
        + '\nEmail : ' + self.getEmail()
