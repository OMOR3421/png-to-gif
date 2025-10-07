# Image Sequence to GIF Converter

A simple Python tool to combine sequential images (`01.png`, `02.png`, `03.png`, etc.) into an animated GIF.

---

## 🚀 Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/Ali-Hammond/png-to-gif.git
   cd image-to-gif
   ```

2. **Install dependencies**

   ```bash
   pip install Pillow
   ```

---

## 📁 Folder Structure

```
/input      ← place your images here
/output     ← the generated GIF will appear here
make_gif.py
README.md
```

---

## 🖼️ Supported Image Types

You can use **any image format**, including:
- `.png`
- `.jpg` / `.jpeg`
- `.webp`
- `.bmp`
- `.tiff`

---

## 🧩 How to Use

1. Add your images in the `/input` folder, named in order:
   ```
   01.png
   02.png
   03.png
   ...
   ```
2. Run the script:
   ```bash
   python make_gif.py
   ```
3. Your GIF will be saved as:
   ```
   /output/output.gif
   ```

---

## ⚙️ Options (Optional Parameters)

You can change output name, folder, or frame duration by editing the function call in the script:

```python
make_gif(
    input_folder="input",
    output_folder="output",
    output_name="my_animation.gif",
    duration=150  # frame duration in ms
)
```

---

## 🧠 Notes on Image Sizes

- The **first image’s size** determines the final GIF’s size.
- If other images differ in size, they are **automatically resized** to match.
- For best results, make sure all images have **the same dimensions** before running the script.

---

## ✅ Example

If your `/input` folder contains:

```
01.png
02.png
03.png
04.png
```

You’ll get:

```
/output/output.gif
```

🎉 That’s it!

- A simple tool by [Ali Hammond on Github](https://www.github.com/Ali-Hammond/)