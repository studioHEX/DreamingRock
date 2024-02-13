#include "Arduino.h"
#include "WiFi.h"
#include <OSCMessage.h>

int randVal=0;
int ECG = 0;
int ECGVal = A0;
 
WiFiUDP Udp; // A UDP instance to let us send and receive packets over UDP
const IPAddress outIp(192,168,178,87); // your esp ip here
 
// Options
int update_rate = 16;
 
// Network settings
char ssid[] = "Roelie de Poes"; // your network SSID (name)
char pass[] = "nhraEevapsQ3";  // your network password
unsigned int localPort = 7777; // local port to listen for OSC packets
 
bool is_streaming = true;
 
void setup() {

pinMode(40, INPUT);
pinMode(41, INPUT);
  
  /* setup wifi */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
 Serial.begin(115200);
 Serial.println(WiFi.localIP());
  Udp.begin(localPort);
}
 
void sendOSC() {
  OSCMessage msg("/datafromespRand");
  OSCMessage msg1("/datafromespECG");
 
  // send some random values from 0 to 1
  //float _v1 = (sin(millis()*.01)+1.)*.5;
randVal=random(0, 1023);
ECG = analogRead(ECGVal);
  msg.add(randVal);
  msg.add(ECG);
  

   
  Udp.beginPacket(outIp, 7777);
  msg.send(Udp); // Send the bytes to the SLIP stream
  Udp.endPacket();  // Mark the end of the OSC Packet
  msg.empty();   // Free space occupied by message
  delay(10);
}
 
 
void receiveMessage() {
  OSCMessage inmsg;
  int size = Udp.parsePacket();
 
  if (size > 0) {
    while (size--) {
      inmsg.fill(Udp.read());
    }
//    if (!inmsg.hasError()) {
 //     inmsg.dispatch("/toggle_stream", stream_toggle);
  //} 
 
    
   
    //else { auto error = inmsg.getError(); }
  }
}
 
 
//void stream_toggle(OSCMessage &msg) {
 // switch (msg.getInt(0)) {
 // case 0:
 //  is_streaming=false;
  //  break;
 // case 1:
 //   is_streaming=true;
 //   break;
 // }
//}
 
 
 
 
void loop() {
 
     
sendOSC();
 
 
    receiveMessage();
    delay(10);
 
    
 
}
