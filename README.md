# Image Sequence → GIF (with Transitions)

This tool converts a folder of sequential images (`01.png`, `02.png`, etc.) into an animated GIF — with optional **fade** transitions between frames.

---

## 🚀 Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/image-to-gif.git
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
/output     ← generated GIFs appear here
make_gif.py
README.md
```

---

## 🧩 Usage

### 🖼️ Basic Example

```bash
python make_gif.py
```

This reads images from `/input`, combines them, and saves `/output/output.gif`.

---

### ⚙️ Advanced Example

```bash
python make_gif.py --input my_images --output results --name demo.gif --duration 150 --mode fade --fade-steps 15
```

**Options:**
| Flag | Description | Default |
|------|--------------|----------|
| `--input` | Input folder with images | `input` |
| `--output` | Output folder | `output` |
| `--name` | Output GIF filename | `output.gif` |
| `--duration` | Frame duration in milliseconds | `100` |
| `--mode` | Transition mode: `cut` (hard jump) or `fade` (smooth blend) | `cut` |
| `--fade-steps` | Number of frames in each fade transition | `10` |

---

## 🧠 Notes on Image Sizes

- The **first image’s size** determines the GIF’s size.  
- All other images are automatically resized to match.  
- For best results, ensure all images are **the same dimensions** before running.

---

## 🖼️ Supported Image Types

Supports: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`

---

## ✅ Example

Input:

```
/input
 ├─ 01.png
 ├─ 02.png
 ├─ 03.png
```

Run:

```bash
python make_gif.py --mode fade --duration 120 --fade-steps 20
```

Output:

```
/output/output.gif
```

🎉 You now have a smooth animated GIF with custom fade transitions!

---

## 🤝 Contributing & Reuse

This is just a small helpful script — feel free to:
- Fork it  
- Modify it  
- Add new transition modes  
- Fix bugs  
- Or use it in your own projects however you like  

If you make improvements, you’re welcome (but not required) to open a pull request so others can benefit too.  
No formal license required — it’s open and free to use. ❤️

---

*Made with Python & Pillow*

- A simple tool by [Ali Hammond on Github](https://www.github.com/Ali-Hammond/)