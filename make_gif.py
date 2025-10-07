import os
import argparse
from PIL import Image

def fade_transition(img1, img2, steps=10):
    """
    Creates a smooth fade transition between two images.
    Returns a list of intermediate frames.
    """
    frames = []
    for i in range(1, steps + 1):
        alpha = i / steps
        frame = Image.blend(img1, img2, alpha)
        frames.append(frame)
    return frames


def make_gif(input_folder="input", output_folder="output", output_name="output.gif",
             duration=100, mode="cut", fade_steps=10):
    """
    Combine sequential images into a single animated GIF with optional transition effects.

    Args:
        input_folder (str): Folder where input images are stored.
        output_folder (str): Folder where the output GIF will be saved.
        output_name (str): Name of the output GIF file.
        duration (int): Duration per frame in milliseconds.
        mode (str): Transition mode ("cut" or "fade").
        fade_steps (int): Number of frames for each fade transition (smoothness).
    """
    os.makedirs(output_folder, exist_ok=True)

    valid_exts = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_exts)]
    files.sort()

    if not files:
        print("⚠️ No images found in the input folder.")
        return

    # Load images
    images = [Image.open(os.path.join(input_folder, f)).convert("RGBA") for f in files]
    first_size = images[0].size
    images = [img.resize(first_size) for img in images]

    frames = []
    for i in range(len(images) - 1):
        frames.append(images[i])
        if mode == "fade":
            fade_frames = fade_transition(images[i], images[i + 1], steps=fade_steps)
            frames.extend(fade_frames)

    frames.append(images[-1])  # Add last frame

    output_path = os.path.join(output_folder, output_name)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
        disposal=2
    )

    print(f"✅ GIF created successfully: {output_path}")
    print(f"🎞️ Mode: {mode.upper()} | Frames: {len(frames)} | Duration: {duration}ms | Fade Steps: {fade_steps}")


def main():
    parser = argparse.ArgumentParser(description="Combine images into an animated GIF with optional transitions.")
    parser.add_argument("--input", default="input", help="Input folder containing images")
    parser.add_argument("--output", default="output", help="Output folder for GIF")
    parser.add_argument("--name", default="output.gif", help="Output GIF file name")
    parser.add_argument("--duration", type=int, default=100, help="Frame duration in milliseconds")
    parser.add_argument("--mode", choices=["cut", "fade"], default="cut", help="Transition mode")
    parser.add_argument("--fade-steps", type=int, default=10, help="Number of frames for fade transitions")

    args = parser.parse_args()
    make_gif(
        input_folder=args.input,
        output_folder=args.output,
        output_name=args.name,
        duration=args.duration,
        mode=args.mode,
        fade_steps=args.fade_steps
    )


if __name__ == "__main__":
    main()
