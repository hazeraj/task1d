class Module(object):
    module_count = 0

    def __init__(self, ects, title, semester, grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade
        self.dates = []
        self.elements = []
        Module.module_count += 1

    def get_important_dates_overview(self):

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind, date))

    def set_grade(self, grade):
        self.grade = grade

    def add_module_element(self, classs, date):
        obj = classs(self)
        obj.add_important_date(self, date)
        self.elements.append(obj)

    def get_title(self):
        return self.title

    def get_grade(self):
        return self.grade


class ModuleElement(object):
    def __init__(self, module):
        self.module = module

    def add_important_date(self, kind, date):
        self.module.dates.append((kind, date))


class Lesson(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, kind, date):
        ModuleElement.add_important_date(self, "Lesson", date)


class Lab(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, kind, date):
        ModuleElement.add_important_date(self, "Lab Session", date)


class Midterm(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, kind, date):
        ModuleElement.add_important_date(self, "Midterm", date)


class FinalExam(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, kind, date):
        ModuleElement.add_important_date(self, "Final Exam", date)


class Course(Module):
    def __str__(self):
        return "Course: {}".format(self.title)


class Seminar(Module):
    def __init__(self, ects, title, semester, topic, grade=None):
        Module.__init__(self, ects, title, semester, grade)
        self.topic = topic

    def __str__(self):
        return "{} under the topic: {}".format(self.title, self.topic)

    def get_topic(self):
        return self.topic


class Thesis(Module):
    def __init__(self, ects, title, semester, topic, research_group, grade=None):
        Module.__init__(self, ects, title, semester, grade)
        self.topic = topic
        self.research_group = research_group

    def __str__(self):
        return "Bachelor Thesis on the topic: {} in the Research Group {}".format(self.topic, self.research_group)

    def get_topic(self):
        return self.topic

    def get_research_group(self):
        return self.research_group


class Student(object):
    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self, Module):
        self.modules.append(Module)
        self.grades[Module] = Module.get_grade()

    def get_list_modules(self):
        for module in self.modules:
            print(module)

    def get_grades(self):
        for grade in self.grades:
            print(grade)
