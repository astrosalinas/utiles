 $.ajax({
    url: 'http://127.0.0.1:5000/1',
    dataType: 'application/json',
    complete: function(data){
        console.log(data)
    }});


function prueba(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET","http://127.0.0.1:5000/1");
	xhr.send();
	xhr.onreadystatechange = function() {
	    if(xhr.readyState == 4 && xhr.status == 200){
	        console.log(xhr.responseText);
	    }
	}
}