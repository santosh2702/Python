#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

print "Registration Form"
print """
<html>
<head>
<title>Register</title>
<style>
body{
	background-color:rgb(215,150,100);
	margin:10px;
	font-size:30px;
	;
}


</style>
</head>
<body>
<hr/>
<form action="code.py" method="post">
Name:<input type="text" name="name"/>
<br/><br/>
F'Name:<input type="text" name="fname"/>
<br/><br/>
Gender:
<input type="radio" name="a" value="male"/>Male
<input type="radio" name="a" value="female"/>Female
<br/><br/>
Email:
<input type="email" name="email"/>
<br/><br/>
Password:
<input type="password" name="password"/>
<br/><br/>
<input type="submit" value="Register"/>
</form>
</body>
</html>

"""

