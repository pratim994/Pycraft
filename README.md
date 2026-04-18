
---

# Pycraft 🎮

*A Python-based Game Engine for 3D Worlds*

Pycraft is a lightweight Python game engine designed for experimenting with 3D rendering, procedural terrain generation, shaders, and basic game mechanics. It serves as a learning-focused engine for graphics programming and game development.

---

![Demo](output.gif)


## 🚀 Features

* 3D rendering pipeline
* Camera and frustum handling
* Procedural terrain generation
* Shader support
* Scene and object management
* Modular architecture for easy extension

---

## 📁 Project Structure

```
Pycraft/
│
├── assets/             # Textures, models, and other assets
├── meshes/             # Mesh data and geometry
├── shaders/            # GLSL shader programs
├── world_objects/      # Game world entities
│
├── camera.py           # Camera system
├── frustum.py          # View frustum culling
├── main.py             # Entry point
├── noise.py            # Procedural noise generation
├── player.py           # Player logic
├── scene.py            # Scene management
├── settings.py         # Engine configuration
├── shader_program.py   # Shader handling
├── terrain_gen.py      # Terrain generation
```

---

## ⚙️ Requirements

Make sure you have:

* Python 3.8+
* pip

### Install dependencies


```bash
pip install pygame moderngl numpy pyglm
```

---

## 🛠️ How to Build & Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Pycraft.git
cd Pycraft
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

* **Linux / Mac**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install pygame moderngl numpy pyglm
```

---

### 4. Run the engine

```bash
python main.py
```

---

## 🎮 Controls (example – customize as needed)

| Key           | Action      |
| ------------- | ----------- |
| W / A / S / D | Move player |
| Mouse         | Look around |
| Space         | Jump        |
| ESC           | Exit        |

---

## 🧠 How It Works

* **Rendering**: Uses shaders to draw 3D objects
* **Camera**: Handles view transformations
* **Terrain**: Generated procedurally using noise
* **Scene**: Manages objects and rendering order
* **Shaders**: Define how objects appear on screen

---

## 🧩 Extending the Engine

You can:

* Add new world objects in `world_objects/`
* Create custom shaders in `shaders/`
* Modify terrain generation logic in `terrain_gen.py`
* Add physics or collision systems

---

## 🐛 Troubleshooting

* **Black screen** → Check OpenGL support and drivers
* **Module not found** → Ensure dependencies are installed
* **Performance issues** → Try reducing terrain complexity

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and improve the engine.

---


---

