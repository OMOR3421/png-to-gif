import os
from PIL import Image

def make_gif(input_folder="input", output_folder="output", output_name="output.gif", duration=100):
    """
    Combine sequential images into a single animated GIF.

    Args:
        input_folder (str): Folder where input images are stored.
        output_folder (str): Folder where the output GIF will be saved.
        output_name (str): Name of the output GIF file.
        duration (int): Duration per frame in milliseconds.
    """
    # Create output folder if it doesn’t exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all image files (any format)
    valid_exts = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_exts)]
    files.sort()

    if not files:
        print("⚠️ No images found in the input folder.")
        return

    # Load all images
    images = [Image.open(os.path.join(input_folder, f)) for f in files]

    # Resize all images to match the first one (if necessary)
    first_size = images[0].size
    images = [img.resize(first_size) for img in images]

    # Save as GIF
    output_path = os.path.join(output_folder, output_name)
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )

    print(f"✅ GIF created successfully: {output_path}")

if __name__ == "__main__":
    make_gif()
