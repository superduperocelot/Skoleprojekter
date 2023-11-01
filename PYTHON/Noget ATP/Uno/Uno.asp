<html>
<head>
    <title>My First ASP Page</title>
</head>
<body bgcolor="white" text="black">
    <%
    Dim strMessage
    strMessage = "Hello World"
    Response.Write (strMessage)
    Response.Write ("<br>")
    'Write the server time on the web page using the VBScript Time() function
    Response.Write ("The time on the server is: " & Time())
    'Close the server script
    %>
</body>
</html>