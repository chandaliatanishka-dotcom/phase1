class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self._score = score

    @property 
    def score(self):
        return self._score

    @property 
    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        #for humans: print(student) will return a string representation of the student object
        return f"{self.name}: {self._score} ({self.grade})"

    def __repr__(self):
        #for developers: print(student) will return a string representation of the student object
        return f"Student(name={self.name}, score={self._score})"

#Test it
s1 = Student("Tia", 95)
s2 = Student("Rohan", 82)
print(s1)  #uses __str__ method
print(repr(s2))  #uses __repr__ method
print(s1.grade) #uses grade property    
print(s1.score) #uses grade property