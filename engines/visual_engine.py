from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_images(script_lines, output_dir, size=(1080, 1920)):
    """
    Generates image slides for each line of the script.
    Returns a list of file paths.
    """
    image_paths = []
    
    # Try to load a nice font, otherwise fallback to default (which might be tiny but functional for a test)
    try:
        # Windows usually has arial
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()
        print("Warning: Arial font not found, using default.")

    for i, text in enumerate(script_lines):
        # Create black background image
        img = Image.new('RGB', size, color=(0, 0, 0))
        d = ImageDraw.Draw(img)
        
        # Wrap text
        wrapper = textwrap.TextWrapper(width=30) 
        word_list = wrapper.wrap(text=text)
        caption_new = '\n'.join(word_list)
        
        # Calculate text position to center it
        # specific to pillow versions, but getbbox is reliable enough for recent ones or textbbox
        try:
            left, top, right, bottom = d.textbbox((0, 0), caption_new, font=font)
            text_width = right - left
            text_height = bottom - top
        except AttributeError:
             # Fallback for older Pillow
            text_width, text_height = d.textsize(caption_new, font=font)

        x = (size[0] - text_width) / 2
        y = (size[1] - text_height) / 2
        
        d.multiline_text((x, y), caption_new, font=font, fill=(255, 255, 255), align="center")
        
        filename = os.path.join(output_dir, f"image_{i}.png")
        img.save(filename)
        image_paths.append(filename)
        print(f"Generated image: {filename}")
        
    return image_paths
