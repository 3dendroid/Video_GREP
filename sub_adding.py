# https://www.bannerbear.com/blog/how-to-add-subtitles-to-a-video-file-using-ffmpeg/ - source from this
# ffmpeg/bin/ffmpeg.exe -i video.mp4 -vf subtitles=subtitle.srt output_srt.mp4 - command for adding hard subs
# ffmpeg -i subtitle.srt subtitle.ass - converting srt to ass

# For SRT files , the options for the subtitle styles are limited. You can do basic styling using HTML markups like <b>, <i>, <u>, and <font>.
# ffmpeg -i input.mp4 -vf "subtitles=subtitle.srt:force_style='Fontname=Futura,PrimaryColour=&HFF00'" output_force_style.mp4 - command for ass subs
