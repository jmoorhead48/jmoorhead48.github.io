function setup() {
  createCanvas(600, 400);
  background(0);
}
function draw() {
  if (mouseIsPressed) {
    fill(random(250),random(200),random(200),random(100));
  }
  else {
    fill(random(500),random(300),random(300),random(300));
  }
    rect(random(600),random(600),random(20,50),random(20,50));
}
