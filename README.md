# IDSE
## Lab1
---
## Lab2
### Q1 Student Grading
Write a program in python to find the score and grade of a student based on the following criteria:
Theory test: 50% (2 exams)
Lab Test: 30% (2 exams)
Assignment: 10% (5 assignments)
Mini Project: 10% (1 Mini Project)
Create a dictionary to store the above data. Use the data to grade the student based on the following grading pattern:
score >= 90 : "S"
score >= 80 : "A"
score >= 70 : "B"
score >= 60 : "C"
score >= 50 : "D"
score >= 35 : "E"
score < 35 : "F"

> ram's dictionary, All marks are given out of 100
      { "name":"Ram Padhy",
         "assignment" : [80, 50, 40, 20, 60],
         "theory test" : [75, 75],
         "lab test" : [78.20, 77.20],
         "mini project" : 70,
       }

Find the class average score and average grade if the data for 5 students are given.

>NB: Use of dictionary is compulsory  
[Code](Lab2/grading.py)
---
### Q2 Election Winner
Given an list of the names of candidates in an election. A candidate name in the list represents a vote cast to the candidate. Print the winner of the election. If there is tie, print a lexicographically smaller name (alphabetically smaller).

Input :  votes = ["john", "johnny", "jackie",   
                    "johnny", "john", "jackie",   
                    "jamie", "jamie", "john",  
                    "johnny", "jamie", "johnny",   
                    "john"];  
Output : John  
We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it.
>NB: Use of dictionary is compulsory for this program  
[Code](Lab2/election.py)
---
## Lab3
### Q1
