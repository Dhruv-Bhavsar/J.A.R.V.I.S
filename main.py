from datetime import date
from sound import Sound
import sys


if len(sys.argv) == 1 or sys.argv[1] == "g":
	per = Sound.current_volume()
	muted = Sound.is_muted()
	print("Current volume is " + str(per) + " percent")
	print("Sound muted    | %s" % str(muted))
	print("----------------------")
	print("")

if len(sys.argv)>=3:
	if sys.argv[1] == "i":
		try:
			i = int(sys.argv[2])
			# print('main : ', i)
			Sound.volume_up(i)
		except ValueError:
			print("Please specify a number after saying increase volume by")

	elif sys.argv[1] == "m":
		try:
			Sound.mute()
		except:
			print("Wrong!!")

	elif sys.argv[1] == "d":
		try:
			d = int(sys.argv[2])
			Sound.volume_down(d)
		except:
			print("Please specify a number after saying decrease volume by")

	elif sys.argv[1] == "s":
		try:
			s = int(sys.argv[2])
			Sound.volume_set(s)
		except:
			print("Please specify a number after saying set volume to")

    
# while True:
#     print("Choose an option:")
#     print("1] Mute / Unmute volume")
#     print("2] Increase volume")
#     print("3] Decrease volume")
#     print("4] Set volume to 0")
#     print("5] Set volume to 100")
#     print("6] Set volume to ...")
#     print("7] Print sound settings")
#     print("8] Quit")
#     option = input("> ")
#     print("")

#     if (option == "1"):
#         Sound.mute()
#         continue

#     if (option == "2"):
#         Sound.volume_up()
#         continue

#     if (option == "3"):
#         Sound.volume_down()
#         continue

#     if (option == "4"):
#         Sound.volume_min()
#         continue

#     if (option == "5"):
#         Sound.volume_max()
#         continue

#     if (option == "6"):
#         volume = int(input("Volume (0 - 100): "))
#         Sound.volume_set(volume)
#         continue

#     if (option == "7"):
#         print("Current volume | %s" % str(Sound.current_volume()))
#         print("Sound muted    | %s" % str(Sound.is_muted()))
#         print("----------------------")
#         print("")
#         continue

#     if (option == "8"):
#         exit(0)