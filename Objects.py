class Video(object):
    size = 0
    def __init__(self, size):
        self.size = size

class Endpoint(object):
    videos = {}
    videoRequests = {}
    latencyToDataServer = 0
    latencyToCacheServers = {}


    def __init__(self, videos, latencyToCacheServer, latencyToDataServer):
        self.videos = videos
        self.latencyToCacheServer = latencyToCacheServer    
        self.latencyToDataServer = latencyToDataServer

    def setVideoRequests(self,video, numRequests):
        self.videoRequests[video] = numRequests


class CacheServer:
    endpoints = {}
    capacity = 0
    videos = {}
    def __init__(self, endpoints, capacity):
        self.endpoints = endpoints
        self.capacity = capacity
    
    def addVideo(self, key,video):
        self.videos.update({key,video})
        self.capacity -= video.size

    def add_endpoint(self, name, endpoint):
        self.endpoints.update({name: endpoint})

    def get_capacity(self):
        current_capacity = 0
        for i in self.videos:
            current_capacity += i.size
        return self.capacity - current_capacity


