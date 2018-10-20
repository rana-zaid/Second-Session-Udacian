
#!/usr/bin/env python3
#
# Udacian activity to practice get and post http
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from Udacian_Rana import Udacian
memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        # Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()
        # Extract the "message" field from the request data.
        name = parse_qs(data)["name"][0]
        city = parse_qs(data)["city"][0]
        enrollment = parse_qs(data)["enrollment"][0]
        nanodegree = parse_qs(data)["nanodegree"][0]
        status = parse_qs(data)["status"][0]
        st = Udacian(name,city,enrollment,nanodegree,status)
        # Store it in memory.
        memory.append(st.print_Udacity())
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()
        # 1. Send a 303 redirect back to the root page.
    def do_GET(self):
        self.send_response(200)
        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        # 2. Put the response together out of the form and the stored messages.
        # 3. Send the response.
        mesg = form.format("\n".join(memory))
        self.wfile.write(mesg.encode())
        
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()