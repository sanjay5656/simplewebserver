from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content with a list of the top 5 revenue-generating companies
content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Top 5 Revenue-Generating Companies</title>
</head>
<body style="background-color:LightCyan;">
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
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()