# hadoop-exercise-1

Exercise 1  
Q1. How many files are there?
7 ( 6 part files 1 success file).
Q2. Did number of mapper change?
no because the number of mapper depend on the split number of the text.
Q3. Did number of reducer changed? 
yes ,the default was 3 and after we define -numReduceTasks 6 so it changed to 6.
Q4. Did number of output files change? Why?  
yes because every reducer write 1 output file .
Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?  
It is the number of map output chunks that were merged during the shuffle phase, and it is basically mappers × reducers (e.g., 9×3=27, 9×6=54).

Exercise 2  
Q1. Is your change in the mapper or in the reducer?
The change is in the mapper


Exercise 3
Q1. Is your change in the mapper or in the reducer?  
The change is in the reducer

Q3. Print the output of the MapReduce and add to the project.  
[hadoop@ip-172-31-35-42 course]$ hadoop fs -cat /user/hduser/gutenberg-output/*
the     74369
and     42768
of      34588
