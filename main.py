import os
from Objects import Video, Endpoint

def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    datafile = '/'.join([dir_path, 'me_at_the_zoo.in'])

    videos = 0
    endpoints = 0
    requests = 0
    caches = 0
    capacity = 0

    video_objs = []
    endpoint_objs = {}
    cache_objs = {}

    with open(datafile) as f:
        info = f.readline().strip().split(' ')
        videos = int(info[0])
        endpoints = int(info[1])
        requests = int(info[2])
        caches = int(info[3])
        capacity = int(info[4])

        # create video objects
        for i in range(1, videos):
            videosizes = f.readline().strip().split(' ')

            for i in videosizes:
                video_objs.append(Video(int(i)))

        for endpoint in range(1, endpoints):
            endpoint_data = f.readline().strip().split(' ')
            # endpoint_object = Endpoint([], [], endpoint_data[0])
            caches = endpoint_data[1]
            for cache in caches:
                cache_data = f.readline().strip().split(' ')
                # get or create cache server
                cache = get_or_create_cacheserver(cache_data[0], cache_objs, capacity)
                cacheserver = CacheServer()
                latencies = f.readline().strip().split(' ')

def get_or_create_cacheserver(key, dict, capacity):
    cache = dict.get(key[0])
    if not cache:
        dict.update({key: CacheServer({}, capacity)})

if __name__ == '__main__':
    main()