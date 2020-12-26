import subprocess
input_file = 'video.MOV'
output_file = 'output.mkv'
subprocess.call('ffmpeg -i '+input_file +
                ' -c:v vp9 -c:a libvorbis '+output_file, shell=True)
