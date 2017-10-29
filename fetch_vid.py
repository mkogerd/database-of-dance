from __future__ import unicode_literals
import youtube_dl
import os
import pandas as pd

# ffmpeg download required for moviepy to import properly
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip

# Downloads a specified youtube video and saves to specified directory, returns the name of the video
def get_video(url, directory = 'vid/'):
	# Make output directory if it doesn't exist
	if not os.path.exists(directory):
		os.makedirs(directory)

	# Download youtube video via URL
	ydl_opts = {'outtmpl': '%(title)s'}
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
	clip.write_videofile(directory+'/'+name+'.mp4', fps=fps)
	os.remove(name)
	return(name+'.mp4')

# Downloads multiple videos from a list of youtube URLs to specified directory, returns a list of downloaded video names
def get_videos(urls, directory = 'vid/'):
	names = []
	for url in urls:
		names.append(get_video(url, directory))
	return names