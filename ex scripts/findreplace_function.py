import re

def cleanup(ugly_string):	
	ugly_string = re.sub('\s+{2}',' ',ugly_string)
	return ugly_string

clean_string = cleanup("    Hello         There.      Everyone!!!!!!!         ")

print(clean_string)

# re.sub( '\s+', ' ', mystring ).strip()