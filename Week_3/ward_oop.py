from abc import ABC, abstractmethod
#all objects are protected variables which can only used withn class or sub-class
class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
    @abstractmethod #create a blueprint for a method, this method will be overided in child class
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Ward():
    def __init__(self,name):
        self._name = name
        self._people = []

    def add_person(self,person):
        self._people.append(person)

    def describe(self):
        print(f"Ward name: {self._name}")
        print("List of people:")
        for pupil in self._people:
            pupil.describe()
    
    def count_doctor(self):
        count = 0
        for pupil in self._people:
            if isinstance(pupil,Doctor):
                count += 1
        return count

    def sort_age(self):
        age_sorted = self._people.sort(key = lambda pupil: pupil._yob)
        return age_sorted
    
    def compute_average(self):
        sum_teacher_age = 0
        count_teacher = 0
        for pupil in self._people:
            if isinstance(pupil,Teacher):
                sum_teacher_age += pupil._yob
                count_teacher += 1
        mean_teacher_age = sum_teacher_age / count_teacher
        return mean_teacher_age
    
if __name__ == "__main__":
    student1 = Student(name = "Jack", yob=2010, grade='7')
    student1.describe()

    teacher1 = Teacher("Ms.Martha", yob=1969,subject="CS")
    teacher1.describe()

    doctor1 = Doctor("X",yob=1945,specialist='Endocrinologists')
    doctor1.describe()
    print()
    #
    teacher2 = Teacher("Phan Tan Trung", 1995,'Joke')
    doctor2 = Doctor("Charles Xavier",1975,'unknow')
    ward1 = Ward("Yale")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    print()
    #
    print(f"Number of doctor: {ward1.count_doctor()}")
    print()
    #
    ward1.sort_age()
    print("Age after sorted:")
    ward1.describe()
    print()
    #
    print(f"Average age of tearcher: {ward1.compute_average()}")