#
# Aidlab_SDK.py
# Aidlab-SDK
# Created by Szymon Gesicki on 09.05.2020.
#

from Aidlab.IAidlab import IAidlab
from ctypes import *
import sys
import os
import logging

logger = logging.getLogger(__name__)

class AidlabSDK_ptr(Structure):
    pass


class AidlabSDK:

    sample_time_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float)
    samples_time_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, POINTER(c_float), c_int)
    activity_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_uint8)
    respiration_rate_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_uint32)
    accelerometer_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float, c_float, c_float)
    gyroscope_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float, c_float, c_float)
    magnetometer_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float, c_float, c_float)
    battery_callback_type = CFUNCTYPE(None, c_void_p, c_uint8)
    steps_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_uint64)
    orientation_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float, c_float, c_float)
    body_position_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_uint8)
    quaternion_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_float, c_float, c_float, c_float)
    wear_state_callback_type = CFUNCTYPE(None, c_void_p, c_uint8)
    heart_rate_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_int)
    hrv_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_int)
    pressure_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, POINTER(c_int), c_int)
    pressure_wear_state_callback_type = CFUNCTYPE(None, c_void_p, c_uint8)
    sound_volume_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_uint16)
    exercise_callback_type = CFUNCTYPE(None, c_void_p, c_uint8)
    received_command_callback_type = CFUNCTYPE(None, c_void_p)
    sync_state_callback_type = CFUNCTYPE(None, c_void_p, c_uint8)
    unsynchronized_size_callback_type = CFUNCTYPE(None, c_void_p, c_uint16, c_float)
    received_message_type = CFUNCTYPE(None, c_void_p, POINTER(c_char), POINTER(c_char))
    user_event_callback_type = CFUNCTYPE(None, c_void_p, c_uint64)
    did_receive_error_callback_type = CFUNCTYPE(None, c_void_p, c_char_p)
    signal_quality_callback_type = CFUNCTYPE(None, c_void_p, c_uint64, c_int)


    Activity_type = {
        1: "automotive",
        2: "walking",
        4: "running",
        8: "cycling",
        16: "still",
        32: "still"
    }

    Wear_state_type = {
        0: "placed properly",
        1: "loose",
        2: "placed upside down",
        3: "detached"
    }

    Exercise = {
        0: "pushUp",
        1: "jump",
        2: "sitUp",
        3: "burpee",
        4: "pullUp",
        5: "squat",
        6: "plankStart",
        7: "plankEnd" 
    }

    Sync_state = {
        0: "start",
        1: "end",
        2: "stop",
        3: "empty"
    }

    Body_position = {
        0: "unknown",
        1: "front",
        2: "back",
        3: "left side",
        4: "right side"
    }

    ecgFiltrationMethod = {"normal": False, "aggressive": True}

    def __init__(self, delegate, aidlab_address):
        self.delegate = delegate
        self.aidlab = IAidlab(self)
        self.aidlab.address = aidlab_address

        # loading  aidlabsdk lib
        full_path = os.path.realpath(__file__)
        cwd, filename = os.path.split(full_path)

        if 'linux' in sys.platform:
            self.lib = cdll.LoadLibrary(cwd+"/aidlabsdk.so")
        elif 'win32' in sys.platform:
            self.lib = cdll.LoadLibrary(cwd+"/aidlabsdk.dll")
        elif 'darwin' in sys.platform:
            self.lib = cdll.LoadLibrary(cwd+"/aidlabsdk.dylib")
        else:
            raise RuntimeError("Unsupported operating system: {}".format(sys.platform))

        self.lib.initial.restype = POINTER(AidlabSDK_ptr)
        self.aidlab_sdk_ptr = self.lib.initial()
        # setting up type of variables and return values
        self.setup_process_types()

    def calculate_temperature(self, data):
        self.lib.processTemperaturePackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_respiration(self, data):
        self.lib.processRespirationPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_ecg(self, data):
        self.lib.processECGPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_battery(self, data):
        self.lib.processBatteryPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_motion(self, data):
        self.lib.processMotionPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_activity(self, data):
        self.lib.processActivityPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_orientation(self, data):
        self.lib.processOrientationPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_steps(self, data):
        self.lib.processStepsPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_heart_rate(self, data):
        self.lib.processHeartRatePackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_health_thermometer(self, data):
        self.lib.processHealthThermometerPackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def calculate_sound_volume(self, data):
        self.lib.processSoundVolumePackage((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)

    def did_receive_raw_cmd_value(self, data):
        logger.debug("receive cmd\n" + str(data))
        self.lib.processCMD((c_uint8 * len(data))(*data), len(data), self.aidlab_sdk_ptr)
    
    def get_command(self, message):
        data_array =(c_uint8 * (len(message)+1))(*message.encode('utf-8'))
        return self.lib.get_command(data_array, self.aidlab_sdk_ptr)
    
    def get_collect_command(self, realTime, sync):
        return self.lib.get_collect_command((c_uint8 * len(realTime))(*realTime), len(realTime), (c_uint8 * len(sync))(*sync), len(sync), self.aidlab_sdk_ptr)

    def did_receive_firmware_revision(self, firmware_revision):
        self.lib.setFirmwareRevision((c_uint8 * len(firmware_revision))(*firmware_revision.encode('utf-8')), len(firmware_revision), self.aidlab_sdk_ptr)
        self.aidlab.firmware_revision = firmware_revision

    def did_receive_hardware_revision(self, hardware_revision):
        self.lib.setHardwareRevision((c_uint8 * len(hardware_revision))(*hardware_revision.encode('utf-8')), len(hardware_revision), self.aidlab_sdk_ptr)
        self.aidlab.hardware_revision = hardware_revision

    def did_receive_manufacture_name(self, manufacture_name):
        self.aidlab.manufacture_name = manufacture_name

    def did_receive_serial_number(self, serial_number):
        self.aidlab.serial_number = serial_number

    def set_ecg_filtration_method(self, method):
        self.lib.setAggressiveECGFiltration(self.ecgFiltrationMethod.get(method,False), self.aidlab_sdk_ptr)

    def start_synchronization(self, address):
        self.delegate.start_synchronization(address)        

    def stop_synchronization(self, address):
        self.delegate.stop_synchronization(address)
    
    def send(self, address, command):
        self.delegate.send(address, command)

    def destroy(self):
        self.lib.destroy(self.aidlab_sdk_ptr)

    def did_connect_aidlab(self):
        self.delegate.did_connect(self.aidlab)

    def did_disconnect_aidlab(self):
        self.delegate.did_disconnect(self.aidlab)

    def setup_user_callback(self):

        self.ecg_c_callback = self.samples_time_callback_type(self.ecg_callback)
        self.respiration_c_callback = self.samples_time_callback_type(self.respiration_callback)
        self.temperature_c_callback = self.sample_time_callback_type(self.temperature_callback)
        self.activity_c_callback = self.activity_callback_type(self.activity_callback)
        self.steps_c_callback = self.steps_callback_type(self.steps_callback)
        self.accelerometer_c_callback = self.accelerometer_callback_type(self.accelerometer_callback)
        self.gyroscope_c_callback = self.gyroscope_callback_type(self.gyroscope_callback)
        self.magnetometer_c_callback = self.magnetometer_callback_type(self.magnetometer_callback)
        self.quaternion_c_callback = self.quaternion_callback_type(self.quaternion_callback)
        self.orientation_c_callback = self.orientation_callback_type(self.orientation_callback)
        self.body_position_c_callback = self.body_position_callback_type(self.body_position_callback)
        self.heart_rate_c_callback = self.heart_rate_callback_type(self.heart_rate_callback)
        self.hrv_c_callback = self.hrv_callback_type(self.hrv_callback)
        self.respiration_rate_c_callback = self.respiration_rate_callback_type(self.respiration_rate_callback)
        self.wear_state_c_callback = self.wear_state_callback_type(self.wear_state_did_change)
        self.sound_volume_c_callback = self.sound_volume_callback_type(self.sound_volume_callback)
        self.exercise_c_callback = self.exercise_callback_type(self.exercise_callback)
        self.receive_command_c_callback = self.received_command_callback_type(self.receive_command_callback)
        self.pressure_c_callback = self.pressure_callback_type(self.pressure_callback)
        self.pressure_wear_state_c_callback = self.pressure_wear_state_callback_type(self.pressure_wear_state_did_change)
        self.received_message_c_callback = self.received_message_type(self.received_message_callback)
        self.user_event_c_callback = self.user_event_callback_type(self.user_event_callback)
        self.did_receive_error_c_callback = self.did_receive_error_callback_type(self.did_receive_error_callback)
        self.battery_c_callback = self.battery_callback_type(self.battery_callback)
        self.signal_quality_c_callback = self.signal_quality_callback_type(self.signal_quality_callback)

        self.lib.initUserServiceCallback(
            self.ecg_c_callback, self.respiration_c_callback, self.temperature_c_callback,
            self.accelerometer_c_callback, self.gyroscope_c_callback, self.magnetometer_c_callback,
            self.battery_c_callback, self.activity_c_callback, self.steps_c_callback, 
            self.orientation_c_callback, self.quaternion_c_callback, self.respiration_rate_c_callback,
            self.wear_state_c_callback, self.heart_rate_c_callback, self.hrv_c_callback,
            self.sound_volume_c_callback, self.exercise_c_callback, self.receive_command_c_callback, 
            self.received_message_c_callback, self.user_event_c_callback, self.pressure_c_callback,
            self.pressure_wear_state_c_callback, self.body_position_c_callback,
            self.did_receive_error_c_callback, self.signal_quality_c_callback, self.aidlab_sdk_ptr)

    def setup_synchronization_callback(self):

        self.sync_state_c_callback = self.sync_state_callback_type(self.sync_state_did_change)
        self.unsynchronized_size_c_callback = self.unsynchronized_size_callback_type(self.did_receive_unsynchronized_size)
        self.past_ecg_c_callback = self.samples_time_callback_type(self.past_ecg_callback)
        self.past_respiration_c_callback = self.samples_time_callback_type(self.past_respiration_callback)
        self.past_temperature_c_callback = self.sample_time_callback_type(self.past_temperature_callback)
        self.past_activity_c_callback = self.activity_callback_type(self.past_activity_callback)
        self.past_steps_c_callback = self.steps_callback_type(self.past_steps_callback)
        self.past_accelerometer_c_callback = self.accelerometer_callback_type(self.past_accelerometer_callback)
        self.past_gyroscope_c_callback = self.gyroscope_callback_type(self.past_gyroscope_callback)
        self.past_magnetometer_c_callback = self.magnetometer_callback_type(self.past_magnetometer_callback)
        self.past_quaternion_c_callback = self.quaternion_callback_type(self.past_quaternion_callback)
        self.past_orientation_c_callback = self.orientation_callback_type(self.past_orientation_callback)
        self.past_body_position_c_callback = self.body_position_callback_type(self.past_body_position_callback)
        self.past_heart_rate_c_callback = self.heart_rate_callback_type(self.past_heart_rate_callback)
        self.past_hrv_c_callback = self.hrv_callback_type(self.past_hrv_callback)
        self.past_respiration_rate_c_callback = self.respiration_rate_callback_type(self.past_respiration_rate_callback)
        self.past_sound_volume_c_callback = self.sound_volume_callback_type(self.past_sound_volume_callback)
        self.past_pressure_c_callback = self.pressure_callback_type(self.past_pressure_callback)
        self.past_user_event_c_callback = self.user_event_callback_type(self.past_user_event_callback)
        self.past_signal_quality_c_callback = self.signal_quality_callback_type(self.past_signal_quality_callback)

        self.lib.initSynchronizationCallback(
            self.sync_state_c_callback, self.unsynchronized_size_c_callback, self.past_ecg_c_callback,
            self.past_respiration_c_callback, self.past_temperature_c_callback, self.past_heart_rate_c_callback,
            self.past_hrv_c_callback, self.past_activity_c_callback, self.past_respiration_rate_c_callback,
            self.past_steps_c_callback, self.past_user_event_c_callback, self.past_sound_volume_c_callback,
            self.past_pressure_c_callback, self.past_accelerometer_c_callback, self.past_gyroscope_c_callback,
            self.past_quaternion_c_callback, self.past_orientation_c_callback, self.past_magnetometer_c_callback,
            self.past_body_position_c_callback, self.past_hrv_c_callback, self.past_accelerometer_c_callback,
            self.aidlab_sdk_ptr)

    def setup_process_types(self):

        self.lib.processECGPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processECGPackage.restype = None

        self.lib.processTemperaturePackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processTemperaturePackage.restype = None

        self.lib.processMotionPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processMotionPackage.restype = None

        self.lib.processRespirationPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processRespirationPackage.restype = None

        self.lib.processBatteryPackage.argtypes = [ POINTER(c_uint8), c_int, c_void_p]
        self.lib.processBatteryPackage.restype = None

        self.lib.processActivityPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processActivityPackage.restype = None

        self.lib.processStepsPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processStepsPackage.restype = None

        self.lib.processOrientationPackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processOrientationPackage.restype = None

        self.lib.processHeartRatePackage.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processHeartRatePackage.restype = None

        self.lib.processCMD.argtypes = [POINTER(c_uint8), c_int, c_void_p]
        self.lib.processCMD.restype = None

        self.lib.setHardwareRevision.argtypes = [POINTER(c_uint8), c_void_p]
        self.lib.setHardwareRevision.restype = None

        self.lib.setFirmwareRevision.argtypes = [POINTER(c_uint8), c_void_p]
        self.lib.setFirmwareRevision.restype = None

        self.lib.setAggressiveECGFiltration.argtypes = [c_bool, c_void_p]
        self.lib.setAggressiveECGFiltration.restype = None

        self.lib.destroy.argtypes = [c_void_p]
        self.lib.destroy.restype = None

        self.lib.get_command.argtypes = [POINTER(c_uint8), c_void_p]
        self.lib.get_command.restype = POINTER(c_uint8)

        self.lib.get_collect_command.argtypes = [POINTER(c_uint8), c_int, POINTER(c_uint8), c_int, c_void_p]
        self.lib.get_collect_command.restype = POINTER(c_uint8)

    def user_event_callback(self, context, timestamp):
        self.delegate.did_detect_user_event(self.aidlab, timestamp)

    def did_receive_error_callback(self, context, log_text):
        try:
            logger.warn(" [DLL] " + log_text.decode("utf-8"))
        except UnicodeDecodeError:
            logger.warn(" [DLL] " + str(log_text))

    def exercise_callback(self, context, exercise):
        exercise = self.Exercise.get(exercise, "None")
        self.delegate.did_detect_exercise(self.aidlab, exercise)
        
    def ecg_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_ecg(self.aidlab, timestamp, values)

    def respiration_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_respiration(self.aidlab, timestamp, values)

    def battery_callback(self, context, state_of_charge):
        self.delegate.did_receive_battery_level(self.aidlab, state_of_charge)

    def temperature_callback(self, context, timestamp, value):
        self.delegate.did_receive_skin_temperature(self.aidlab, timestamp, value)

    def accelerometer_callback(self, context, timestamp, ax, ay, az):
        self.delegate.did_receive_accelerometer(self.aidlab, timestamp, ax, ay, az)

    def gyroscope_callback(self, context, timestamp, gx, gy, gz):
        self.delegate.did_receive_gyroscope(self.aidlab, timestamp, gx, gy, gz)

    def magnetometer_callback(self, context, timestamp, mx, my, mz):
        self.delegate.did_receive_magnetometer(self.aidlab, timestamp, mx, my, mz)

    def orientation_callback(self, context, timestamp, roll, pitch, yaw):
        self.delegate.did_receive_orientation(self.aidlab, timestamp, roll, pitch, yaw)
    
    def quaternion_callback(self, context, timestamp, qw, qx, qy, qz):
        self.delegate.did_receive_quaternion(self.aidlab, timestamp, qw, qx, qy, qz)

    def body_position_callback(self, context, timestamp, body_position):
        body_position = self.Body_position.get(body_position, "unknown")
        self.delegate.did_receive_body_position(self.aidlab, timestamp, body_position)

    def activity_callback(self, context, timestamp, activity):
        activity = self.Activity_type.get(activity, "still")
        self.delegate.did_receive_activity(self.aidlab, timestamp, activity)

    def steps_callback(self, context, timestamp, value):
        self.delegate.did_receive_steps(self.aidlab, timestamp, value)

    def heart_rate_callback(self, context, timestamp, heart_rate):
        self.delegate.did_receive_heart_rate(self.aidlab, timestamp, heart_rate)

    def hrv_callback(self, context, timestamp, hrv):
        self.delegate.did_receive_hrv(self.aidlab, timestamp, hrv)

    def respiration_rate_callback(self, context, timestamp, value):
        self.delegate.did_receive_respiration_rate(self.aidlab, timestamp, value)

    def pressure_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_pressure(self.aidlab, timestamp, values)

    def pressure_wear_state_did_change(self, context, wear_state):
        wear_state = self.Wear_state_type.get(wear_state, "detached")
        self.delegate.pressure_wear_state_did_change(self.aidlab, wear_state)

    def wear_state_did_change(self, context, wear_state):
        wear_state = self.Wear_state_type.get(wear_state, "detached")
        self.delegate.wear_state_did_change(self.aidlab, wear_state)

    def sound_volume_callback(self, context, timestamp, sound_volume):
        self.delegate.did_receive_sound_volume(self.aidlab, timestamp, sound_volume)

    def receive_command_callback(self, context):
        self.delegate.did_receive_command(self.aidlab)
    
    def received_message_callback(self, context, process, message):
        pass

    def signal_quality_callback(self, context, timestamp, value):
        self.delegate.did_receive_signal_quality(self.aidlab, timestamp, value)

    # Synchronization

    def past_user_event_callback(self, context, timestamp):
        self.delegate.did_receive_past_user_event(self.aidlab, timestamp)

    def past_ecg_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_past_ecg(self.aidlab, timestamp, values)

    def past_respiration_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_past_respiration(self.aidlab, timestamp, values)

    def past_temperature_callback(self, context, timestamp, value):
        self.delegate.did_receive_past_skin_temperature(self.aidlab, timestamp, value)

    def past_accelerometer_callback(self, context, timestamp, ax, ay, az):
        self.delegate.did_receive_past_accelerometer(self.aidlab, timestamp, ax, ay, az)

    def past_gyroscope_callback(self, context, timestamp, gx, gy, gz):
        self.delegate.did_receive_past_gyroscope(self.aidlab, timestamp, gx, gy, gz)

    def past_magnetometer_callback(self, context, timestamp, mx, my, mz):
        self.delegate.did_receive_past_magnetometer(self.aidlab, timestamp, mx, my, mz)

    def past_orientation_callback(self, context, timestamp, roll, pitch, yaw):
        self.delegate.did_receive_past_orientation(self.aidlab, timestamp, roll, pitch, yaw)

    def past_quaternion_callback(self, context, timestamp, qw, qx, qy, qz):
        self.delegate.did_receive_past_quaternion(self.aidlab, timestamp, qw, qx, qy, qz)

    def past_activity_callback(self, context, timestamp, activity):
        activity = self.Activity_type.get(activity, "still")
        self.delegate.did_receive_past_activity(self.aidlab, timestamp, activity)

    def past_body_position_callback(self, context, timestamp, body_position):
        body_position = self.Body_position.get(body_position, "unknown")
        self.delegate.did_receive_past_body_position(self.aidlab, timestamp, body_position)

    def past_pressure_callback(self, context, timestamp, values, size):
        values = [values[i] for i in range(size)]
        self.delegate.did_receive_past_pressure(self.aidlab, timestamp, values)

    def past_steps_callback(self, context, timestamp, value):
        self.delegate.did_receive_past_steps(self.aidlab, timestamp, value)

    def past_heart_rate_callback(self, context, timestamp, heart_rate):
        self.delegate.did_receive_past_heart_rate(self.aidlab, timestamp, heart_rate)

    def past_hrv_callback(self, context, timestamp, hrv):
        self.delegate.did_receive_past_hrv(self.aidlab, timestamp, hrv)

    def past_respiration_rate_callback(self, context, timestamp, value):
        self.delegate.did_receive_past_respiration_rate(self.aidlab, timestamp, value)

    def past_sound_volume_callback(self, context, timestamp, sound_volume):
        self.delegate.did_receive_past_sound_volume(self.aidlab, timestamp, sound_volume)

    def past_signal_quality_callback(self, context, timestamp, value):
        self.delegate.did_receive_past_signal_quality(self.aidlab, timestamp, value)

    def sync_state_did_change(self, context, sync_state):
        sync_state = self.Sync_state.get(sync_state, "empty")
        self.delegate.sync_state_did_change(self.aidlab, sync_state)

    def did_receive_unsynchronized_size(self, context, unsynchronized_size, sync_bytes_per_second):
        self.delegate.did_receive_unsynchronized_size(self.aidlab, unsynchronized_size, sync_bytes_per_second)