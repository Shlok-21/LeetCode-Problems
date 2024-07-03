class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                val = students.pop(0)
                students.append(val)

            if students and sandwiches[0] not in students:
                print(students)
                return len(students)
        return 0