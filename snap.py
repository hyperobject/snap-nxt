import SimpleHTTPServer
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
	path = self.translate_path(self.path)
	print path
	ospath = os.path.abspath('')
	if path == ospath + '/nxtfull360a': #motor a
		m_a.turn(100, 360)
	elif path == ospath + '/nxthalf360a':
		m_a.turn(50, 360)
	elif path == ospath + '/nxtfull180a':
		m_a.turn(100, 180)
	elif path == ospath + '/nxthalf180a':
		m_a.turn(50, 180)
	elif path == ospath + '/nxtfull90a':
		m_a.turn(100, 90)
	elif path == ospath + 'nxthalf90a':
		m_a.turn(50, 90)
	elif path == ospath + '/nxtfull360b': #motor B
		m_b.turn(100, 360)
	elif path == ospath + '/nxthalf360b':
		m_b.turn(50, 360)
	elif path == ospath + '/nxtfull180b':
		m_b.turn(100, 180)
	elif path == ospath + '/nxthalf180b':
		m_b.turn(50, 180)
	elif path == ospath + '/nxtfull90b':
		m_b.turn(100, 90)
	elif path == ospath + 'nxthalf90b':
		m_b.turn(50, 90)
	elif path == ospath + '/nxtfull360c': #motor C
		m_c.turn(100, 360)
	elif path == ospath + '/nxthalf360c':
		m_c.turn(50, 360)
	elif path == ospath + '/nxtfull180c':
		m_c.turn(100, 180)
	elif path == ospath + '/nxthalf180c':
		m_c.turn(50, 180)
	elif path == ospath + '/nxtfull90c':
		m_c.turn(100, 90)
	elif path == ospath + 'nxthalf90c':
		m_c.turn(50, 90)
	elif path == ospath + '/nxttouch': #touch
		f = open(ospath + '/return', 'w+')
		f.write(str(t.get_sample()))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == ospath + '/nxtsound': #sound
		f = open(ospath + '/return', 'w+')
		f.write(str(s.get_sample()))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == ospath + '/nxtlight': #light
		f = open(ospath + '/return', 'w+')
		f.write(str(l.get_sample()))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	elif path == ospath + '/nxtultrasonic': #ultrasonic
		f = open(ospath + '/return', 'w+')
		f.write(str(u.get_sample()))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
	else:
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
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()
	        return f
		print 'OK'


if __name__ == "__main__":
    import os
    import SocketServer
    import nxt.locator
    from nxt.motor import *
    from nxt.sensor import *
    b = nxt.locator.find_one_brick()
    try:
    	t = Touch(b, PORT_1)
    except:
    	pass
    try:
    	s = Sound(b, PORT_2)
    except:
    	pass
    try:
    	l = Light(b, PORT_3)
    except:
    	pass
    try:
    	u = Ultrasonic(b, PORT_4)
    except:
    	pass
    m_a = Motor(b, PORT_A)
    m_b = Motor(b, PORT_B)
    m_c = Motor(b, PORT_C)
    P2ORT = 1330

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()

