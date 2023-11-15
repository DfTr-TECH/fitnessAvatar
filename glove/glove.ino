#define TX 10
#define RX 11

#include <SoftwareSerial.h>
#include <Wire.h>
#include <MAX30105.h>
#include <heartRate.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
SoftwareSerial BTmodule(RX, TX);
MAX30105 pulse;

long timer1 = 0;
long lastBeat = 0;
int BPM_raw = 0;
int BPM = 0;
int ball_system = 0;
void setup() {

  BTmodule.begin(9600);
  Serial.begin(9600);
  pulse.begin();
  pulse.setup();
  accel.begin();

  accel.setRange(ADXL345_RANGE_16_G);
  pulse.setPulseAmplitudeRed(0x0A);

}

void loop() {

  sensors_event_t event; 
  accel.getEvent(&event);
 
  float x = event.acceleration.x;
  float y = event.acceleration.y;
  double acc = abs(sqrt((x*x)+(y*y)-2*x*y*(y/x)));

 
  if (checkForBeat(pulse.getRed()) == true) {

    long deltaBeat = millis() - lastBeat;
    lastBeat = millis();
    BPM_raw = 60 / (deltaBeat / 1000.0);
  }
  if ((millis()-timer1) > 1000) {
    timer1  = millis();
    BPM = BPM_raw;
    BTmodule.println(BPM_raw);
    //Serial.println(BPM_raw);
    //Serial.println(acc);
  }

  if ((acc > 6) and (BPM >= 80)) {
    ball_system++;
    //Serial.print("score= ");
    Serial.println(ball_system);
  } 
}
