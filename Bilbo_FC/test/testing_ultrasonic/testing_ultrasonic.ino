/*
  Author:
  Date
  Summary: Test HC-SR04 to confirm the measurements taken are correct.
  Test case: Read signals from the sensor. Server will get the serial data with values and will evalauate based on a specific distance
  which was predetermined. If the 5 secs of readings, the values where within X - Y then the test pass
*/

#define PIN_ECHO    (4)  //D4
#define PIN_TRIGGER (2)  //D2
#define LED_GREEN   (X)   //DX

float duration, distance;

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing ultrasonic test");
  pinMode(PIN_TRIGGER, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  pinMode(LED_GREEN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(PIN_TRIGGER, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIGGER, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIGGER, LOW);

  duration = pulseIn(PIN_ECHO, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(300);
  if(distance <= 30)
  {
    digitalWrite(LED_GREEN, HIGH);
  }
  else
  {
    digitalWrite(LED_GREEN, LOW);
  }
}
