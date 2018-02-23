from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO,send, emit
#from model import User_lista, db
import json
#import pdb
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
mongo = PyMongo(app)

#db = SQLAlchemy(app)
socketio = SocketIO(app)

def saber_ip():
	if request.headers.getlist("X-Forwarded-For"):
		ip = request.headers.getlist("X-Forwarded-For")[0]
	else:
		ip = request.remote_addr
	return ip


@app.route('/cargar_db',methods=['GET'])
def cargar_db():
	#compruebo y creo collection video
	if (mongo.db.video.find({})):
		#consulto si existe 0 = false, 1 = true
		if(mongo.db.video.count({'_id': '1'})):
			#si existe cambia la lista
			lista = ['soy', 'la', 'nueva', 'lista2']
			#obtengo datos de db, y cambio lista
			mongo.db.video.replace_one({"_id":"1"}, {"lista":lista})
		else:
			# si no existe crea la lista
			mongo.db.video.insert_one({"_id":"1"})
			mongo.db.video.replace_one({"_id":"1"}, {"lista":["hello","world"]})
	else:
		mongo.db.create_collection("video")
	#obtengo la lista actualizada
	list_videos = mongo.db.video.find_one_or_404({'_id': '1'})
	#retorno la lista actualizada
	return json.dumps(list_videos["lista"])



@app.route('/doy_json', methods=['GET'])
def doy_json():
    #obtiene lista y manda
    lista_video = mongo.db.producto.find_one_or_404({'id': '1'})
    print lista_video["lista"]
    return lista_video["lista"]

"""
@app.route('/producto/<id>',methods=['GET'])
def index(id):
	producto = mongo.db.producto.find_one_or_404({'codigo': id})
	return render_template('index.html', 
							pro = producto,
							title = producto['title'],
							link = producto['link_images'],
							code = producto['codigo'] )
"""

"""
SOCKETS
"""
"""
@socketio.on("recibo")
def handle_recibo(msg):
    print 'hola soy msg',msg


@socketio.on("url")
def handle_recibo(url, valor):
	#retorna la ip
	if request.headers.getlist("X-Forwarded-For"):
		ip = request.headers.getlist("X-Forwarded-For")[0]
	else:
		ip = request.remote_addr
	#trae un objeto de la ip y none si no hay	
	existo = User_ip.query.filter_by(ip=ip).first()
	#confirma si existe o no y si, no existe guarda
	if existo == None:
		db.session.add(User_ip(ip=ip, url=url['href']))
		db.session.commit()
	print "hola soy ip ",ip
	print 'hola soy url',url['href']
	emit('recibo_url', url['href'])

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on("actu_list")
def handle_recibo(json_videos):
	list_videos = User_lista.query.filter_by(id=1).first()
	list_videos.lista = json_videos
	db.session.commit()
	db.session.close()
	list_videos = User_lista.query.filter_by(id=1).first()
	print "###", list_videos.lista
	db.session.close()

@socketio.on("connect")
def handle_connection():
	print("Someone is here!")
	list_videos = User_lista.query.filter_by(id=1).first()
	if len(list_videos.lista) == 0:
		video_files = ['soy', 'el', 'pajaro']
	else:
	 	video_files = list_videos.lista 
	db.session.close()
	print video_files
	emit("lista", json.dumps(video_files))




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/1')
def index1():
	lista = json.dumps(['hola', 'que', 'tal'])
	return lista

@app.route('/2')
def index2():
	ip = saber_ip()
	return ip 




@app.route("/play", methods=["GET"])
def play():
	if request.headers.getlist("X-Forwarded-For"):
		ip = request.headers.getlist("X-Forwarded-For")[0]
	else:
		ip = request.remote_addr

	existo = User_ip.query.filter_by(ip=ip).first()
	print existo
	if existo == None:
		print 'no existo'
	else:
		db.session.add(User_ip(ip=ip, url='www.lala.com', valor='jaja'))
		db.session.commit()
		print 'guarde'
	return render_template('play.html', 
						variable =str({'ip': ip , 'nombre': 'aqui estara el nombre'}))






@app.route('/hola')
def hola():
	list_videos = User_lista.query.filter_by(id=1).first()
	print list_videos.lista
	db.session.commit()
	db.session.close()
	return "mira"

@app.route('/hola2')
def hola2():
	return render_template('hola2.html')

"""
if __name__ == '__main__':
    socketio.run(app, debug=True)

