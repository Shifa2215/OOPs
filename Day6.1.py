from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")

c = Car()
b = Bike()
bu = Bus()

c.start_engine()
b.start_engine()
bu.start_engine()
