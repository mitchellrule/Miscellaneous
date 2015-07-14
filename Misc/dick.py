from time import sleep


dick = '''
-----------------------
----------OO-----------
-------OOOOOOOO--------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
-----OOOOOOOOOOOO------    
------OOOOOOOOOO-------   
------OOOOOOOOOO-------   
------OOOOOOOOOO-------    
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
------OOOOOOOOOO-------
-OOOOOOOOOOOOOOOOOOOOO-
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
-OOOOOOOOOOOOOOOOOOOOO-
-----------------------
'''

dicklines = dick.split('\n')

for line in dicklines:
	print line
	sleep(0.3)