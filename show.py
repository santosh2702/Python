#!C:\Python27\python.exe
import MySQLdb
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>SHOW ALL USERS</title>
<style>
body{
background-color:rgb(100,100,150);
}
th{
	size:100px;
	color:black;
}

</style>
</head>
<body>

<h1 style="text-align:center;color:black;">SHOW ALL USERS</h1>
<table border="1" align="center">
<tr>
<th>Name</th>
<th>Gender</th>
<th>Email Address</th>
<th>Password</th>
<th>Contact No</th>
<th>Delete</th>
<th>Edit</th>
</tr>

"""
con=MySQLdb.connect("127.0.0.1","root","","project",3306)
cur=con.cursor()
cur.execute("select * from ipec")
res=cur.fetchall()
for row in res:
 print "<tr><td>",row[1],"</td>"
 print "<td>",row[2],"</td>"
 print "<td>",row[3],"</td>"
 print "<td>",row[4],"</td>"
 print "<td>",row[5],"</td>"
 print "<td><a href='delete.py?id=",row[1],"'>delete</a></td>"
 print "<td><a href='edit.py'>edit</a></td></tr>"
print """</table>
</body>
</html>
"""
