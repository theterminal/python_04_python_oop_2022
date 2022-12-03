from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('James', {'karate': ['note 1']})
        self.student_no_courses = Student('Jimmy')

    def test_1_init_with_none_courses(self):                            # 1, 2, x, x, x, x, x, x, x, x : 20%
        self.assertEqual({}, self.student_no_courses.courses)

    def test_2_correct_init(self):                                      # 1, 2, x, x, x, x, x, x, x, x : 20%
        self.assertEqual('James', self.student.name)
        self.assertEqual({'karate': ['note 1']}, self.student.courses)

    def test_3_enroll_add_notes_to_existing_course(self):               # 1, 2, x, x, x, 6, x, x, x, x : 30%
        result = self.student.enroll('karate', ['first note', 'second note'])
        self.assertEqual(3, len(self.student.courses['karate']))
        self.assertEqual('first note', self.student.courses['karate'][1])
        self.assertEqual('second note', self.student.courses['karate'][2])
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_4_enroll_add_course_notes_without_no_3rd_param(self):       # 1, 2, x, x, 5, 6, 7, x, x, x : 50%
        result = self.student.enroll('python', ['python notes'])
        self.assertEqual(['python notes'], self.student.courses['python'])
        self.assertEqual('Course and course notes have been added.', result)

    def test_5_enroll_add_course_notes_with_3rd_parameter_Y(self):       # 1, 2, x, 4, 5, 6, 7, x, x, x : 60%
        result = self.student.enroll('python', ['python notes'], 'Y')
        self.assertEqual(['python notes'], self.student.courses['python'])
        self.assertEqual('Course and course notes have been added.', result)

    def test_6_enroll_add_course_without_adding_the_notes(self):         # 1, 2, 3, 4, 5, 6, x, x, x, x : 60%   !!!
        result = self.student.enroll('python', ['python notes not to be added'], 'N')
        self.assertEqual([], self.student.courses['python'])
        self.assertEqual('Course has been added.', result)

    def test_7_add_notes_on_existing_course(self):                       # 1, 2, 3, 4, 5, 6, 7, x, x, x : 70%
        result = self.student.add_notes('karate', 'note math 1')
        self.assertEqual(['note 1', 'note math 1'], self.student.courses['karate'])
        self.assertEqual('Notes have been updated', result)

    def test_8_add_notes_to_non_existing_course(self):                  # 1, 2, 3, 4, 5, 6, 7, 8, x, x : 80%
        with self.assertRaises(Exception) as ex:
            self.student_no_courses.add_notes('math', 'some note')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_9_leave_course_for_existing_course(self):                  # 1, 2, 3, 4, 5, 6, 7, 8, 9, x : 90%
        result = self.student.leave_course('karate')
        self.assertEqual({}, self.student.courses)
        self.assertEqual('Course has been removed', result)

    def test_10_leave_course_for_non_existing_course(self):             # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 : 100%
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('python')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()
