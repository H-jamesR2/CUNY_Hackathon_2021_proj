int radius = 15;
int direction = 1;
int direction2 = 0;
int score = 0; 
float x = 0;
float y = 0;
 
ArrayList<Particle> poop = new ArrayList();
 
void setup() {
  size(500, 500);
  ellipseMode(RADIUS);
  for (int i=0; i<50; i++) {
    Particle P = new Particle((int)random(width), (int)random(height));
    poop.add(P);
  }
}
 
void draw() {
  background(255);
  int msElapsed = millis();
  float secsElapsed = floor(msElapsed / 1000); 
  stroke(1, 1, 1);
  textSize(18);
  fill(1, 1, 1);
  text("Time Elapsed: " + secsElapsed + "s", width/2, height/2);
  text("Score: " + score, width/2, height/3);
  
  if (secsElapsed > 15) { 
    text("TIME IS RUNNING OUT", width/2, height/2 + 100);
  } 
  
  /*if (secsElapsed % 3 == 0) {
    x = random(width);
    y = random(height);
    
  }*/ 
  fill(30, 30, 120); 
  circle(x, y, 30);
  fill (0, 175, 255);
  smooth ();
  noStroke();
  render();
 
  for (int i=0;i<poop.size();i++) {
    Particle Pn = (Particle) poop.get(i);
    Pn.display();
    if (dist(x, y, Pn.x, Pn.y)<radius) {
      poop.remove(i);
      score = score+1;
    }
  }
}
 
class Particle {
  int x, y;
  Particle(int x, int y) {
    this.x = x;
    this.y = y;
  }
  void display() {
    noStroke();
    fill(#FCA900);
    ellipse(x, y, 10, 10);
  }
}
 
 
void keyPressed() {
  if (key == CODED) {
    if (keyCode == LEFT) {
      x = x - 10;
      direction = -1;
      direction2 = 0;
    }
    else if (keyCode == RIGHT) {  
      x = x + 10;
      direction = 1;
      direction2 = 0;
    }
    else if (keyCode == UP) {
      y = y - 10;
      direction = 0;
      direction2 = -1;
    }
    else if (keyCode == DOWN) { 
      y = y + 10;
      direction = 0;
      direction2 = 1;
    }
  }
}
 
 
void render() {
  for ( int i=-1; i < 2; i++) {
    for ( int j=-1; j < 2; j++) {
      pushMatrix();
      translate(x + (i * width), y + (j*height));
      if ( direction == -1) { 
        rotate(PI);
      }
      if ( direction2 == 1) { 
        rotate(HALF_PI);
      }
      if ( direction2 == -1) { 
        rotate( PI + HALF_PI );
      }
      arc(0, 0, radius, radius, map((millis() % 500), 0, 500, 0, 0.52), map((millis() % 500), 0, 500, TWO_PI, 5.76) );
      popMatrix();
      // mouth movement //
    }
  }
}
    
