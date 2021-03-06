const jsonlint = require("jsonlint");
const axios = require("axios");


const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
// Connection URL
const url_db = 'mongodb://localhost:27017';
// Database Name
const dbName = 'ejemplo';


const URL = "http:url_donde_tenga_json/produtos.json";


// Use connect method to connect to the server
MongoClient.connect(url_db, function(err, client) {
	assert.equal(null, err);
	console.log("Connected successfully to server");

	axios.get(URL).then(response => {
		
		var json = jsonlint.parse(JSON.stringify(response.data));
		if(json){	
			//obtengo codigo de los objeto 
			var codigo = Object.keys(json);
			const db = client.db(dbName);
			// Get the producto collection
			const collection = db.collection('producto');
			//for par agrupar los datos
			for (var i = 0; i < codigo.length; i++) {

				//guarda en valor el objeto de la clave en ese momento
				var valor = Object.keys(json[codigo[i]]);
				//obtengo en otro objeto el valor del objeto anterior
				var values_object = json[codigo[i]];
				// Get the producto collection
				const collection = db.collection('producto');
				// Insert some producto
				collection.insertMany([
					{	
						codigo: codigo[i],
						title: values_object[valor[0]], 
						description: values_object[valor[1]], 
						link_images: values_object[valor[2]], 
						price: values_object[valor[3]],
						stock:  values_object[valor[4]] 
					}
					]/*, function(err, result) {
						assert.equal(err, null);
						assert.equal(3, result.result.n);
						assert.equal(3, result.ops.length);
						console.log("Inserted 3 documents into the collection");
						callback(result);
					}*/);
			}
			var sali = 'sali';
			if (sali == 'sali'){
				client.close();
				console.log("termine ya sali");
			}	
		}		
	}).catch(e => console.log(e)); 
		
});
