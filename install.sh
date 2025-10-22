#!/bin/bash
echo "☕ Installing Mocha.sh locally..."
mkdir -p ~/.local/bin
echo '#!/usr/bin/env bash' > ~/.local/bin/mocha
echo "python3 $(pwd)/mocha.py \"\$@\"" >> ~/.local/bin/mocha
chmod +x ~/.local/bin/mocha
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo "✅ Mocha installed. Try: mocha greet"
