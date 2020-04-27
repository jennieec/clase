class student:

def _init_(self, code, name, age, gender, carrreer):
self.code = code
self.name = name
self.age = age
self.gender = gender
self.carrreer = carrreer

def set_age(self, age):
    self.age = age

def set_gender(self, gender):
    self.gender = gender

def set_career(self, carrreer):
    self.carrreer = carrreer

def get_age(self):
    return ("edad: " + self.age)

def get_gender(self):
    return ("genero: " + self.gender)