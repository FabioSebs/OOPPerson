class Person():
    def __init__(self , name:str , address:str):
        self._name = name
        self._address = address
    
    @property
    def name(self):
        return self._name
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self , address:str):
        self._address = address
        
    def __str__(self):
        return f'This is Person Class - Name = {self.name} || Address = {self.address}'

class Student(Person):
    def __init__(self , name:str , address:str , courses: list,
     grades:list  , num_course:int = 0):
        super().__init__(name, address)
        self._num_course = num_course
        self._courses = courses
      
        self._grades = grades
    
    def addCourseGrade(self, course , grade):
        for i in range(len(course)):
            self._courses.append(course[i])
            self._grades.append(grade[i])
    
    def printGrades(self):
        for i in self._grades:
            print(i)
    
    def getAverageGrade(self):
        summ = 0
        count = 0
        for i in self._grades:
            summ += i
            count += 1
        
        return summ/count
    
    def __str__(self):
        return super().__str__() + f' This is also the student class Course = {self._courses} , Grades = {self._grades}, Number of Courses = {self._num_course} , Average = {self.getAverageGrade()}'
    
class Teacher(Person):
    
    def __init__(self , name:str , address:str ,num_courses:int, courses:list):
        super().__init__(name, address)
        self._num_courses = num_courses
        self._courses = courses
        
    def addCourse(self, course:list):
        if course in self._courses:
            return False
        
        for i in course:
            self._courses.append(i)
            
        self._num_courses += 1
        return True
    
    def removeCourse(self, course):
        if course not in self._courses:
            return False
        
        self._courses.remove(course)
        self._num_courses -= 1
        return True
    
    def __str__(self):
        return super().__str__() + f'This is teacher class , Number of Courses = {self._num_courses} , Courses = {self._courses}'        


if __name__ == "__main__":
    person = Person("Fabio" , "FabioVille Ave")
    print(person.__str__())
    person.address = "FabioVille Street"
    print(person.__str__())
    
    student = Student("Jonny" , "JonnyVille" , ['Math' , 'English' , 'Science'], [90 , 80, 85] , 3)
    print(student.__str__())
    student.addCourseGrade(['Art' , 'Programming'] , [90, 100])
    print(student.__str__())
    
    teacher = Teacher("Julian", "Julianville", 5 , ['Bahasa' , 'English' , 'Programming' , 'Math' , 'Art'])
    print(teacher.__str__())
    teacher.removeCourse("Bahasa")
    print(teacher.__str__())
    teacher.addCourse(["Bahasa"])
    print(teacher.__str__())