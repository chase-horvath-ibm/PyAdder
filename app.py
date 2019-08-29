from flask import Flask, request, Response
from datetime import datetime
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
	   "<b>You have just accessed you containerized Python api.<br>" \
           "<b>The host container who served this up is:</b> {hostname}<br/>" \
           "<b>This reply was generated at: </b> {nowtime}<br/>"
    return html.format(name=os.getenv("whoBuilt"), hostname=socket.gethostname(), \
                nowtime=datetime.now())

@app.route("/xml")
def xml():
    xmlresponse = \
        '''<?xml version="1.0" encoding="UTF-8"?>
        <breakfast_menu>
        <food>
            <name>Belgian Waffles</name>
            <price>$5.95</price>
            <description>
           Two of our famous Belgian Waffles with plenty of real maple syrup
           </description>
            <calories>650</calories>
        </food>
        <food>
            <name>Strawberry Belgian Waffles</name>
            <price>$7.95</price>
            <description>
            Light Belgian waffles covered with strawberries and whipped cream
            </description>
            <calories>900</calories>
        </food>
        <food>
            <name>Berry-Berry Belgian Waffles</name>
            <price>$8.95</price>
            <description>
            Belgian waffles covered with assorted fresh berries and whipped cream
            </description>
            <calories>900</calories>
        </food>
        <food>
            <name>French Toast</name>
            <price>$4.50</price>
            <description>
            Thick slices made from our homemade sourdough bread
            </description>
            <calories>600</calories>
        </food>
        <food>
            <name>Homestyle Breakfast</name>
            <price>$6.95</price>
            <description>
            Two eggs, bacon or sausage, toast, and our ever-popular hash browns
            </description>
            <calories>950</calories>
        </food>
        </breakfast_menu> '''
    return Response(xmlresponse, mimetype='text/xml')

@app.route("/add")
def add():
    return str(int(request.args.get('num1')) + int(request.args.get('num2')))

@app.route("/PyAdder", methods=['GET', 'POST'])
def PyAdder():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        theanswer = str(int(num1)+int(num2))
        hostname = socket.gethostname()
        nowtime = datetime.now()
        html = '''<form method == "GET">
            {printanswer}<br>
            <input type="submit" value="Reset"><br><br><br>
            The host container who served this up is:</b> {hostname}<br>
            This reply was generated at: </b> {nowtime}<br/>
        </form>'''
        return html.format(printanswer=theanswer, nowtime=nowtime, hostname=hostname)

    return '''<form method="POST">
        Welcome to PyAdder.<br>
        Enter two numbers that you want to add together.<br>
        First_Number: <input type="text" name="num1"><br>
        Second_Number: <input type="text" name="num2"><br>
        <input type="submit" value="Submit"><br><br><br>
        
        This application maintained by chase.horvath@ibm.com<br>
        Git repo: https://github.com/chase-horvath-ibm/PyAdder<br>
   </form> '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
