import os, json
from flask import Flask, request, Response, send_file, make_response, jsonify
from flask import render_template, url_for, redirect, send_from_directory
from werkzeug import secure_filename
from imanip import app, helpers

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def get_index():
	return make_response(open('imanip/templates/index.html').read())

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		print "in POST"
		effects = request.form['effects']
		effects = json.loads(effects)
		file = request.files['file']
		print file
		if file and allowed_file(file.filename):
			filename = helpers.name_gen(secure_filename(file.filename))
			print filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			helpers.apply(os.path.join(app.config['UPLOAD_FOLDER'], filename), effects)
			return jsonify({ 'success': True, 'path': filename })
			return redirect(url_for('get_image', filename=filename))

@app.route('/image/<filename>')
def get_image(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

	