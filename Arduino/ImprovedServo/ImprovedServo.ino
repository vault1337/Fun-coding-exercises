unsigned long startTime;
unsigned long calculationTime;

void setup() {
  Serial.begin(115200);
  Serial.println("Start...");
  pinMode(13, OUTPUT);
  
  startTime = micros();
  for(int adc = 0; adc < 1024; adc++)
  {
    int servoSignal = map(adc, 0, 1023, 180, 0);
    digitalWrite(13, servoSignal > 0);  
  }
  calculationTime = micros() - startTime;
  Serial.print("Map:\t");
  Serial.println(calculationTime);


  startTime = micros();
  float floatFactor = 180.0 / 1023;
  for(int adc = 0; adc < 1024; adc++)
  {
    int servoSignal = 180 - (adc * floatFactor);
    digitalWrite(13, servoSignal > 0);  
  }
  calculationTime = micros() - startTime;
  Serial.print("Float:\t");
  Serial.println(calculationTime);

  startTime = micros();
  int intFactor = 45;
  int shiftCount = 8;
  for(int adc = 0; adc < 1024; adc++)
  {
    int servoSignal = 180 - ((adc * intFactor) >> shiftCount);
    digitalWrite(13, servoSignal > 0);  
  }
  calculationTime = micros() - startTime;
  Serial.print("Shift:\t");
  Serial.println(calculationTime);
}

void loop() {

}
