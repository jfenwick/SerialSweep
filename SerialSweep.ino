/*
  SerialSweep
  Reads serial data until the null byte and turns that data into servo movement

*/
#include <Servo.h> 

Servo myservo;
char serialData[4];
int pos = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Ready");
  myservo.attach(9);
}

void loop() {
  if (Serial.available()) {
    Serial.readBytesUntil('\0', serialData, 4);
    pos = atoi(serialData);
    
    myservo.write(pos);
    memset(serialData, '\0', 4);
  }
}
