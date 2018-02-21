var socket = io.connect('http://' + document.domain + ':' + location.port);


var lista = ['soy', 'lista', 'actualizada'];
console.log(lista);
socket.emit('actu_list', JSON.stringify(lista)); //envio lista en format json
//localStorage.setItem('lista', JSON.parse(lista));
