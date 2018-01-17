# running my application

from flask import Flask

from newsDB import q1, q2, q3

app = Flask(__name__)

HTML_WRAP = '''
<!DOCTYPE html>
<html>
  <head>
    <title>News Data</title>
  </head>
  <body>
    <h1>News Data Project</h1>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

@app.route('/', methods=['GET'])
def main():
	# Returning the data
	data = ",".join(str(v) for v in q1())
	html = HTML_WRAP % data
	return html

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)