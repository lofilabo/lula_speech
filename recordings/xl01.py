import vlc
import time
media_player = vlc.MediaPlayer()
media01 = vlc.Media("zz--001--thinglepingle.mp3")
media02 = vlc.Media("zz--002--mmmnnn.mp3")
media03 = vlc.Media("single-recording__3___03.mp3")

#try one
media_player.set_media(media01)
media_player.play()
time.sleep(3)

"""
media_player.set_media(media02)
media_player.play()
time.sleep(1)

media_player.set_media(media03)
media_player.play()
time.sleep(1)
"""
