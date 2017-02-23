class Video(object):
    size = 0
    def __init__(self, size):
        self.size = size

class Endpoint(object):
    videos = []
    videoRequests = []
    latencyToDataServer = 0
    latencyToCacheServer = 0
    def __init__(self, videos, latencyToCacheServer, latencyToDataServer):
        self.videos = videos
        self.latencyToCacheServer = latencyToCacheServer    
        self.latencyToDataServer = latencyToDataServer

    def setVideoRequests(self,video, numRequests):
        self.videoRequests[video] = numRequests
class CacheServer:
    endpoints = []
    capacity = 0
    videos = []
    def __init__(self, endpoints, capacity):
        self.endpoints = endpoints
        self.capacity = capacity
    
    def addVideo(self, video):
        self.videos.append(video)
        self.capacity -= video.size
