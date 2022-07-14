import  logging
logging.basicConfig(filename="CsObCn.log",level=logging.INFO,format='%(asctime)s,%(name)s,%(levelname)s,%(message)s')
logging.info("Examples for class,object and constructor")
##class
class Student:
    try:
      def __init__(self,name,course,fee):
          logging.info("Constructor started")
          self.name = name
          self.course = course
          self.fee = fee
          logging.info("student name - %s",name)
          logging.info("course name  - %s", course)
          logging.info("course fee - %s", fee)

          print(name, course, fee)
    except Exception as e:
        logging.error(e)

obj=Student("Muskan","data structure","15000")
print(obj)


class IneuronServices:
    logging.info("Examples of abtraction")
    __service1="Internship"
    __service2="Jobs"

    try:
        logging.info(" fisrt example for abstraction")
        def services1(self):

            print("first provided by Ineuron is : ", IneuronServices.__service1)

    except Exception as e:
        logging.error(e)

    try:
        logging.info(" second example for abstraction")
        def services2(self):

            print("second service provided by Ineuron is : ", IneuronServices.__service2)

    except Exception as e:
        logging.error(e)

obj=IneuronServices()
print(obj._IneuronServices__service1)
print(obj._IneuronServices__service2)
print(obj.services1())
print(obj.services2())

class courses:
    c1="DataScience"
    _c2="Javascript"
    __c3="MachineLearning"
class course1(courses):
    try:
        def coursename(self):
            C1=self.c1
            logging.info("The first course is - %s ",C1)

    except Exception as e:
        logging.error(e)

class course2(courses):
    try:
        def coursename1(self):
            C2=self.c2
            logging.info("The second course is - %s",C2)
    except Exception as e:
        logging.error(e)
class course3(courses):
    try:
        def coursename2(self):
            C3=self._courses__c3
            logging.info("The second course is - %s",C3)
    except Exception as e:
        logging.error(e)

obj1=course1()
obj2=course2()
obj3=course3()
print(obj1.coursename)
##print(obj2.coursename1)
print(obj3._courses__c3) ## calling through class

## Inheritance
##Single Inheritance

class Ineuron1:
    logging.info("This is the example of single level inheritance")
    def Jobs(self,type):
        try:
            self.type=type
            print(type)
            logging.info("Type of job is : %s", type)
        except Exception as e:
            logging.error(e)

class Ineuron2(Ineuron1):
    def hallOfFame(self,package):
        try:
            self.package=package
            print(package)
            logging.info("Package received is : %s",package)
        except Exception as e:
            logging.error(e)
#obj_in2=Ineuron2()
#obj_in2.hallOfFame("20 LPA")
#obj_in2.jobs("Data Sciencetist")

#Multi leve inheritance

class Ineuron3(Ineuron2):
    def CourseProvided(self,name_of_course):
        try:
            self.name_of_course=name_of_course
            print(name_of_course)
            logging.info("name of course provided is - %s",name_of_course)
        except Exception as e:
            logging.error(e)
obj_in3=Ineuron3()
print(obj_in3.Jobs("Manager"))
print(obj_in3.hallOfFame("20lpa"))
print(obj_in3.CourseProvided("Datascience bootcamp"))

#Multiple inheritance

class Ineuron4:
    def Placement(self,companyName):
        try:
            self.companyName = companyName
            print(companyName)
            #logging.info("name of course provided is - %s", companyName)
        except Exception as e:
            logging.error(e)
class Ineuron5:
    def interviews(self,dateOfInterview):
        try:
            self.dateOfInterview = dateOfInterview
            print(dateOfInterview)
            #logging.info("name of course provided is - %s", dateOfInterview)
        except Exception as e:
            logging.error(e)
class Ineuron6(Ineuron4,Ineuron5):
    def result(self,value):
        try:
            self.value = value
            print(value)
           # logging.info("name of course provided is - %s", value)
        except Exception as e:
            logging.error(e)
obj_in6=Ineuron6()
print(obj_in6.Placement("TataIQ"))
print(obj_in6.interviews("2ndJuly"))
print(obj_in6.result("ClearedInterview"))

#polymorphism

class Ineuron:
    try:
        def Intro(self):
            logging.info("All the students of Ineuron belong to different courses.")

        def Courses(self):
            logging.info("Some belong to FSDS course and some to FSDA.")

    except Exception as e:
        logging.error(e)


# child class 1
class CourseFSDS(Ineuron):
    try:
        # using the same method of base class differently using polymorphism
        def Courses(self):
            logging.info("These students belong to FSDS course and not FSDA.")

    except Exception as e:
        logging.error(e)


# child class 2
class CourseFSDA(Ineuron):
    try:
        def Courses(self):
            # using the same method of base class differently using polymorphism
            logging.info("These students belong to FSDA course and not FSDS.")

    except Exception as e:
        logging.error(e)


# this function behaves like a bridge between all the classes as per the object
def ineuron_external(a):
    a.Intro()
    a.Courses()
i6 = Ineuron()
i7 = CourseFSDS()
i8 = CourseFSDA()
ineuron_external(i6)  # This is for the parent class
ineuron_external(i7)  # This is for child class 1
ineuron_external(i8)  # This is for child class 2

## method overriding

# creating base class
class Studentclass:
    try:
        def __init__(self, course):
            self.course = course

        # defining method for the base class
        def Course(self):
            logging.info(f"The course attended by the student at the beginning is {self.course}")

    except Exception as e:
        logging.error(e)


# creating child class to override the method
class Changeclass(Studentclass):
    try:
        # constructor
        def __init__(self, course):
            self.course = course

        # defining method for the child class using method overriding
        def Course(self):
            logging.info(f"The course attended by the student after change is {self.course}")

    except Exception as e:
        logging.error(e)


# Initializing
i5 = Studentclass("FSDS")
i5.Course()
# Using the child class to call the same method
i5 = Changeclass("FSDA")
i5.Course()































