# coding=utf-8

class Student(object):
    '''2018 new student'''
    grade = 2018
    __school = '清华'

    def __init__(self,subj,name,age,sex):
        '''this is create fun'''
        self.subj = subj
        self.name = name
        self.age = age
        self.sex = sex
        print('init student')

    def setName(self, newname):
        self.name = newname

    def getName(self):
        return self.name

    def showStudent(self):
        print('subj=',self.subj)
        print('name=',self.name)
        print('age=',self.age)
        print('sex=',self.sex)
        print('grade=',Student.grade)
        print('school=',Student.__school)

    @classmethod
    def updategrade(cls, newgrade):
        cls.grade = newgrade

    @classmethod
    def showClass(cls):
        print('__name__=',cls.__name__)
        print('__dict__=',cls.__dict__)
        print('class__=',cls.__class__)

if __name__ == '__main__':
    s1 = Student('专业','xiaocai',12,'女')
    print(s1.getName())
    s1.setName('yaya')
    print(s1.getName())
    print(s1.showClass())
    print(s1.showStudent())
    s1.updategrade(2019)
    print('啦'*20)
    print(s1.showStudent())
    content = dir(Student)
    print(content)


