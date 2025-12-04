#!/bin/bash

echo "🤖 GitHub Auto-Coder - Installation"
echo "===================================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create config from example
if [ ! -f "config.json" ]; then
    echo ""
    echo "⚙️  Creating config.json from example..."
    cp config.example.json config.json
    echo "   ✅ config.json created"
    echo ""
    echo "⚠️  WICHTIG: Bitte bearbeite config.json und füge deinen GitHub Token ein!"
    echo ""
    echo "   So erhältst du einen GitHub Token:"
    echo "   1. Gehe zu: https://github.com/settings/tokens"
    echo "   2. Klicke auf 'Generate new token' → 'Generate new token (classic)'"
    echo "   3. Gebe einen Namen ein (z.B. 'Auto-Coder')"
    echo "   4. Wähle Berechtigungen: ✅ repo (alle)"
    echo "   5. Klicke 'Generate token'"
    echo "   6. Kopiere den Token und füge ihn in config.json ein"
    echo ""
else
    echo ""
    echo "   ℹ️  config.json existiert bereits"
fi

echo ""
echo "✅ Installation abgeschlossen!"
echo ""
echo "🚀 Verwendung:"
echo "   python auto_coder.py "Erstelle eine Flask Web-App""
echo "   python auto_coder.py --interactive"
echo "   python web_interface.py  # Web-Interface starten"
echo ""
