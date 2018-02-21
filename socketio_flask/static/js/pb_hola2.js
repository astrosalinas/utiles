var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on("lista", (lista) => { //escucha en recibo_url
    console.log(lista);
    localStorage.setItem('lista', JSON.parse(lista));
}); 
