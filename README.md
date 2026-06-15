# RuView Phase Sanitization Enhancements

**Project**: Phase sanitization and preprocessing pipeline for [RuView](https://github.com/ruvnet/RuView)

**Based on** the paper:  
[**DensePose From WiFi**](https://arxiv.org/abs/2301.00250) by Jiaqi Geng, Dong Huang, Fernando De la Torre (CMU, 2022)

---

### Visualization Example

![Phase Sanitization Comparison](phase_comparison_example.jpg)

*Left: Raw noisy CSI phase*  *Right: Sanitized phase using method from the paper*

---

### Features

- Phase unwrapping + median filtering (core technique from the paper)
- Saves **full raw and sanitized phase arrays** in JSON format
- High-quality comparison plots
- Structured for multi-view fusion (2+ laptops/sensors)

### Installation & Quick Start

```bash
# 1. Clone this repo
git clone https://github.com/rblair01/ruview-phase-sanitizer.git
cd ruview-phase-sanitizer

# 2. Create virtual environment
python3 -m venv ~/ruview_venv
source ~/ruview_venv/bin/activate
pip install -r requirements.txt

# 3. Start RuView (simulation mode)
docker run -p 3000:3000 --name ruview --rm ruvnet/wifi-densepose:latest &

# 4. Start Phase Sanitizer
./run.sh

Open http://localhost:3000 to see the RuView Observatory.
Hardware Setup Guide
Install Ubuntu 20.04/22.04 on the T420
Install CSI Tool (iwl-csi)
Update the data source in phase_sanitizer_real.py (the script is already prepared for it)
Run both RuView and the sanitizer

Full hardware guide coming soon in docs/hardware.md.

Future Roadmap
Short-term: ESP32 nodes
Medium-term: Multi-view fusion (2+ laptops pointing at the same area)
Long-term: Real-time sanitized CSI streaming back into RuView
Jupyter notebooks for training and analysis
Transfer learning from the DensePose model
Support for multi-person through-wall scenarios

Project Structure

ruview-phase-sanitizer/
├── phase_sanitizer_real.py     # Main script
├── run.sh                      # Easy launcher
├── README.md
├── requirements.txt
├── .gitignore
├── phase_data/                 # JSON with full phase arrays
├── phase_plots/                # Comparison images
└── notebooks/                  # Analysis notebooks

Attribution
This work builds directly on:
RuView by ruvnet
"DensePose From WiFi" paper

License
MIT License — see LICENSE for details.Made for the WiFi sensing community.

