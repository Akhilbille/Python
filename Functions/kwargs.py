def kwargs(id,**list_details):
    for i,j in list_details.items():
        print(i[0],j[1])

kwargs(1,name="Akhil",branch="ece")
