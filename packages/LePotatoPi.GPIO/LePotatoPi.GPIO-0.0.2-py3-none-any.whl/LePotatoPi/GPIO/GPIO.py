import gpiod
from LePotatoPi.GPIO import consts
from LePotatoPi.GPIO import PulseWidthManagement as Pulse

class GPIO:
  used_pins = {}
  
  IN = 1
  OUT = 0

  BOARD = 10
  BCM = 11
  
  HIGH = 1
  LOW = 0

  PUD_OFF = 0
  PUD_DOWN = 1
  PUD_UP = 2

  def __init__(self):
    self.mode = self.BOARD
    self.chips = {
      "gpiochip0": gpiod.chip(consts.CHIP0),
      "gpiochip1": gpiod.chip(consts.CHIP1)
    }

  def setmode(self, mode):
    self.mode = mode
    
  
  def setup(self, pin, direction, pull_up_down=PUD_OFF, initial=None):
    mapped_pin = consts.LE_POTATO_PIN_TO_RPI_PIN[pin]

    print('checking for pin')
    if pin in self.used_pins:
      print('getting pin')
      p = self.used_pins[pin]
      print('releasing pin')
      p.release()
      print('pin released')
      print('deleting pin')
      del self.used_pins[pin]
      print('pin deleted')
      

    chip = self.chips[mapped_pin.chip]
    p = chip.get_line(mapped_pin.pin)
    bais = gpiod.line_request.FLAG_BIAS_DISABLE

    if pull_up_down == self.PUD_DOWN:
      bais = gpiod.line_request.FLAG_BIAS_PULL_DOWN
    elif pull_up_down == self.PUD_UP:
      bais = gpiod.line_request.FLAG_BIAS_PULL_UP
    else:
      bias = gpiod.line_request.FLAG_BIAS_DISABLE
    
    config = gpiod.line_request()
    config.consumer = "Blink"
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT if direction == self.OUT else gpiod.line_request.DIRECTION_INPUT
    config.flags = bais

    p.request(config)
    self.used_pins[pin] = p

  def output(self, pin, level):
    p = self.used_pins[pin]
    p.set_value(level)
    print("output set")

  def input(self, channel):
    p = self.used_pins[channel]
    return p.get_value()

  def cleanup(self):
    while len(self.used_pins ) > 1:
      pinItem = self.used_pins.popitem()
      pinItem.release()

  def PWM(self, pin, frequency):
    p = self.used_pins[pin]
    print("Pulse", dir(Pulse))
    return Pulse.PulseWidthManagement(p, frequency)
