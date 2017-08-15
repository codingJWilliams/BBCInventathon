var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/html/view.html');
});
app.get("/master/", function(req, res){
  res.sendFile(__dirname + "/html/lobby.html")
})
app.use(express.static('assets'))
io.on('connection', function(socket){
  console.log('a user connected');
  socket.on("start-connection", function(param){
    io.emit("thing-started")
    console.log("START")
  })
  socket.on("end-connection", function(param){
    io.emit("thing-ended")
    console.log("END")
  })
});

http.listen(4000, function(){
  console.log('listening on *:3000');
});
