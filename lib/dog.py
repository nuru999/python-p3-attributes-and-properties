#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name=None, breed=None):
        self._name = "Name must be string between 1 and 25 characters."
        if name is not None:
            self.set_name(name)
        self._breed ="Breed must be in list of approved breeds.\n"
        if breed is not None:
            self.set_breed(breed)
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        if type(name) == str and 0< len(name) <25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
    def get_breed(self):
        return (self._breed)
    def set_breed(self,breed):
        # self._breed = breed if breed in APPROVED_BREEDS else "Breed must be in list of approved breeds.\n"
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    breed = property( get_breed,set_breed )

evie = Dog()
evie.breed = "Chihuah"
print(evie.breed)

