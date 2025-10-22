# ☕ Mocha.sh

**Mocha.sh** is a minimalist, aesthetic CLI tool for developers —  
bringing a cozy, stylish touch to your terminal while helping you stay productive.  

---
## ☕ Installation

Mocha.sh is available for all major platforms —  
install it the way that fits your setup best.

---

### 🐍 **Universal (Recommended for all systems)**

Install globally with [pipx](https://pypa.github.io/pipx/):

```bash
pipx install mocha-sh
```
Or update:
```bash
pipx upgrade mocha-sh
```
Then run:
```bash 
mocha
```
🍎 macOS (via Homebrew)
```bash
brew tap mocha-sh/mocha
brew install mocha-sh
```
To update:
```bash
brew upgrade mocha-sh
```
🐧 Ubuntu / Debian (.deb package)
```bash
sudo apt install ./mocha-sh_0.1.6_all.deb
```
Or build it yourself:
```bash
sudo apt install dpkg-dev debhelper dh-python python3-all python3-setuptools
dpkg-buildpackage -us -uc
sudo apt install ../mocha-sh_0.1.6_all.deb
```
🪟 Windows (via Scoop)
```bash
scoop bucket add mocha https://github.com/mocha-sh/scoop-mocha
scoop install mocha-sh
``` 
To update:
```bash
scoop update mocha-sh
```
## 🌱 Features 

- **Quick Notes** – jot down small snippets or ideas directly from the terminal  
- **Focus Timer** – keep your workflow smooth and your coffee warm  
- **Stylish Output** – color-coded messages, ASCII art, icons  
- **Hydration Tracker** - add glasses to your Tracker
- **Coffee Tracker** - Track your Coffee
- **Plugins** - you can now create your own plugins for Mocha
- - **New Note/ File System** - i will add a new system for mocha files
  - 
![MochaEditor_2025-10-20T20_51_10_297548](https://github.com/user-attachments/assets/a6bc3a95-d832-484a-9fac-7c1cdbea5f61)
![MochaEditor_2025-10-20T21_01_35_736691](https://github.com/user-attachments/assets/61225954-b6fb-45e8-a739-1c6a78a266a2)
---

## 🕖 Coming soon

- **Themes & Prompts** – cozy terminal themes for your shell  
- **Small Utilities** – handy helper commands for everyday tasks  
- **Mocha.conf files** - full customizable mocha.sh
---

## How to use Mocha.sh

    mocha note "your note"

    mocha note list

    mocha note view <index>

    mocha note edit <index>

    mocha note delete <index>

    mocha timer 25 -  for a 25 Minutes Timer

    mocha hydrate add -adds one glass of water

    mocha hydrate stats - shows your stats

    mocha coffee add - adds on cup

    mocha coffee stats  - same as hydrate stats

---


    More commands and features will be added as Mocha.sh evolves ☕
