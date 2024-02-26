#include <Arduino.h>
#include <PacketSerial.h>
#include <Adafruit_MCP23X17.h>

#include "Wire.h"
#include "USB.h"
#include "USBCDC.h"
#include "board.h"

#define HWSerial Serial0
#define USBSerial Serial

uint16_t fixSolenoidOrdering(uint16_t);
void testSolenoids();
void testSolenoid();

void testEOL();

void testEncoder();
void testBeltShift();

void testLEDs();
void testButton();

Adafruit_MCP23X17 mcp_handle; 

void setup() {
  USBSerial.begin();
  USB.begin();

  pinMode(LED_B, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);

  digitalWrite(LED_B, HIGH);
  digitalWrite(LED_R, HIGH);
  digitalWrite(LED_G, HIGH);
  
  pinMode(USER_BUTTON, INPUT);

  pinMode(ENC_A, INPUT);
  pinMode(ENC_B, INPUT);
  pinMode(ENC_C, INPUT);

  pinMode(EOL_L_N, INPUT);
  pinMode(EOL_L_S, INPUT);
  pinMode(EOL_R_N, INPUT);
  pinMode(EOL_R_S, INPUT);
  
  Wire.begin(MCP_SDA, MCP_SCL, 400000);
  mcp_handle.begin_I2C(0x00, &Wire);

  delay(1000);
  USBSerial.print("Starting hardware tests...\n");
  testLEDs();
  testButton();
  testBeltShift();
  testEncoder();
  testEOL();
  testSolenoids();
}

void loop() {
  digitalWrite(LED_R, LOW);
  delay(250);
  digitalWrite(LED_R, HIGH);
  digitalWrite(LED_G, LOW);
  delay(250);
  digitalWrite(LED_G, HIGH);
  digitalWrite(LED_B, LOW);
  delay(250);
  digitalWrite(LED_B, HIGH);
}

void testSolenoids(){
  USBSerial.print("Testing all solenoids...\n");

  uint16_t i;
  uint16_t pattern;

  for(i = 0; i < 0xFF; i++){
    pattern = fixSolenoidOrdering(i);
    mcp_handle.writeGPIOA((uint8_t)pattern);
    mcp_handle.writeGPIOB((uint8_t)(pattern >> 8));
    USBSerial.printf("Wrote pattern to solenoids: %04x\n", pattern);
    delay(10);
  }

  mcp_handle.writeGPIOAB(0x0000);
  USBSerial.print("Cleared pattern on solenoids.\n");
}

void testSolenoid(int solenoidNum){
  USBSerial.printf("Testing single solenoid: %i", solenoidNum);

  uint16_t pattern;

  pattern = fixSolenoidOrdering(1 << solenoidNum);
  mcp_handle.writeGPIOAB(pattern);
  USBSerial.printf("Wrote pattern to solenoids: %x\n", pattern);

  delay(100);

  mcp_handle.writeGPIOAB(0x0000);
  USBSerial.print("Cleared pattern on solenoids.\n");
}

uint16_t fixSolenoidOrdering(uint16_t pattern){
  uint16_t lowByte = pattern >> 8;
  uint16_t reversedByte = 0;

  uint8_t i;
  for(i=0; i < 8; i++){
    reversedByte |= ((pattern >> (7-i)) & 0x1);
    reversedByte <<= 1;
  }

  reversedByte <<= 8;

  return (reversedByte & lowByte);
}

void testEOL(void){
  USBSerial.print("Testing the end of line sensors.\n");
  uint8_t rightNorth = digitalRead(EOL_R_N);
  uint8_t rightSouth = digitalRead(EOL_R_S);
  uint8_t leftNorth = digitalRead(EOL_L_N);
  uint8_t leftSouth = digitalRead(EOL_L_S);

  USBSerial.printf("EOL L North: %i, South: %i, EOL R North: %i, South: %i\n", leftNorth, leftSouth, rightNorth, rightSouth);
}

void testEncoder(void){
  USBSerial.print("Testing the carriage movement encoder.\n");
  uint8_t encoderA = digitalRead(ENC_A);
  uint8_t encoderB = digitalRead(ENC_B);

  USBSerial.printf("Encoder A: %i\t Encoder B: %i\n", encoderA, encoderB);
}

void testBeltShift(void){
  USBSerial.print("Testing the belt phase sensor.\n");

  uint8_t beltPhase = digitalRead(ENC_C);

  USBSerial.printf("Belt phase state: %i\n", beltPhase);
}

void testLEDs(void){
  USBSerial.print("Testing LEDs...\n");

  digitalWrite(LED_R, LOW);
  digitalWrite(LED_G, LOW);
  digitalWrite(LED_B, LOW);
  USBSerial.print("Turned on all LEDs.\n");

  delay(250);

  digitalWrite(LED_R, HIGH);
  digitalWrite(LED_G, HIGH);
  digitalWrite(LED_B, HIGH);
  USBSerial.print("Turned off all LEDs.\n");
}

void testButton(void){
  USBSerial.print("Testing user button...\n");
  USBSerial.print("Please press the user button.\n");

  while(digitalRead(USER_BUTTON) != LOW){}

  USBSerial.print("User button pressed.\n");
}
