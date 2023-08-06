from mutagen.mp4 import MP4
from pymediainfo import MediaInfo


def get_video_duration(file):
    video = MP4(file)

    if (video.info.length > 0): 
        return video.info.length
    else:    
        media_info = MediaInfo.parse(file)
        duration_in_ms = media_info.tracks[0].duration
        return duration_in_ms / 1000

