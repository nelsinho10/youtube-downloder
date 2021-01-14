# -*- coding: utf-8 -*-

from pytube import YouTube
import os
import math
import datetime


class Controller:
    def __init__(self, url='',resolution=''):
        self.setUrl(url)
        self.setResolution(resolution)

    def getUrl(self):
        return self.url

    def setUrl(self,url):
        self.url = url

    def setResolution(self,resolution):
        self.resolution = resolution
 
    def getNameVideo(self):
        yt = YouTube(self.url)
        return yt.title

    def getDuration(self):
        yt = YouTube(self.url)
        timeDuration = str( datetime.timedelta(seconds= yt.length))
        return timeDuration

    def getSize(self):
        yt = YouTube(self.url)
        streams = yt.streams.filter(file_extension='mp4')
        r = ''
        for stream in streams:
            if (stream.resolution == self.resolution):

                s = stream.filesize * (9.537*(10**(-7)))
                r = "{0:.2f}".format(s)
                self.res = r 
                break
        return r

    def video(self):
        yt = YouTube(self.url)
        streams = yt.streams.filter(file_extension='mp4')
        
        for stream in streams:
            if (stream.resolution == self.resolution ):
                stream.download(filename='video')
                self.music()
                self.join()
                break

    def music(self):
        yt = YouTube(self.url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename='audio')

    def formats(self):
        temp = []
        resolutions = []
        yt = YouTube(self.url)
        streams = yt.streams.filter(file_extension='mp4')
        
        for stream in streams:
            temp.append(stream.resolution)
        
        for t in temp:
            if( t not in resolutions ):
                resolutions.append(t)

        return resolutions

    def join(self):
        yt = YouTube(self.url)
        name = yt.title
        os.system('ffmpeg -i video.mp4 -i audio.mp4 -c:v copy -c:a copy output.mp4')
        os.remove('audio.mp4')
        os.remove('video.mp4')
        os.rename('output.mp4', '%s.mp4' %name)

