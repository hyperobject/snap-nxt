import SimpleHTTPServer
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
	print path
	ospath = os.path.abspath('')
	if 'move' in path:
		regex = re.compile("\/move([abc])0([0-9]+)0([0-9]+)0([+-])")
		m = regex.match(path)
		if m.group(4) == '-':
			power = -1 * int(m.group(2))
		elif m.group(4) == "+":
			power = int(m.group(2))
		degrees = int(m.group(3))
		motor = m.group(1)
		if motor == "a":
			m_a.turn(power, degrees)
		elif motor == "b":
			m_b.turn(power, degrees)
		if motor == "a":
			m_a.turn(power, degrees)
	elif 'tone' in path:
		regex = re.compile('\/tone([0-9]{1,})a([0-9]{1,})')
		m = regex.match(path)
		tone = int(m.group(1))
		time = int(m.group(2))
		print time
		print tone
		b.play_tone_and_wait(tone, time)
	elif path == '/nxttouch': #touch
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
	elif path == '/nxtsound': #sound
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
	elif path == '/nxtlight': #light
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
	elif path == '/nxtultrasonic': #ultrasonic
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

if __name__ == "__main__":
    import re
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
    PORT = 1330 #N reminded me of 13, X in Roman numerals is 10, and T is the 20th letter. I added X and T together.

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()

