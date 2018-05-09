// install bcm2835_v4l2 in /etc/modules-load.d/modules.conf

var capture;

function setup() {
  createCanvas(640, 480);
  capture = createCapture(VIDEO);
  //capture.size(320, 240);
  capture.hide();
}

function draw() {
  background(255);
  image(capture, 0, 0, 640, 480);
  filter('INVERT');
}
