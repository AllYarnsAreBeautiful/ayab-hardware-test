#include <Arduino.h>
#include "Wire.h"
#include "PacketSerial.h"

#include "board.h"

#define SERIAL_BAUDRATE 115200

#define HWSerial Serial0
#define USBSerial Serial

#define TXBUFFER_SIZE 16

#define CMD_DIGITAL_WRITE 0x01
#define CMD_DIGITAL_READ  0x02
#define CMD_I2C_WRITE     0x03
#define CMD_I2C_READ      0x04
#define CMD_BEEP          0x05

hw_timer_t* beeperTimer = NULL;

SLIPPacketSerial packetSerial;
uint8_t txBuffer[TXBUFFER_SIZE];

void onPacketReceived(const uint8_t* buffer, size_t size)
{
  switch (buffer[0]) {
    case CMD_DIGITAL_WRITE:
      digitalWrite(buffer[1], buffer[2] & 0x1);
      break;

    case CMD_DIGITAL_READ:
      txBuffer[0] = CMD_DIGITAL_READ;
      txBuffer[1] = (uint8_t) digitalRead(buffer[1]);
      packetSerial.send(txBuffer, 2);
      break;

    case CMD_I2C_WRITE:
      Wire.beginTransmission(buffer[1]);
      Wire.write(buffer[2]);
      Wire.write(buffer[3]);
      Wire.endTransmission();
      break;

    case CMD_I2C_READ:
      Wire.beginTransmission(buffer[1]);
      Wire.write(buffer[2]);
      Wire.endTransmission();
      Wire.requestFrom(buffer[1],(uint8_t) 1);
      if (Wire.available()) {
        txBuffer[0] = CMD_DIGITAL_READ;
        txBuffer[1] = (uint8_t) Wire.read();
        packetSerial.send(txBuffer, 2);
	    }
      break;

    case CMD_BEEP:
      // Configure the timer to run at 10kHz with number of periods from arg
      timerAlarm(beeperTimer, 100, true, txBuffer[1]);
      timerAlarmEnable(beeperTimer);
      break;

    default:
      break;
  }
}

void ARDUINO_ISR_ATTR beeperHandler(){
  digitalToggle(PIEZO);
}

void setup() {
  USBSerial.begin(SERIAL_BAUDRATE);

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

  // Default APB clock 80MHz so prescaler 80 -> 1MHz clock
  beeperTimer = timerBegin(0, 80, true);
  timerAttachInterrupt(beeperTimer, &beeperHandler, true);
  
  Wire.begin(MCP_SDA, MCP_SCL, 400000);

  packetSerial.setStream(&USBSerial);
  packetSerial.setPacketHandler(&onPacketReceived);
}

void loop() {
  packetSerial.update();
}