import logging
log = logging.getLogger(__name__)

try:
  import threading
  import numpy as np
  import numpy.typing as npt
  import pathlib
  import argparse
  from ctypes import byref, c_int16, addressof, create_string_buffer, Structure, CDLL, POINTER, c_char_p, c_uint8,\
                     c_uint16, c_uint32, c_bool, c_double, c_int8, c_float, c_void_p, c_uint64, c_int64, Union,\
                     LittleEndianStructure
except ModuleNotFoundError as err:
  # Error handling
  log.error(err)

class ModuleInit(Structure):
  _fields_ = [("deviceNr", c_uint8),
              ("serialNrStr", c_char_p)]

class ModuleStatusFlags(LittleEndianStructure):
  _fields_ = [("fifoFull", c_uint8, 1),
              ("fifoEmpty", c_uint8, 1),
              ("waitTrig", c_uint8, 1),
              ("measure", c_uint8, 1),
              ("armed", c_uint8, 1),
              ("colT", c_uint8, 1)]

class ModuleStatus(Union):
    _fields_ = [("b", ModuleStatusFlags),
                ("asByte", c_uint8)]

class HardwareError(IOError):
  pass

class SpcQcDllWrapper:
  versionStr = ""
  versionStrBuf = create_string_buffer(128)

  def __init__(self, filename):
    self.__dll = CDLL(filename)

    self.__get_dll_version = self.__dll.get_dll_version
    self.__get_dll_version.restype = c_int16

    self.__init = self.__dll.init
    self.__init.restype = c_int16
    self.__init.argtypes = [POINTER(ModuleInit), c_uint8, c_char_p]

    self.__deinit = self.__dll.deinit
    self.__deinit.restype = c_int16

    self.__set_measurement_configuration = self.__dll.set_measurement_configuration
    self.__set_measurement_configuration.restype = c_int16
    self.__set_measurement_configuration.argtypes = [c_uint8, POINTER(c_uint32),POINTER(c_uint32),POINTER(c_uint8)]

    self.__set_card_focus = self.__dll.set_card_focus
    self.__set_card_focus.restype = c_int16
    self.__set_card_focus.argtypes = [c_uint8]

    self.__write_setting = self.__dll.write_setting
    self.__write_setting.restype = c_uint32
    self.__write_setting.argtypes = [c_uint16, c_uint32]

    self.__read_setting = self.__dll.read_setting
    self.__read_setting.restype = c_uint32
    self.__read_setting.argtypes = [c_uint16]

    self.__get_firmware_version = self.__dll.get_firmware_version
    self.__get_firmware_version.restype = c_uint16

    self.__reset_registers = self.__dll.reset_registers
    self.__reset_registers.restype = c_uint16

    self.__get_rates = self.__dll.get_rates
    self.__get_rates.argtypes = [c_uint8]
    self.__get_rates.restype = c_uint32

    self.__get_marker_status = self.__dll.get_marker_status
    self.__get_marker_status.argtype = c_uint8
    self.__get_marker_status.restype = c_int8

    self.__set_external_trigger_enable = self.__dll.set_external_trigger_enable
    self.__set_external_trigger_enable.argtype = c_bool
    self.__set_external_trigger_enable.restype = c_int8

    self.__set_trigger_polarity = self.__dll.set_trigger_polarity
    self.__set_trigger_polarity.argtype = c_uint8
    self.__set_trigger_polarity.restype = c_int8

    self.__set_routing_compensation = self.__dll.set_routing_compensation
    self.__set_routing_compensation.argtype = c_int8
    self.__set_routing_compensation.restype = c_int8

    self.__set_routing_enable = self.__dll.set_routing_enable
    self.__set_routing_enable.argtypes = [c_uint8, c_bool]
    self.__set_routing_enable.restype = c_int8

    self.__set_hardware_countdown_enable = self.__dll.set_hardware_countdown_enable
    self.__set_hardware_countdown_enable.argtype = c_bool
    self.__set_hardware_countdown_enable.restype = c_int8

    self.__set_marker_edge = self.__dll.set_marker_polarity
    self.__set_marker_edge.argtypes = [c_uint8, c_uint8]
    self.__set_marker_edge.restype = c_int8

    self.__get_module_status = self.__dll.get_module_status
    self.__get_module_status.restype = c_uint8

    self.__stop_measurement = self.__dll.stop_measurement
    self.__stop_measurement.restype = c_int8

    self.__set_hardware_countdown_time = self.__dll.set_hardware_countdown_time
    self.__set_hardware_countdown_time.argtype = c_double
    self.__set_hardware_countdown_time.restype = c_double

    self.__set_marker_enable = self.__dll.set_marker_enable
    self.__set_marker_enable.argtypes = [c_uint8, c_bool]
    self.__set_marker_enable.restype = c_int8

    self.__set_channel_divider = self.__dll.set_channel_divider
    self.__set_channel_divider.argtypes = [c_uint8, c_uint8]
    self.__set_channel_divider.restype = c_int8

    self.__set_dithering_enable = self.__dll.set_dithering_enable
    self.__set_dithering_enable.argtype = c_bool
    self.__set_dithering_enable.restype = c_int8

    self.__set_channel_delay = self.__dll.set_channel_delay
    self.__set_channel_delay.argtypes = [c_uint8, c_float]
    self.__set_channel_delay.restype = c_float

    self.__set_CFD_threshold = self.__dll.set_CFD_threshold
    self.__set_CFD_threshold.argtypes = [c_uint8, c_float]
    self.__set_CFD_threshold.restype = c_float

    self.__set_CFD_zc = self.__dll.set_CFD_zc
    self.__set_CFD_zc.argtypes = [c_uint8, c_float]
    self.__set_CFD_zc.restype = c_float

    self.__initialize_data_collection = self.__dll.initialize_data_collection
    self.__initialize_data_collection.argtype = c_uint64
    self.__initialize_data_collection.restype = c_int16

    self.__run_data_collection = self.__dll.run_data_collection
    self.__run_data_collection.argtypes = [c_uint32, c_uint32]
    self.__run_data_collection.restype = c_int16

    self.__get_raw_events_from_buffer = self.__dll.get_raw_events_from_buffer
    self.__get_raw_events_from_buffer.argtypes = [c_void_p, c_uint32, c_uint8]
    self.__get_raw_events_from_buffer.restype = c_int64

    self.__deinit_data_collection = self.__dll.deinit_data_collection

    self.__get_dll_version(byref(self.versionStrBuf))
    self.versionStr = str(self.versionStrBuf.value)[2:-1]

  def init(self, moduleList: list[int], logPath: str, emulateHardware: bool=False) -> int:
    arg1 = (ModuleInit * len(moduleList))()
    self.serialNumber = []
    serialNumber = []

    self.logPath = logPath

    for i in range(len(moduleList)):
      serialNumber.append(create_string_buffer(16))
      arg1[i].serialNrStr = addressof(serialNumber[-1])
      arg1[i].deviceNr = c_uint8(moduleList[i])

    numberOfHwModules = len(moduleList) if emulateHardware == False else 0

    ret = self.__init(arg1, c_uint8(numberOfHwModules), logPath.encode('utf-8'))

    for serStr in serialNumber:
      self.serialNumber.append(str(serStr.value)[2:-1])
    return ret

  def set_measurement_configuration(self, operationMode, timeRange, frontClipping, resolution):
    arg1 = c_uint8(operationMode)
    arg2 = c_uint32(timeRange)
    arg3 = c_uint32(frontClipping)
    arg4 = c_uint8(resolution)
    ret = self.__set_measurement_configuration(arg1, byref(arg2), byref(arg3), byref(arg4))
    return ret, arg2.value, arg3.value, arg4.value

  def set_lower_limit(self, frontClipping):
    arg = c_uint16(frontClipping)
    return self.__set_lower_limit(arg)

  def set_cfd_zero_cross(self, channel, zeroCross) -> float:
    arg1 = c_uint8(channel)
    arg2 = c_float(zeroCross)
    return self.__set_CFD_zc(arg1, arg2)

  def set_cfd_threshold(self, channel, threshold) -> float:
    arg1 = c_uint8(channel)
    arg2 = c_float(threshold)
    return self.__set_CFD_threshold(arg1, arg2)

  def set_card_focus(self, focusOnCardNr):
    arg = c_uint8(focusOnCardNr)
    return self.__set_card_focus(arg)

  def set_routing_compensation(self, delay):
    arg = c_int8(delay)
    return self.__set_routing_compensation(arg)

  def set_routing_enable(self, channel, state):
    arg1 = c_uint8(channel)
    arg2 = c_bool(state)
    return self.__set_routing_enable(arg1, arg2)

  def set_channel_divider(self, channel, divider: int) -> int:
    arg1 = c_uint8(int(channel))
    arg2 = c_uint8(divider)
    return self.__set_channel_divider(arg1, arg2)

  def set_marker_enable(self, marker, state):
    arg1 = c_uint8(marker)
    arg2 = c_bool(state)
    return self.__set_marker_enable(arg1, arg2)

  def set_marker_edge(self, marker, edge):
    arg1 = c_uint8(marker)
    arg2 = c_uint8(edge)
    return self.__set_marker_edge(arg1, arg2)

  def set_dithering_enable(self, state):
    arg1 = c_bool(state)
    return self.__set_dithering_enable(arg1)

  def set_external_trigger_enable(self, state):
    arg1 = c_bool(state)
    return self.__set_external_trigger_enable(arg1)

  def set_trigger_polarity(self, edge):
    arg1 = c_uint8(edge)
    return self.__set_trigger_polarity(arg1)

  def reset_registers(self):
    return self.__reset_registers()

  def read_setting(self, settingId):
    arg1 = c_uint16(settingId)
    return self.__read_setting(arg1)

  def write_setting(self, settingId, value):
    arg1 = c_uint16(settingId)
    arg2 = c_uint32(value)
    return self.__write_setting(arg1, arg2)

  def deinit(self):
    return self.__deinit()

  def get_rates(self, channel):
    arg = c_uint8(channel)
    return self.__get_rates(arg)

  def get_marker_status(self, marker):
    arg = c_uint8(marker)
    return self.__get_marker_status(arg)

  def set_hardware_countdown_enable(self, enable):
    arg = c_bool(enable)
    return self.__set_hardware_countdown_enable(arg)

  def get_module_status(self) -> dict:
    ms = ModuleStatus()
    ms.asBytes = self.__get_module_status()
    return dict((field, getattr(ms.b, field)) for field, _ in ms.b._fields_)

  def stop_measurement(self):
    return self.__stop_measurement()

  def set_hardware_countdown_time(self, nsTime):
    arg = c_double(nsTime)
    ret = self.__set_hardware_countdown_time(arg)
    if ret < 0:
      raise HardwareError(f"DLL call set_hardware_countdown_time() returned with {int(ret)}, more details: {self.logPath}")
    return ret

  def set_channel_delay(self, channel, nsDelay) -> float:
    arg1 = c_uint8(channel)
    arg2 = c_float(nsDelay)
    return self.__set_channel_delay(arg1, arg2)

  def initialize_data_collection(self, fifoSize):
    arg = c_uint64(fifoSize)
    return self.__initialize_data_collection(arg)

  def run_data_collection(self, acquisitionTimeMs, timeoutMs):
    arg1 = c_uint32(acquisitionTimeMs)
    arg2 = c_uint32(timeoutMs)
    return self.__run_data_collection(arg1, arg2)

  def get_raw_events_from_buffer(self, buffer: npt.NDArray[np.uint32], maxEvents, cardNumber):
    arg2 = c_uint32(maxEvents)
    arg3 = c_uint8(cardNumber)
    events = self.__get_raw_events_from_buffer(buffer.ctypes.data, arg2, arg3)
    return buffer, events

  def get_events_from_buffer_to_file(self, cardNumber, filePath, threadEvent: threading.Event):
    pathlib.Path(filePath).parent.mkdir(parents=True, exist_ok=True)
    with open(filePath, 'wb') as file:
      buffer_size = 8388607
      buffer = np.array([0]*int(buffer_size), dtype=np.uint32) # 1GiB
      arg2 = c_uint32(buffer_size)#0x7F_FFFF)#4000_0000)
      arg3 = c_uint8(cardNumber)

      while not threadEvent.isSet():
        events = self.__get_raw_events_from_buffer(buffer.ctypes.data, buffer_size, arg3)
        if events > 0:
          file.write(buffer[:int(events)])

      events = self.__get_raw_events_from_buffer(buffer.ctypes.data, c_uint32(0), arg3)
      while events > 0:
        events = self.__get_raw_events_from_buffer(buffer.ctypes.data, arg2, arg3)
        if events > 0:
          file.write(buffer[:int(events)])

  def deinit_data_collection(self):
    self.__deinit_data_collection()

  def get_firmware_version(self):
    return self.__get_firmware_version()

def main():
  home_drive = pathlib.Path.home().drive
  parser = argparse.ArgumentParser(prog="bhPy", description="SPC-QC-104 dll wrapper that provides python bindings to use Becker&Hickls' SPC-QC-104 hardware through the dll")
  parser.add_argument('dll_path', nargs='?', default=f'{home_drive}/Program Files (x86)/BH/SPCM/spc_qc_104.dll')

  args = parser.parse_args()

  dll_path = pathlib.Path(args.dll_path)

  print(dll_path)

  if not dll_path.exists:
    dll_path = pathlib.Path(f"{home_drive}/Program Files/BH/SPCM/spc_qc_104.dll")
    if not dll_path.exists:
      print(".../spc_qc_104.dll was neither found at default location nor at the specified path")
      exit()

  spcQcDll = SpcQcDllWrapper(str(dll_path))
  print(spcQcDll.versionStr)

if __name__ == '__main__':
  main()