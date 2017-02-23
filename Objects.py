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
        running_cache_latency = 0
        running_ds_latency = 0
        video_scores = {}

        for key,value in self.endpoints.items():
            running_cache_latency += value.latencyToCacheServers(self.index)      
            running_ds_latency += value.latencyToDataServer()      
            for index, videoVal in value.videoRequests:
                video_scores[index] += videoVal

        running_cache_latency /= self.endpoints.len()
        running_ds_latency /= self.endpoints.len()
        running_score = 0
        
        for value in video_scores.keys():
            running_score += running_ds_latency*value - running_cache_latency * value  

        return running_score