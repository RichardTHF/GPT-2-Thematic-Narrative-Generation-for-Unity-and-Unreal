import flask
from flask import request, jsonify
import gpt_2_simple as gpt2
import tensorflow as tf

app = flask.Flask(__name__)
app.config["DEBUG"] = False

run_name = 'pirates' # This is where you select the default thematic you want to select

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=run_name)


@app.route('/', methods=['GET'])
def home():
	return '''<h1>Game NLP Proccessing Engine</h1>
	<p>A prototype API for generating text naration during a videogame</p>'''

@app.route('/api/v1/speech', methods=['GET'])
def api_speach():
	global sess
	global run_name
	print("Entry")
	if 'speech' in request.args:
		speech = str(request.args['speech'])
		print("Got String: "+speech)

	else:
		return "Error: No speach field provided. Please specificy the imputted speach."

	if 'leng' in request.args:
		leng = str(request.args['leng'])
		length = int(leng)
		print("Got required length: " + leng)

	else:
		leng = 100
		length = int(leng)

	if 'style' in request.args:
		style = str(request.args['style'])
		print("Style: " + style)
		#Rename the run_name = '***' to name you gave the model you trained in the import / finetune stages of the process.
		if style == "vikings":
			tf.compat.v1.reset_default_graph()
			sess.close()
			sess = gpt2.start_tf_sess()
			run_name = 'vikings'
			gpt2.load_gpt2(sess, run_name=run_name)
		elif style == "scifi":
			tf.compat.v1.reset_default_graph()
			sess.close()
			sess = gpt2.start_tf_sess()
			run_name = 'scifi'
			gpt2.load_gpt2(sess, run_name=run_name)
		elif style == "pirates":
			tf.compat.v1.reset_default_graph()
			sess.close()
			sess = gpt2.start_tf_sess()
			run_name = 'pirates'
			gpt2.load_gpt2(sess, run_name=run_name)
		else:
			tf.compat.v1.reset_default_graph()
			sess.close()
			run_name = 'pirates'
			sess = gpt2.start_tf_sess()
			gpt2.load_gpt2(sess, run_name=run_name)


	trunc = None
	if 'trunc' in request.args:
		trunc = str(request.args['trunc'])
		print("Got Truncate Argument")

	results = []
	print("Predicting...")
	if trunc is not None:
		text = gpt2.generate(sess, run_name=run_name, length=length, prefix=speech, temperature=1.0, truncate = trunc, return_as_list=True, include_prefix=False)[0]
	else:
		text = gpt2.generate(sess, run_name=run_name, length=length, prefix=speech, temperature=1.0, return_as_list=True, include_prefix=False)[0]
	print("Text Predicted" + text)
	results.append(text)
	print("Compiling to JSON")
	return jsonify(results)
	print("Result Returned")


app.run(host='0.0.0.0', port=80, threaded=False)