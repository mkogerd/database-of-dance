from __future__ import unicode_literals
import youtube_dl
import os

# ffmpeg download required for moviepy to import properly
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip

def get_video(url):

	# Download youtube video via URL
	ydl_opts = {'outtmpl': 'vid/%(title)s'}
	#ydl_opts = {'outtmpl': 'hello.mp4'}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
		result = ydl.extract_info("{}".format(url))
		name = ydl.prepare_filename(result)

	# Resize and output as MP4 at 30fps
	fps = 30
	compress_factor = 0.5
	clip = (VideoFileClip(name)
		.resize(compress_factor))
	clip.write_videofile(name+'.mp4', fps=fps)
	os.remove(name)
