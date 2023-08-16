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
pySetDebugMode = dll.SetDebugMode
pySetDebugMode.argtype = ctypes.c_bool
pySetDebugMode.restype = None
########################################

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
pyMoveXY = dll.MoveXY
pyMoveXY.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_int]
pyMoveXY.restype = ctypes.c_bool
########################################
#
pyMoveZ = dll.MoveZ
pyMoveZ.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_int]
pyMoveZ.restype = ctypes.c_bool
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
pyGetPos = dll.GetPos
pyGetPos.argtypes = [ctypes.c_void_p, ctypes.c_int]
pyGetPos.restype = ctypes.c_double

########################################
#
def main():
#	numDevice = dll.GetEnumDevices();
	numDevice = pyGetEnumDevices(None);
	print(numDevice, ' device(s) found.')

	if (numDevice > 0):
		hDevice = pyDeviceOpen(0);
		print('device', hex(hDevice))

		pySetDebugMode(True)
		pyScaraInitialize(hDevice)

		while 1:
			print('Select Action')
			print('    1:X Y')
			print('    2:Z')
			print('    3:Yaw')
			print('    4:OC')
			print('    5:X Y Z')
			print('    6:X Y Z Yaw OC')
			print('    7:Yaw OC')
			print('    8:Get Angle')
			print('    0:Quit')
			print('')
			a = input('Input Action : ')
			if (a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8'):
				break;

		if a == '0':
			pass

		elif a == '1':
			print('1:X Y')

			# 移動先の座標を入力
			n = input('Input move positon x (-1,400 ～ +1,400): ')
			x = float(n)
			n = input('Input move positon y (-1,400 ～ +1,400): ')
			y = float(n)

			pyMotorTorque(hDevice, True, 1, 2)
			pyMoveXY(hDevice, x, y, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 1, 2)

		elif a == '2':
			print('2:Z')
			n = input('Input move positon z (-1,500 ～ +1,500): ')
			z = float(n)

			pyMotorTorque(hDevice, True, 3, 3)
			pyMoveZ(hDevice, z, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 3, 3)

		elif a == '3':
			print('3:Yaw')

			n = input('Input move positon yaw (-1,500 ～ +1,500): ')
			yaw = float(n)

			pyMotorTorque(hDevice, True, 4, 4)
			pyMoveYaw(hDevice, yaw, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 4, 4)

		elif a == '4':
			print(' 4:OC')

			n = input('Input move positon width (0 ～ +700): ')
			oc = float(n)

			pyMotorTorque(hDevice, True, 5, 5)
			pyMoveOC(hDevice, oc, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 5, 5)

		elif a == '5':
			print('5:X Y Z')
			pass

		elif a == '6':
			print('6:X Y Z Yaw OC')

			while 1:
				servoNum = 0
				n = input('How many motors?(3 or 5):')
				servoNum = int(n)
				if (servoNum < 3 or servoNum > 5):
					print('Does not correspond to ', servoNum, ' motors.\n')
				else:
					break;

			# 移動先の座標を入力
			n = input('Input move positon x (-1,400 ～ +1,400): ')
			x = float(n)
			n = input('Input move positon y (-1,400 ～ +1,400): ')
			y = float(n)
			n = input('Input move positon z (-1,500 ～ +1,500): ')
			z = float(n)

			if (servoNum == 3):
				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZ(hDevice, x, y, z, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

			elif (servoNum == 4):
				n = input('Input move positon yaw (-1,500 ～ +1,500): ')
				yaw = float(n)

				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZYaw(hDevice, x, y, z, yaw, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

			elif (servoNum == 5):
				n = input('Input move positon yaw (-1,500 ～ +1,500: ')
				yaw = float(n)
				n = input('Input move positon width (0 ～ +700): ')
				oc = float(n)
				pyMotorTorque(hDevice, True, 1, servoNum)
				pyMoveXYZYawOC(hDevice, x, y, z, yaw, oc, 1000)
				time.sleep(1);
				pyMotorTorque(hDevice, False, 1, servoNum)

		elif a == '7':
			print('7:Yaw OC')

			n = input('Input move positon yaw (-1,500 ～ +1,500): ')
			yaw = float(n)
			n = input('Input move positon width (0 ～ +700): ')
			oc = float(n)
			pyMotorTorque(hDevice, True, 4, 5)
			pyMoveYawOC(hDevice, yaw, oc, 1000)
			time.sleep(1);
			pyMotorTorque(hDevice, False, 4, 5)

		elif a == '8':
			print('8:Get Angle')
			pyGetPos(hDevice, 0)

		pyDeviceClose(hDevice)

	else:
		print('device not found.')

if __name__ == "__main__":
	main()
