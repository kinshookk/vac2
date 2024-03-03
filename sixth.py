data=''
file = open("text.txt","r")
data=file.read()
file2=open("result.txt","w")
file2.write(data)