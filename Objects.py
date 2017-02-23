class Video(object):
    index = 0
    size = 0
    def __init__(self,index, size):
        self.size = size
        self.index = index

class Endpoint(object):
    videos = {}
    videoRequests = {}
    latencyToDataServer = 0
    latencyToCacheServers = {}
    index = 0

    def __init__(self, videos, latencyToCacheServer, latencyToDataServer, index):
        self.videos = videos
        self.latencyToCacheServer = latencyToCacheServer    
        self.latencyToDataServer = latencyToDataServer
        self.index = index

    def setVideoRequests(self,video, numRequests):
        self.videoRequests[video] = numRequests


class CacheServer:
    index = 0
    endpoints = {}
    capacity = 0
    videos = {}
    score = 0

    def __init__(self, endpoints, capacity, index):
        self.endpoints = endpoints
        self.capacity = capacity
        self.index = index

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
    def get_score(self):
        running_latency = 0
        video_scores = {}
        for key,value in endpoints.items():
            runningLatency += value.latencyToCacheServers(self)


    def calculate_avg_latenc        

