import vlc
import time
media_player = vlc.MediaPlayer()
media = vlc.Media("single-recording_01__1__2__3.mp3")
media_player.set_media(media)
media_player.play()
time.sleep(15)
