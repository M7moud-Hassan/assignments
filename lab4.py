import re
import time

class Person:
    Moods = ('happy', 'tired', 'lazy')
    def __init__(self, name):
        self.name = name
        self.__mood = 'unknown'
        self.money = 0
        self.__healthRate = 'unknown'

    def sleep(self, hours):
        if hours == 7:
            self.mood = self.Moods[0]
        elif hours < 7:
            self.mood = self.Moods[1]
        elif hours > 7:
            self.mood = self.Moods[2]

    def eat(self, meals):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"

    def buy(self, items):
        self.money -= items * 10

class Employee(Person):
    def __init__(self, id, name, car,distance):
        self.id = id
        self.car = car
        self.distance=distance
        self.__salary=1000
        super(Employee, self).__init__(name)

    @property
    def Salary(self):
        return self.__salary

    @Salary.setter
    def Salary(self, newValue):
        if (newValue >= 1000):
            self.__salary = newValue
        else:
            print("invalid salary")

    @property
    def Email(self):
        return self.__email

    @Email.setter
    def Email(self, newValue):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        match = re.match(regex, newValue)
        if (match != None):
            self.__email = match.string
        else:
            print('invalid email')



    @property
    def HealthRate(self):
        return self.__healthRate

    @HealthRate.setter
    def HealthRate(self, newValue):
        if (newValue > 0 and newValue <= 100):
            self.__healthRate = newValue
        else:
            print("invalid value")

    def work(self, hours):
        if (hours == 8):
            self.__mood = self.Moods[0]
        elif (hours < 8):
            self.__mood = self.Moods[1]
        elif (hours > 8):
            self.__mood = self.Moods[2]

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = gasAmount

    @staticmethod
    def send_email(to, subject, msg, receiver_name):
        print("email to ", to, " msg ", msg)

class Car:
    velocity=10
    def __init__(self, name):
        self.name = name
        self.__velocity=0
        self.__fuelRate=100

    @property
    def Velocity(self):
        return self.__velocity
    @Velocity.setter
    def Velocity(self, newValue):
        if (newValue > 0 and newValue <= 200):
            self.__velocity = newValue
            return True
        else:
            print("invalid value")
            return False

    @property
    def FuelRate(self):
        return self.__fuelRate

    @FuelRate.setter
    def FuelRate(self, newValue):
        if (newValue > 0 and newValue <= 100):
            self.__fuelRate = newValue
            return True
        else:
            print("invalid value")
            return False




    def run(self,distance, velocity):
         if(self.Velocity(velocity)):
            rate=self.FuelRate-distance
            if(self.FuelRate(rate)):
                self.stop()
            else:
                remainDistance=distance-self.FuelRate
                self.__fuelRate=0
                print("please reFuel this car")
                self.stop(1,remainDistance)
         else: print("type valid velocity")

    def stop(self, finish=1, distance=0):
        if (finish):
            self.__velocity = 0
            print("finish trip")
        else:
            self.__velocity = 0
            print("remain distance is ", distance)

class Office:
    employeesNum = 0

    def __init__(self, name,targetHour):
        self.name = name
        self.employees = []
        self.targetHour=targetHour

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for em in self.employees:
            if (em.id == empId):
                return em

    def hire(self, empl):
        self.employees.append(empl)

    def fire(self, empId):
        for em in self.employees:
            if (em.id == empId):
                self.employees.remove(em)

    @staticmethod
    def cal_lateness(targetHour, moveHour, distance, velocity):
        timeSpend=distance/velocity
        return  (moveHour+timeSpend) -targetHour

    def deduct(self, empId, deduction):
        for em in self.employees:
            if (em.id == empId):
                em.Salary = em.Salary - deduction
                break

    def reward(self, empId, reward):
        for em in self.employees:
            if (em.id == empId):
                em.Salary = em.Salary + reward
                break

    def check_lateness(self, empId, moveHour):
        for em in self.employees:
            if (em.id == empId):
                result=Office.cal_lateness(self.targetHour, moveHour, em.distance,em.car.velocity)
                if(result<0):
                   self.deduct(empId,10)
                else:self.reward(empId,10)
                break

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

iti=Office('iti',9)
Office.employeesNum=10
Office.change_emps_num(20)
c=Car('fiat 128')
emp=Employee(1,'samy',c,20)
emp.Salary=5000
iti.hire(emp)
print('velocity of car',emp.car.velocity)
print("distance is ",emp.distance)
print('target hour',iti.targetHour)
iti.check_lateness(1,6)
print(emp.Salary)

