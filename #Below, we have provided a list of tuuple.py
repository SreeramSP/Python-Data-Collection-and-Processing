#Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

opposites=filter(lambda x: len(x[1])>3 and len(x[0])>3 , zip(l1,l2) )

