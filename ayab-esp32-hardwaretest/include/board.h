#define MCP23017_ADDR_0 0x0U // I2C address of expander on ayab-esp32 (16-wide)

// Knitting machine control
#define EOL_R_N 3  // Right EOL marker, each polarity.
#define EOL_R_S 4

#define EOL_L_N 1  // Left EOL marker, each polarity.
#define EOL_L_S 2 

#define ENC_A 5    // Carriage movement A
#define ENC_B 6    // Carriage movement B
#define ENC_C 7    // Carriage belt phase alignment.

#define MCP_SDA 8  // Internal I2C bus with MCP GPIO expander.
#define MCP_SCL 9  // I2C0

// Communication busses
#define SPI_COPI 12 // Internal SPI bus for future display.
#define SPI_CIPO 11 // SPI0
#define SPI_SCK 13
#define SPI_CS 10

#define UART_TX 43  // External bus for debugging and/or user.
#define UART_RX 44  // UART0

#define I2C_SDA 15  // External bus for user applications.
#define I2C_SCL 16  // I2C1

// Misc I/O
#define LED_R 33  
#define LED_G 34   
#define LED_B 35    

#define PIEZO 38

// User I/O
#define USER_BUTTON 36

#define USER_14 14 // Should these actually be like USER_0... etc?
#define USER_17 17 // And then on the silk/ enclosure we put friendly numbers (0..8) instead of GPIO name?
#define USER_18 18
#define USER_21 21

#define USER_39 39
#define USER_40 40
#define USER_41 41
#define USER_42 42