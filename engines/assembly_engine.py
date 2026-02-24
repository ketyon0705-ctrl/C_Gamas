from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

def assemble_video(audio_paths, image_paths, output_filename):
    """
    Combines audio and image files into a single video.
    """
    clips = []
    
    if len(audio_paths) != len(image_paths):
        raise ValueError("Number of audio files and image files must match.")
        
    for audio_path, image_path in zip(audio_paths, image_paths):
        audio_clip = AudioFileClip(audio_path)
        # Create an ImageClip with the same duration as the audio
        image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
        image_clip = image_clip.set_audio(audio_clip)
        
        clips.append(image_clip)
        
    final_video = concatenate_videoclips(clips, method="compose")
    
    # Write the result to a file
    # fps=24 is standard enough for this slide-show style
    final_video.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
    print(f"Video saved to {output_filename}")
