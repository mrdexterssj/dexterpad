# Dexterpad

<img width="541" height="650" alt="image" src="https://github.com/user-attachments/assets/d6c31944-0840-4087-af08-dda6356351b4" />

A custom macropad with the looks! Built for Half Life@11/26 #YSWS

## Features

* 9 customizable Cherry MX keys with keycaps
* A rotary encoder (volume and play/pause)
* A 1x4 pinheader to connect a physical button in the future 
* Kmk (circuitpython) firmware
* LEDs to display the current layer (soon)

## Firmware description

The firmware was written in python (circuitpython) using the kmk libraries. This allowed me to easily add features such as keyboard matrix scan, status LEDs, custom keybindings and rotary encoder functionality easily. I also edited one of the built-in extensions to make it work with 4 LEDs instead of 3. The firmware can be found inside /firmware.

## BOM Table

|Item                                          |Qty|Supplier |Cost/item|Total Cost|link                                                                                                                                          |
|----------------------------------------------|---|---------|---------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
|Waveshare ESP32-S3-Zero                       |1  |Waveshare|$5.49    |$5.49     |https://www.waveshare.com/esp32-s3-zero.htm?sku=25081                                                                                         |
|RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm|1  |Temu     |$1.21    |$1.21     |https://www.temu.com/ec/1pc-accesorio-de-robot-s----rotatorio-ec11-potenciometro-digital-para-altavoz-con--5-pines-20mm-g-606209147009488.html|
|Estimated total shipping                      |1  |         |         |$10.00    |                                                                                                                                              |

## Screenshots

<img width="541" height="650" alt="image" src="https://github.com/user-attachments/assets/d6c31944-0840-4087-af08-dda6356351b4" />

_Front render_

<img width="541" height="650" alt="image" src="https://github.com/user-attachments/assets/49175b6a-245e-4ae9-a21e-dbb56657f3f1" />

_Back render_

<img width="462" height="494" alt="image" src="https://github.com/user-attachments/assets/c9258be9-d32c-4460-aae6-3d5a0bae713c" />

_PCB_

<img width="911" height="606" alt="image" src="https://github.com/user-attachments/assets/8a73b53a-53d3-45aa-aaf2-3917c063c5d2" />

_Schematic_


