from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}
        
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
        
    def report_grade(self,name,subject,score):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(score)
        
    def avarage_grade(self,name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count
    
    def keys(self):
        return self._grades.keys()
    
book = BySubjectGradebook()
book.add_student('Bartek Szafran')
book.report_grade('Bartek Szafran', 'Math', 90)
book.report_grade('Bartek Szafran', 'Physics', 97)
book.report_grade('Bartek Szafran', 'PE',20)
book.report_grade('Bartek Szafran', 'PE', 67)

book.add_student('Ula Mazur')
book.report_grade('Ula Mazur', 'Math', 79)
book.report_grade('Ula Mazur', 'Math', 99)
book.report_grade('Ula Mazur', 'Math', 89)
book.report_grade('Ula Mazur', 'Hisotry', 76)
book.report_grade('Ula Mazur', 'Physics', 87)

book.add_student('Tom Thomas')
book.report_grade('Tom Thomas', 'Physics', 65)
book.report_grade('Tom Thomas', 'Physics', 45)

for n in book.keys():
    print(f'The avrage grade for {n} is {book.avarage_grade(n)}')
            