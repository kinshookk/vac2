data=''
file = open("text.txt","r")
data=file.read()
data= data.upper()
file2=open("result.txt","w")
file2.write(data)