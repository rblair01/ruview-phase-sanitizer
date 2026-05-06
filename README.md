# RuView Phase Sanitization Enhancements

**Project**: Phase sanitization and preprocessing pipeline for [RuView](https://github.com/ruvnet/RuView)

**Based on** the paper:  
[**DensePose From WiFi**](https://arxiv.org/abs/2301.00250) by Jiaqi Geng, Dong Huang, Fernando De la Torre (CMU, 2022)

---

### Goal

Improve WiFi CSI phase quality for better human pose estimation by implementing the phase sanitization techniques from the DensePose From WiFi paper.

### Features

- Phase unwrapping + median filtering (core method from the paper)
- Saves **full raw and sanitized phase arrays** in JSON format
- Ready for real Intel 5300 CSI data (research mode)
- High-quality comparison plots (Raw vs Sanitized)
- Easy to extend for multi-view fusion (2+ sensors/laptops)

### Project Structure

ruview-phase-sanitizer/
├── phase_sanitizer_real.py     # Main script (simulation + real CSI ready)
├── run.sh                      # One-command launcher
├── README.md
├── requirements.txt
├── .gitignore
├── phase_data/                 # JSON files with full phase arrays
├── phase_plots/                # Generated comparison images
└── notebooks/                  # Analysis notebooks

### Quick Start

```bash
# 1. Start RuView (simulation mode)
docker run -p 3000:3000 --name ruview --rm ruvnet/wifi-densepose:latest

# 2. In another terminal, run the sanitizer
source ~/ruview_venv/bin/activate
cd ~/ruview-phase-sanitizer
./run.sh

Open http://localhost:3000 to see the RuView dashboard.UsagePlots are saved in phase_plots/
Full phase data (raw + sanitized) is saved in phase_data/
When Intel 5300 hardware is ready, the script is already structured to accept real CSI data.

AttributionThis work builds directly on:RuView by ruvnet
"DensePose From WiFi" paper

LicenseMIT License — see LICENSE for details.Made for the WiFi sensing community.

dbe2925 (Update README.md with improved documentation and instructions)
