month=input("enter month:")
if month==("jan" or "mar" or "may" or "jul" or "aug"  or "oct" or "dec"):
  print("31")
elif month==("apr" or "jun" or "sep" or "nov"):
	print("30")
elif month==("feb"):
	print("29")
 else:
	print("enter crct")
