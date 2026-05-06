#!/bin/bash
echo "🚀 Starting RuView + Phase Sanitizer..."

# Start RuView in background
docker rm -f ruview 2>/dev/null || true
docker run -p 3000:3000 --name ruview --rm ruvnet/wifi-densepose:latest &

sleep 5

# Start Phase Sanitizer
source ~/ruview_venv/bin/activate
cd ~/ruview-phase-sanitizer
python phase_sanitizer_real.py
