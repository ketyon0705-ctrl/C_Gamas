import os
import config
from engines import script_engine, audio_engine, visual_engine, assembly_engine

def main():
    print("=== AutoMedia-AG Started ===")
    
    # 1. Script Generation
    print("1. Generating Script...")
    script = script_engine.generate_script(config.VIDEO_THEME)
    print("Script:", script)
    
    # 2. Audio Generation
    print("2. Generating Audio...")
    audio_paths = audio_engine.generate_audio(script, config.AUDIO_DIR)
    
    # 3. Visual Generation
    print("3. Generating Visuals...")
    image_paths = visual_engine.generate_images(script, config.IMAGE_DIR, config.VIDEO_SIZE)
    
    # 4. Assembly
    print("4. Assembling Video...")
    assembly_engine.assemble_video(audio_paths, image_paths, config.OUTPUT_FILENAME)
    
    print("=== AutoMedia-AG Finished Successfully ===")

if __name__ == "__main__":
    main()
