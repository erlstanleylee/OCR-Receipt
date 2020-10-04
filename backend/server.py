from flask import Flask, redirect, url_for, request, jsonify, render_template
app = Flask(__name__)

import time

import logging
import pyrebase

#try:
#    from PIL import Image
#except ImportError:
#    import Image

config = { 
	"apiKey": "AIzaSyBOyikj14f1BWinF96CMO96lS-3ZaNtL-0",
	"authDomain": "receipt-24ad6.firebaseapp.com",
	"databaseURL": "https://project-1067210456275.firebaseio.com",
	"storageBucket": "receipt-24ad6.appspot.com",
	"serviceAccount":"receipt-24ad6-firebase-adminsdk-qoj51-62596cba24.json"
}

firebase = pyrebase.initialize_app(config)

#auth = firebase.auth()
#user = auth.sign_in_with_email_and_password("", "itiswednesday")


def getwords(img):
	try:
		from PIL import Image
	except ImportError:
		import Image
	import pytesseract
	import re
	#you have to change the path below to the absolute path of the tesseract program
	
	pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract' 
		
	UnfilteredString = pytesseract.image_to_string(Image.open(img)) #name of the picture you want to analyze
	
	print("Unfiltered:")
	print(UnfilteredString)
	
	print("Filtered:")
	FilteredList = re.findall(".*\.[0-9]{2}\n", UnfilteredString)
	print(FilteredList)
	for n, entry in enumerate(FilteredList):
		FilteredList[n] = re.sub("\$.+\n", "", entry)
		print(FilteredList[n])
	return(FilteredList)


@app.route('/', methods=['GET','POST'])
def fp():
    if request.method == 'POST':
        img = request.files['file']
        filtereditems = getwords(img)
        itemstring = '\n'.join(filtereditems)
        return redirect(url_for('data', items = itemstring))
		
@app.route('/data')
def data():
	items = request.args.get('items')
	print(items)
	items = items.split('\n')
	return render_template('display.html', items=items)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
