#!/usr/bin/env python3
 
"""Simple HTTP Server With Upload & Text Save.

@jerrylususu mods:

1. icons removed
2. fix the problem of "port already in use" when performing ctrl-c shutdown and restart
3. allows simple text file to be saved directly from the web page

see: https://github.com/Tallguy297/SimpleHTTPServerWithUpload
see: https://gist.github.com/UniIsland/3346170
"""
 
 
__version__ = "0.1"
__all__ = ["SimpleHTTPRequestHandler"]

# Original Author
# __author__ = "bones7456"
# __home_page__ = "https://gist.github.com/UniIsland/3346170"

__author__ = "jerrylususu"

# Name for the text file saved
TEXT_FILE_NAME = ""
 
import os, sys
import os.path, time
import posixpath
import http.server
import socketserver
import urllib.request, urllib.parse, urllib.error
import html
import shutil
import mimetypes
import re
import argparse
import base64
import socket

from io import BytesIO

def fbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

DEFAULT_ERROR_CONTENT_TYPE = "text/html;charset=utf-8"

class HTTPServer(socketserver.TCPServer):

    allow_reuse_address = 1    # Seems to make sense in testing environment

    def server_bind(self):
        """Override server_bind to store the server name."""
        socketserver.TCPServer.server_bind(self)
        host, port = self.server_address[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port


class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    daemon_threads = True

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
 
    """Simple HTTP request handler with GET/HEAD/POST commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method. And can reveive file uploaded
    by client.

    The GET/HEAD/POST requests are identical except that the HEAD
    request omits the actual contents of the file.

    """
 
    server_version = "SimpleHTTPWithUpload/" + __version__
 
    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()
 
    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.send_head()
        if f:
            f.close()
 
    def do_POST(self):
        """Serve a POST request."""
        r, info = self.deal_post_data()
        print((r, info, "by: ", self.client_address))
        f = BytesIO()
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b"<html>\n<title>Upload Result Page</title>\n")
        f.write(b'<style type="text/css">\n')
        f.write(b'* {font-family: Helvetica; font-size: 16px; }\n')
        f.write(b'a { text-decoration: none; }\n')
        f.write(b'</style>\n')
        f.write(b"<body>\n<h2>Upload Result Page</h2>\n")
        f.write(b"<hr>\n")
        if r:
            f.write(b"<strong>Success!</strong>")
        else:
            f.write(b"<strong>Failed!</strong>")
        f.write(info.encode('utf8'))
        f.write(("<br><br><a href=\"%s\">" % self.headers['referer']).encode("utf8"))
        f.write(b"<button>Back</button></a>\n")
        f.write(b"<hr><small>Powered By: httpserver4u<br>Check new version from the original creator (bones7456) ")
        f.write(b"<a href=\"https://gist.github.com/UniIsland/3346170\" target=\"_blank\">here</a>. <br>")
        f.write(b"Or from the creator of the version you're using now ")
        f.write(b"<a href=\"https://github.com/jerrylususu/simple_http_server_py\" target=\"_blank\">here</a>.")
        f.write(b"</small></body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def deal_post_data(self):
        uploaded_files = []   
        content_type = self.headers['content-type']
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")
        boundary = content_type.split("=")[1].encode("utf8")
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        foundText = False
        if not boundary in line:
            return (False, "Content NOT begin with boundary")
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
            fn_text = re.findall(r'Content-Disposition.*name="text"', line.decode())
            # first try text
            if fn_text:
                foundText = True
                fn = [TEXT_FILE_NAME]
            # try again for file
            if not fn:
                return (False, "Can't find out file name...")
            path = self.translate_path(self.path)
            fn = os.path.join(path, fn[0])
            if foundText:
                # always write text in root folder
                fn = TEXT_FILE_NAME
            line = self.rfile.readline()
            remainbytes -= len(line)
            if not foundText:
                line = self.rfile.readline()
                remainbytes -= len(line)
            try:
                if not foundText:
                    out = open(fn, 'wb')
                else:
                    out = open(fn, 'w', encoding="utf8")
            except IOError as e:
                print("IOError when writing file:", e)
                return (False, "<br><br>Can't create file to write.<br>Do you have permission to write?")
            else:
                with out:  
                    preline = self.rfile.readline()
                    remainbytes -= len(preline)
                    while remainbytes > 0:
                        line = self.rfile.readline()
                        remainbytes -= len(line)
                        if boundary in line:
                            preline = preline[0:-1]
                            if preline.endswith(b'\r'):
                                preline = preline[0:-1]
                            if not foundText:
                                out.write(preline)
                            else:
                                out.write(urllib.parse.unquote(preline.decode('utf8')))
                            uploaded_files.append(fn)
                            break
                        else:
                            if not foundText:
                                out.write(preline)
                            else:
                                out.write(preline.decode('utf8'))
                            preline = line
        return (True, "<br><br>'%s'" % "'<br>'".join(uploaded_files))
 
    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        if path.endswith(TEXT_FILE_NAME):
            ctype = "text/plain; charset=utf-8"
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))

        self.end_headers()
        return f
 


    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        # enc = sys.getfilesystemencoding()
        enc = "utf8"
        list.sort(key=lambda a: a.lower())
        f = BytesIO()
        displaypath = html.escape(urllib.parse.unquote(self.path))
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b'<html>\n')
        f.write(('<meta http-equiv="Content-Type" '
                 'content="text/html; charset=%s">' % enc).encode(enc))
        f.write(("<title>Directory listing for %s</title>\n" % displaypath).encode(enc))
        f.write(b'<style type="text/css">\n')
        f.write(b'* {font-family: Helvetica; font-size: 16px; }\n')
        f.write(b'a { text-decoration: none; }\n')
        f.write(b'a:link { text-decoration: none; font-weight: bold; color: #0000ff; }\n')
        f.write(b'a:visited { text-decoration: none; font-weight: bold; color: #0000ff; }\n')
        f.write(b'a:active { text-decoration: none; font-weight: bold; color: #0000ff; }\n')
        f.write(b'a:hover { text-decoration: none; font-weight: bold; color: #ff0000; }\n')
        f.write(b'table {\n  border-collapse: separate;\n}\n')
        f.write(b'th, td {\n  padding:0px 10px;\n}\n')
        f.write(b'</style>\n')
        f.write(("<body>\n<h2>Directory listing for %s</h2>\n" % displaypath).encode(enc))
        f.write(b"<hr>\n")
        if displaypath == "/":
            f.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
            f.write(("text file: /%s <br>" % TEXT_FILE_NAME).encode("utf8"))
            f.write(b"<input type=\"button\" value=\"clear\" onclick=\"javascript:eraseText()\"/><br>\n")
            f.write(b"<textarea name=\"text\" placeholder=\"text here\" rows=\"5\" cols=\"50\" id=\"textinput\" >")
            if os.path.exists(TEXT_FILE_NAME):
                with open(TEXT_FILE_NAME, "r", encoding="utf8") as text_file:
                    text_content = text_file.read()
                    f.write(text_content.encode("utf8"))
            f.write(b"</textarea><br>")
            f.write(b"<input type=\"submit\" value=\"save text\"/></form>\n")
            f.write(b"<hr>\n")
        f.write(b"<form ENCTYPE=\"multipart/form-data\" method=\"post\">")
        f.write(b"<input name=\"file\" type=\"file\" multiple/>")
        f.write(b"<input type=\"submit\" value=\"upload\"/></form>\n")
        f.write(b"<hr>\n")
        f.write(b'<table>\n')
        f.write(b'<tr><td>(up)</td><td><a href="../" >Parent Directory</a></td></tr>\n')
        for name in list:
            dirimage = 'item'
            fullname = os.path.join(path, name)
            displayname = linkname = name
            fsize = fbytes(os.path.getsize(fullname))
            created_date = time.ctime(os.path.getctime(fullname))
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                dirimage = 'dir'
                displayname = name + "/"
                linkname = name + "/"
                fsize = ''
                created_date = ''
            if os.path.islink(fullname):
                dirimage = 'link'
                displayname = name + "@"
            if name.endswith(('.bmp','.gif','.jpg','.png')):
                dirimage = 'image'
            if name.endswith(('.avi','.mpg')):
                dirimage = 'video'
            if name.endswith(('.idx','.srt','.sub')):
                dirimage = 'subtitle'
            if name.endswith('.iso'):
                dirimage = 'iso'
                # Note: a link to a directory displays with @ and links with /
            f.write(('<tr><td>%s</td><td><a href="%s">%s</a></td><td style="text-align:right; font-weight: bold; color:#FF0000">%s</td><td style="text-align:right; font-weight: bold;">%s</td></tr>\n'
                    % ( dirimage, urllib.parse.quote(linkname), html.escape(displayname) , fsize , created_date )).encode(enc))
        f.write(b"</table><hr>\n</body>\n")
        if displaypath == "/":
            f.write(b'<script>function eraseText() {document.getElementById("textinput").value = "";}</script>')
        f.write(b"</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        # abandon query parameters
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]
        path = posixpath.normpath(urllib.parse.unquote(path))
        words = path.split('/')
        words = [_f for _f in words if _f]
        path = os.getcwd()
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path
 
    def copyfile(self, source, outputfile):
        """Copy all data between two file objects.

        The SOURCE argument is a file object open for reading
        (or anything with a read() method) and the DESTINATION
        argument is a file object open for writing (or
        anything with a write() method).

        The only reason for overriding this would be to change
        the block size or perhaps to replace newlines by CRLF
        -- note however that this the default server uses this
        to copy binary data as well.

        """
        shutil.copyfileobj(source, outputfile)
 
    def guess_type(self, path):
        """Guess the type of a file.

        Argument is a PATH (a filename).

        Return value is a string of the form type/subtype,
        usable for a MIME Content-type header.

        The default implementation looks the file's extension
        up in the table self.extensions_map, using application/octet-stream
        as a default; however it would be permissible (if
        slow) to look inside the data to make a better guess.

        """
 
        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']
 
    if not mimetypes.inited:
        mimetypes.init() # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream', # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
        })



def test(host="0.0.0.0", port=8000, text_filename="simple_python_server_text.txt"):
    """Test the HTTP request handler class.
    This runs an HTTP server on port 8000 (or the port argument).
    """
    global TEXT_FILE_NAME
    TEXT_FILE_NAME = text_filename
    with ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler) as httpd:
        host, port = httpd.socket.getsockname()[:2]
        url_host = f'[{host}]' if ':' in host else host
        print(
            f"Serving HTTP on {host} port {port} "
            f"(http://{url_host}:{port}/) ..."
        )
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                            help='Specify alternate bind address '
                                '[default: all interfaces]')
    parser.add_argument('port', action='store',
                            default=8000, type=int,
                            nargs='?',
                            help='Specify alternate port [default: 8000]')
    parser.add_argument('--text_filename', type=str,
                            default='simple_python_server_text.txt',
                            help='File name for the text file (to store the memo). '
                            '[default: simple_python_server_text.txt]')
    args = parser.parse_args()

    PORT = args.port
    BIND = args.bind
    HOST = BIND
    TEXT_FILE_NAME = args.text_filename

    if HOST == '':
        HOST = '0.0.0.0'

    test(
            host=HOST,
            port=PORT,
            text_filename = TEXT_FILE_NAME,
        )

if __name__ == "__main__": 
    parse_arguments()