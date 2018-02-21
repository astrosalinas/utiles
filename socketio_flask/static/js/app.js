var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on("lista", (data) => {
    console.log(data);
});

socket.on("recibo_url", (url) => { //escucha en recibo_url
    console.log(url);

}); 

window.onbeforeunload = function (event) {
	var valor = 'True';
	if (window.location == 'http://127.0.0.1:5000/play'){
		valor = 'False';
	}
	socket.emit('url', window.location.href, valor); //envio a url
}

var valor = 'True';
socket.emit('url', window.location, valor); //envio a url


socket.send('hola'); //envio a menssage



socket.emit('recibo','soyemit'); //envio a recibo