if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = student_marks[query_name]
    a = 0
    for i in range(len(avg)):
        a+=avg[i]
    num = a/3
    print(f"{num:.2f}")
    '''This code is a Python script that seems to be designed for handling student information, including their names and scores, and then performing some kind of query based on a given name. Let's break down the code step by step:

if __name__ == '__main__'::
This line is a common Python idiom that checks whether the script is being run directly as the main program or if it's being imported as a module into another script. When a Python script is executed, __name__ is set to '__main__'. So, code within this block will only run when the script is run directly.

n = int(input()):
This line reads an integer from the user (presumably, the number of students' information to be entered) and stores it in the variable n.

student_marks = {}:
It initializes an empty dictionary called student_marks which will be used to store the student names as keys and their scores as values.

for _ in range(n)::
This line starts a loop that iterates n times. The variable _ is used when you don't intend to use the loop counter value.

name, *line = input().split():
Inside the loop, this line reads a line of input from the user and splits it into words using the split() method. It then unpacks the first word into the variable name and the remaining words into the list line.

scores = list(map(float, line)):
This line converts the list of words in line into a list of floating-point numbers. It does so by using the map function to apply the float function to each element in line and then converting the result to a list.

student_marks[name] = scores:
This line associates the student's name (stored in name) with their list of scores (stored in scores) in the student_marks dictionary.

query_name = input():
Finally, this line reads a query name from the user. It is assumed that this query name corresponds to a student whose scores you want to retrieve or manipulate in some way.

In summary, this code reads and stores information about multiple students, where each student has a name and a list of scores. After reading this information, it waits for a query name. You can use this code to retrieve or manipulate the scores of a specific student based on the provided query name, although the specific query functionality is not shown in this code snippet.'''