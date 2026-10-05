# 🚀 Space Invader Game

A classic-style **Space Invaders-inspired arcade game built with Python and Pygame**.

This is an older personal game project that has been refreshed with clearer documentation, reproducible dependencies, safer asset loading, and a cleaner Python structure while keeping the original gameplay simple.

![Space Invader Game](https://github.com/SandeepKomal/SpaceInvaderGame/assets/99358567/9d2571bd-83f5-4d51-929f-d08efbc146b2)

## ✨ Features

- 🛸 Player-controlled spaceship
- ⬅️➡️ Left/right movement
- 🔫 Spacebar firing
- 👾 Multiple alien enemies
- 💥 Collision detection
- 🏆 Score tracking
- 🎵 Background music and sound effects
- ☠️ Game-over state
- 🎨 Bundled graphics and audio assets

## 🛠️ Tech stack

- Python 3
- Pygame 2.6
- PNG/JPG game assets
- WAV audio assets

## 📁 Project structure

```text
SpaceInvaderGame/
├── game.py
├── requirements.txt
├── Dockerfile
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── *.png
├── *.wav
└── Waffle Story.ttf
```

## ▶️ Run locally

### 1. Clone

```bash
git clone https://github.com/SandeepKomal/SpaceInvaderGame.git
cd SpaceInvaderGame
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the game

```bash
python game.py
```

## 🎮 Controls

| Key | Action |
|---|---|
| **←** | Move left |
| **→** | Move right |
| **Space** | Fire |

## 🎯 Gameplay

Destroy the incoming aliens before they reach the lower part of the screen.

The current version uses:

- 800 × 600 game window
- 6 enemies
- Horizontal player movement
- Single-shot firing
- Score-based gameplay
- 60 FPS frame pacing

## 🧹 Modernization

The original code has been cleaned up while preserving its core gameplay:

- Added a `main()` entry point.
- Asset paths now resolve relative to the project directory.
- Added a fixed game clock for smoother frame pacing.
- Replaced unsafe string identity checks such as `is "ready"` with value comparisons.
- Audio loading failures no longer immediately terminate the game.
- Added reproducible `requirements.txt`.
- Added development ignore rules.
- Added contribution and security guidance.

## 🐳 Docker note

A Dockerfile is retained for historical/experimental use.

Because this is a graphical Pygame application, a normal container running on a headless server will **not automatically display the game window**. For the intended experience, run the project directly on a desktop with Python and Pygame.

## 🗺️ Roadmap

- [ ] Restart without closing the application
- [ ] Multiple levels
- [ ] High-score persistence
- [ ] Pause/resume
- [ ] Configurable difficulty
- [ ] Improved collision boundaries
- [ ] Automated tests for non-rendering game logic
- [ ] Browser/playable build
- [ ] Modern gameplay GIF in the README

## 🎨 Assets and licensing

This repository contains bundled visual, audio, and font assets.

The original `More Info.txt` is retained as a reference for the **Waffle Story** font and its creator/licensing information.

Before redistributing the project commercially or publishing derivative versions, verify that you have the appropriate rights for every bundled asset. The source-code license does not automatically grant rights to third-party assets.

## 🤝 Contributing

Bug fixes, gameplay improvements, documentation improvements, tests, and roadmap features are welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## 🔐 Security

Do not commit passwords, API keys, tokens, private keys, or other sensitive information.

See [SECURITY.md](SECURITY.md).

## 📜 License

The project source code is available under the MIT License. See [LICENSE](LICENSE).

Asset-specific licenses may differ.

---

⭐ If you enjoy this project, consider starring the repository and sharing it with someone learning Python or game development.
