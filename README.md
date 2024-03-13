# EX01 Developing a Simple Webserver
## Date : 11/03/2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```program
from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content with a list of the top 5 revenue-generating companies
content = """
<!DOCTYPE html>
<html>
<head>
    <title>Top 5 Revenue-Generating Companies</title>
</head>
<body style="background-color:powderblue;">
    <center>
        <h1>Top 5 Revenue-Generating Companies</h1>
    </center>
    <center>
        <table border="1">
            <tr> 
               <th></th>
               <th>Name of the Company</th><th>Revenue(TTM)</th>
             </tr>
             <tr>
               <th>1 </th>
               <td>Microsoft Corp</td><td>$203.08 billion</td>
             </tr>
             <tr> 
               <th>2 </th><td>Oracle Corp</td><td>$46.07 billion</td>
            </tr>
            <tr> 
               <th>3 </th><td>SAP SE</td><td>$32.97 billion</td>
            </tr>
            <tr> 
                <th>4 </th><td>Salesforce, Inc</td><td>$30.29 billion</td>
             </tr>
             <tr> 
                <th>5 </th><td>Adobe Inc</td><td>$17.61 billion</td>
             </tr>
           </table>
    </center>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',80)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![Screenshot 2024-03-14 000736](https://github.com/sanjay5656/simplewebserver/assets/115128955/409a77c3-ad8a-4dc8-9a74-2bd79ca72362)

## RESULT:
The program for implementing simple webserver is executed successfully.
