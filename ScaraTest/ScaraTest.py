################################################################################
# https://docs.python.org/ja/3/library/ctypes.html
#
import ctypes
import time

VID = 0x10C4	# ロボットのVender ID
PID	= 0xEA80	# ロボットのProduct ID

########################################
#
dll = ctypes.cdll.LoadLibrary("./ScaraLib.dll")
########################################
#
pyGetEnumDevices = dll.GetEnumDevices
pyGetEnumDevices.argtype = None
pyGetEnumDevices.restype = ctypes.c_bool
########################################
#
pyDeviceOpen = dll.DeviceOpen
pyDeviceOpen.argtypes = [ctypes.c_int]
pyDeviceOpen.restype = ctypes.c_void_p
########################################
#
pyDeviceClose =	dll.DeviceClose
pyDeviceClose.argtypes = [ctypes.c_void_p]
pyDeviceClose.restype = ctypes.c_bool

########################################
#
pyScaraInitialize =	dll.ScaraInitialize
pyScaraInitialize.argtypes = [ctypes.c_void_p]
pyScaraInitialize.restype = ctypes.c_bool
########################################
#
pyMotorTorque = dll.MotorTorque
pyMotorTorque.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
pyMotorTorque.restype = ctypes.c_bool
########################################
#
pyMoveXYZ =	dll.MoveXYZ
pyMoveXYZ.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
pyMoveXYZ.restype = ctypes.c_bool
########################################
#
pyMoveXYZYaw = dll.MoveXYZYaw
pyMoveXYZYaw.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
pyMoveXYZYaw.restype = ctypes.c_bool
########################################
#
pyMoveXYZYawOC = dll.MoveXYZYawOC
pyMoveXYZYawOC.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
pyMoveXYZYawOC.restype = ctypes.c_bool
########################################
#
pyMoveYawOC = dll.MoveYawOC
pyMoveYawOC.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_int]
pyMoveYawOC.restype = ctypes.c_bool
########################################
#
pyMoveYaw =	dll.MoveYaw
pyMoveYaw.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_int]
pyMoveYaw.restype = ctypes.c_bool
########################################
#
pyMoveOC = dll.MoveOC
pyMoveOC.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_int]
pyMoveOC.restype = ctypes.c_bool

########################################
#
def main():
#	numDevice = dll.GetEnumDevices();
	numDevice = pyGetEnumDevices(None);
	print(numDevice, ' device(s) found.')

	if (numDevice > 0):
		hDevice = pyDeviceOpen(0);
		print('device', hex(hDevice))

		pyScaraInitialize(hDevice)

		servoNum = 0

		if 0:

			while 1:
				n = input('How many motors?(3 or 5):')
				servoNum = int(n)
				if (servoNum < 3 or servoNum > 5):
					print('Does not correspond to ', servoNum, ' motors.\n')
				else:
					break;

			# 移動先の座標を入力
			n = input('Input move positon x: ')
			x = float(n)
			n = input('Input move positon y: ')
			y = float(n)
			n = input('Input move positon z: ')
			z = float(n)

			if (servoNum == 3):
				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZ(hDevice, x, y, z, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

			elif (servoNum == 4):
				n = input('Input move positon yaw: ')
				yaw = float(n)

				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZYaw(hDevice, x, y, z, yaw, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

			elif (servoNum == 5):
				n = input('Input move positon yaw: ')
				yaw = float(n)
				n = input('Input move positon width: ')
				oc = float(n)
				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZYawOC(hDevice, x, y, z, yaw, oc, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

		elif 0:
			n = input('Input move positon yaw: ')
			yaw = float(n)

			pyMotorTorque(hDevice, True, 4, 4)
			pyMoveYaw(hDevice, yaw, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 4, 4)

		elif 1:
			n = input('Input move positon width: ')
			oc = float(n)

			pyMotorTorque(hDevice, True, 5, 5)
			pyMoveOC(hDevice, oc, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 5, 5)

		else:

			n = input('Input move positon yaw: ')
			yaw = float(n)
			n = input('Input move positon width: ')
			oc = float(n)
			pyMotorTorque(hDevice, True, 4, 5)
			pyMoveYawOC(hDevice, yaw, oc, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 4, 5)

		pyDeviceClose(hDevice)

	else:
		print('device not found.')

if __name__ == "__main__":
	main()
