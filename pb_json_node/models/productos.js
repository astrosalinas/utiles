var Schema = require('mongoose').Schema
 
var producto_schema = new Schema({
  codigo        :   Number,
  title        :   String,
  description  :   String,
  link_images  :   String,
  price        :   String,
  stock        :   Boolean,
})
 
module.exports = producto_schema
