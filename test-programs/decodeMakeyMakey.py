from evdev import InputDevice, categorize, ecodes
import os
import sys

if __name__ == '__main__':

  if os.path.islink('/dev/input/by-id/usb-JoyLabz_Makey_Makey_v1.20aa_50000000-event-kbd'):
    dev = InputDevice('/dev/input/by-id/usb-JoyLabz_Makey_Makey_v1.20aa_50000000-event-kbd')
  elif os.path.islink('/dev/input/by-id/usb-Arduino_LLC_Arduino_Leonardo-if02-event-mouse'):
    dev = InputDevice('/dev/input/by-id/usb-Arduino_LLC_Arduino_Leonardo-if02-event-mouse')
  else:
    print "No MakeyMakey/Arduino Leonardo found:-("
    sys.exit(1)

  for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
      if event.code == ecodes.KEY_W:
        print "w"
      elif event.code == ecodes.KEY_A:
        print "a"
      elif event.code == ecodes.KEY_S:
        print "s"
      elif event.code == ecodes.KEY_D:
        print "d"
      elif event.code == ecodes.KEY_F:
        print "f"
      elif event.code == ecodes.KEY_G:
        print "g"
      elif event.code == ecodes.KEY_UP:
        print "UP" 
      elif event.code == ecodes.KEY_DOWN:
        print "DOWN" 
      elif event.code == ecodes.KEY_LEFT:
        print "LEFT" 
      elif event.code == ecodes.KEY_RIGHT:
        print "RIGHT" 
      elif event.code == ecodes.KEY_UP:
        print "UP" 
      elif event.code == ecodes.KEY_SPACE:
        print "SPACE"
      else:
        print(event)
        print(categorize(event))
#    else:
#      print(event)
#      print(categorize(event))
