// Two textile sensing zones on a XIAO ESP32-S3.
// Each zone: one snap to an analogue pin held INPUT_PULLUP, the other snap to a digital pin held LOW.
// Prints "value1,value2" per line so logging/readData.py can write Timestamp,Analog1,Analog2.

#define bicepInPin A0   // analogue-capable pin
#define bicepOutPin 2   // digital pin, held LOW

#define kneeInPin A1    // analogue-capable pin
#define kneeOutPin 3    // digital pin, held LOW

int sensorBicepValue = 0;
int sensorKneeValue = 0;

void setup() {
  Serial.begin(115200);

  pinMode(bicepInPin, INPUT_PULLUP);
  pinMode(bicepOutPin, OUTPUT);
  digitalWrite(bicepOutPin, LOW);

  pinMode(kneeInPin, INPUT_PULLUP);
  pinMode(kneeOutPin, OUTPUT);
  digitalWrite(kneeOutPin, LOW);
}

void loop() {
  sensorBicepValue = analogRead(bicepInPin);
  sensorKneeValue = analogRead(kneeInPin);

  Serial.print(sensorBicepValue);
  Serial.print(",");
  Serial.println(sensorKneeValue);

  delay(100);
}
