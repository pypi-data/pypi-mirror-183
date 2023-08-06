import xml.etree.ElementTree as ET
import hashlib
import os

def render_mlt(mlt_file_path, output_file_path):
    # Render the mlt file
    os.system(f"melt {mlt_file_path} -consumer avformat:{output_file_path} vcodec=libx264 acodec=aac")

# Create a class that holds the mlt project
class Melt:
    def __init__(self, width, height, fps):
        self.root = ET.Element('mlt')
        self.root.set('title', 'MLT Project')
        self.root.set('version', '7.5.0')
        self.root.set('LC_NUMERIC', 'C')
        self.root.set('producer', 'main_bin')

        # Set the profile
        self._set_profile(width, height, fps)
        
        # Create the main playlist
        self.main_playlist = ET.SubElement(self.root, 'playlist')
        self.main_playlist.set('id', 'main_bin')
        self.main_playlist.set('autoclose', '1')

        self.main_playlist_property = ET.SubElement(self.main_playlist, 'property')
        self.main_playlist_property.set('name', 'xml_retain')
        self.main_playlist_property.text = "1"

        self.chains = []
        self.playlists = []

    def _set_profile(self, width, height, fps):
        self.profile = ET.SubElement(self.root, 'profile')
        self.profile.set('description', f'HDV {height}p {fps}fps')
        self.profile.set('frame_rate_num', str(fps))
        self.profile.set('frame_rate_den', '1')
        self.profile.set('width', str(width))
        self.profile.set('height', str(height))
        self.profile.set('progressive', '1')
        self.profile.set('sample_aspect_num', '1')
        self.profile.set('sample_aspect_den', '1')
        self.profile.set('display_aspect_num', '16')
        self.profile.set('display_aspect_den', '9')
        self.profile.set('colorspace', '709')
    
    def _set_tractor(self, final_duration):
        tractor_0 = ET.SubElement(self.root, 'tractor')
        tractor_0.set('id', 'tractor0')
        tractor_0.set('title', 'Shotcut version 22.01.30')
        tractor_0.set('in', '00:00:00.000')
        tractor_0.set('out', self._seconds_to_timestamp(final_duration))

        tractor_0_property_shotcut = ET.SubElement(tractor_0, 'property')
        tractor_0_property_shotcut.set('name', 'shotcut')
        tractor_0_property_shotcut.text = '1'

        tractor_0_property_projectAudioChannels = ET.SubElement(tractor_0, 'property')
        tractor_0_property_projectAudioChannels.set('name', 'shotcut:projectAudioChannels')
        tractor_0_property_projectAudioChannels.text = '2'

        tractor_0_property_projectFolder = ET.SubElement(tractor_0, 'property')
        tractor_0_property_projectFolder.set('name', 'shotcut:projectFolder')
        tractor_0_property_projectFolder.text = '0'

        tractor_0_track_playlist = ET.SubElement(tractor_0, 'track')
        tractor_0_track_playlist.set('producer', 'background')

        # add all playlists to the tractor
        for playlist in self.playlists:
            if playlist.get('id') == 'background':
                continue
            tractor_0_track_playlist = ET.SubElement(tractor_0, 'track')
            tractor_0_track_playlist.set('producer', playlist.get('id'))


        tractor_0_track_transition0 = ET.SubElement(tractor_0, 'transition')
        tractor_0_track_transition0.set('id', 'transition0')

        tractor_0_track_transition0_a_track = ET.SubElement(tractor_0_track_transition0, 'property')
        tractor_0_track_transition0_a_track.set('name', 'a_track')
        tractor_0_track_transition0_a_track.text = '0'

        tractor_0_track_transition0_b_track = ET.SubElement(tractor_0_track_transition0, 'property')
        tractor_0_track_transition0_b_track.set('name', 'b_track')
        tractor_0_track_transition0_b_track.text = '1'

        tractor_0_track_transition0_mlt_service = ET.SubElement(tractor_0_track_transition0, 'property')
        tractor_0_track_transition0_mlt_service.set('name', 'mlt_service')
        tractor_0_track_transition0_mlt_service.text = 'mix'

        tractor_0_track_transition0_always_active = ET.SubElement(tractor_0_track_transition0, 'property')
        tractor_0_track_transition0_always_active.set('name', 'always_active')
        tractor_0_track_transition0_always_active.text = '1'

        tractor_0_track_transition0_sum = ET.SubElement(tractor_0_track_transition0, 'property')
        tractor_0_track_transition0_sum.set('name', 'sum')
        tractor_0_track_transition0_sum.text = '1'


        tractor_0_track_transition1 = ET.SubElement(tractor_0, 'transition')
        tractor_0_track_transition1.set('id', 'transition1')

        tractor_0_track_transition1_a_track = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition1_a_track.set('name', 'a_track')
        tractor_0_track_transition1_a_track.text = '0'

        tractor_0_track_transition1_b_track = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition1_b_track.set('name', 'b_track')
        tractor_0_track_transition1_b_track.text = '1'

        tractor_0_track_transition1_version = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition1_version.set('name', 'version')
        tractor_0_track_transition1_version.text = '0.1'

        tractor_0_track_transition1_mlt_service = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition1_mlt_service.set('name', 'mlt_service')
        tractor_0_track_transition1_mlt_service.text = 'frei0r.cairoblend'

        tractor_0_track_transition1_always_active = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition1_always_active.set('name', 'threads')
        tractor_0_track_transition1_always_active.text = '0'

        tractor_0_track_transition0_sum = ET.SubElement(tractor_0_track_transition1, 'property')
        tractor_0_track_transition0_sum.set('name', 'disable')
        tractor_0_track_transition0_sum.text = '1'

    def _compute_hash(self, path_to_video):
        file_hash = hashlib.md5()
        with open(path_to_video, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                file_hash.update(chunk)
        return file_hash.hexdigest()

    def _compute_duration(self, path_to_video):
        return float(os.popen(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {path_to_video}').read()[:-2])

    def _seconds_to_timestamp(self, seconds):
        milliseconds = round(seconds*1000)
        seconds, ms = divmod(milliseconds, 1000)
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%02d:%02d:%02d.%03d" % (hour, min, sec, ms)
    
    def _timestamp_to_seconds(self, timestamp):
        hour, min, sec = timestamp.split(':')
        return int(hour)*3600 + int(min)*60 + float(sec)

    def _compute_final_duration(self):
        longest_duration = 0
        for playlist in self.playlists:
            current_duration = 0
            # go through all children of the playlist
            for child in playlist:
                if child.tag == 'entry':
                    in_time = self._timestamp_to_seconds(child.get('in'))
                    out_time = self._timestamp_to_seconds(child.get('out'))
                    current_duration += out_time - in_time
                if child.tag == 'blank':
                    current_duration += self._timestamp_to_seconds(child.get('length'))
            
            if current_duration > longest_duration:
                longest_duration = current_duration
        return longest_duration

    def _create_background(self, final_duration):
        # create the background producer
        background = ET.SubElement(self.root, 'producer')
        background.set('id', 'black')
        background.set('in', self._seconds_to_timestamp(0))
        background.set('out', self._seconds_to_timestamp(final_duration))
        # add the length, eof, resource, mlt_service, aspect_ratio, mlt_image_format, set.test:audio properties
        background_length = ET.SubElement(background, 'property')
        background_length.set('name', 'length')
        background_length.text = self._seconds_to_timestamp(final_duration)
        background_eof = ET.SubElement(background, 'property')
        background_eof.set('name', 'eof')
        background_eof.text = 'pause'
        background_resource = ET.SubElement(background, 'property')
        background_resource.set('name', 'resource')
        background_resource.text = '0'
        background_mlt_service = ET.SubElement(background, 'property')
        background_mlt_service.set('name', 'mlt_service')
        background_mlt_service.text = 'color'
        background_aspect_ratio = ET.SubElement(background, 'property')
        background_aspect_ratio.set('name', 'aspect_ratio')
        background_aspect_ratio.text = '1'
        background_mlt_image_format = ET.SubElement(background, 'property')
        background_mlt_image_format.set('name', 'mlt_image_format')
        background_mlt_image_format.text = 'rgba'
        background_set_test_audio = ET.SubElement(background, 'property')
        background_set_test_audio.set('name', 'set.test_audio')
        background_set_test_audio.text = '0'
        # create the background playlist
        background_playlist = ET.SubElement(self.root, 'playlist')
        background_playlist.set('id', 'background')
        background_playlist.set('autoclose', '1')
        # add the producer entry
        background_playlist_entry = ET.SubElement(background_playlist, 'entry')
        background_playlist_entry.set('producer', 'black')
        background_playlist_entry.set('in', self._seconds_to_timestamp(0))
        background_playlist_entry.set('out', self._seconds_to_timestamp(final_duration))
        # add the background playlist to playlists
        self.playlists.append(background_playlist)

    def add_video(self, path_to_video, playlist=None):
        """
        Add a video file to the project
        
        :param path_to_video: path to the video file
        :param playlist: the playlist to add the video to. If None, the video will be added to the first playlist

        :return: The xml element of the video
        """
        video_hash = self._compute_hash(path_to_video)
        video = ET.SubElement(self.root, 'chain')
        chain_index = len(self.chains)
        video_duration = self._seconds_to_timestamp(self._compute_duration(path_to_video))
        video.set('id', f'chain{chain_index}')
        video.set('out', str(video_duration))

        # add the length, eof, resource, mlt_service, seekable, audio_index, video_index, mute_on_pause, shotcut:hash and shotcut:caption properties
        video_length = ET.SubElement(video, 'property')
        video_length.set('name', 'length')
        video_length.text = str(video_duration)

        video_eof = ET.SubElement(video, 'property')
        video_eof.set('name', 'eof')
        video_eof.text = 'pause'

        video_resource = ET.SubElement(video, 'property')
        video_resource.set('name', 'resource')
        video_resource.text = path_to_video

        video_mlt_service = ET.SubElement(video, 'property')
        video_mlt_service.set('name', 'mlt_service')
        video_mlt_service.text = 'avformat-novalidate'

        video_seekable = ET.SubElement(video, 'property')
        video_seekable.set('name', 'seekable')
        video_seekable.text = '1'

        video_audio_index = ET.SubElement(video, 'property')
        video_audio_index.set('name', 'audio_index')
        video_audio_index.text = '1'

        video_video_index = ET.SubElement(video, 'property')
        video_video_index.set('name', 'video_index')
        video_video_index.text = '0'

        video_mute_on_pause = ET.SubElement(video, 'property')
        video_mute_on_pause.set('name', 'mute_on_pause')
        video_mute_on_pause.text = '0'

        shotcut_hash = ET.SubElement(video, 'property')
        shotcut_hash.set('name', 'shotcut:hash')
        shotcut_hash.text = video_hash

        shotcut_caption = ET.SubElement(video, 'property')
        shotcut_caption.set('name', 'shotcut:caption')
        shotcut_caption.text = path_to_video

        # add to the playlist
        if playlist is not None:
            entry = ET.SubElement(playlist, 'entry')
            entry.set('producer', f'chain{chain_index}')
            entry.set('in', '00:00:00.000')
            entry.set('out', self._seconds_to_timestamp(video_duration))
            self.chains.append(video)

        return video

    def add_section_to_playlist(self, chain, section, playlist):
        entry = ET.SubElement(playlist, 'entry')
        entry.set('producer', chain.get("id"))
        entry.set('in', self._seconds_to_timestamp(section[0]))
        entry.set('out', self._seconds_to_timestamp(section[1]))

    def add_playlist(self, name):
        playlist = ET.SubElement(self.root, 'playlist')
        playlist.set('id', name)
        playlist.set('autoclose', '1')

        # add properties
        s_v_property = ET.SubElement(playlist, 'property')
        s_v_property.set('name', 'shotcut:video')
        s_v_property.text = str(len(self.playlists))

        s_n_property = ET.SubElement(playlist, 'property')
        s_n_property.set('name', 'shotcut:name')
        s_n_property.text = name

        self.playlists.append(playlist)
        return playlist

    def save_mlt(self, path_to_mlt):

        final_duration = self._compute_final_duration()
        
        self._create_background(final_duration)
        self._set_tractor(final_duration)

        with open(path_to_mlt, 'w') as f:
            f.write(ET.tostring(self.root, encoding='unicode'))
            

        


