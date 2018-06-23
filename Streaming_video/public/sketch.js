var capture;
var socket;

function setup() {
  createCanvas(400, 320);
  background(200);
  // Webcam
  capture = createCapture(VIDEO);
  //capture.size(320, 240);
  capture.hide();

  //socket = io.connect('http://localhost:8080');
  //socket = io.connect('https://localhost:8080', {secure: true});
}

function draw() {
  image(capture, 40, 40, 320, 240);
}
