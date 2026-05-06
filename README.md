# RuView Phase Sanitization Enhancements

**Project**: Phase sanitization and preprocessing improvements for [RuView](https://github.com/ruvnet/RuView)

**Based on** the paper:  
[**DensePose From WiFi**](https://arxiv.org/abs/2301.00250) by Jiaqi Geng, Dong Huang, Fernando De la Torre (CMU, 2022)

---

## Features

- Implements phase unwrapping + median filtering from the *DensePose From WiFi* paper
- Saves full raw + sanitized CSI phase arrays in JSON format
- Ready for real Intel 5300 CSI data (research mode on ThinkPad T420)
- Visualization scripts (Matplotlib)
- Designed for multi-view fusion (2+ laptops)

## Project Structure

ruview-phase-sanitizer/
├── phase_sanitizer_real.py     # Main script (simulation + real CSI ready)
├── README.md
├── requirements.txt
├── phase_data/                 # Saved JSON files with full phase arrays
├── phase_plots/                # Generated comparison images
└── notebooks/                  # Future Jupyter analysis notebooks

## Attribution

This work builds directly on:
- [RuView](https://github.com/ruvnet/RuView) by ruvnet
- "DensePose From WiFi" paper (arXiv:2301.00250)

## Usage

```bash
source ~/ruview_venv/bin/activate
cd ~/ruview-phase-sanitizer
python phase_sanitizer_real.py

LicenseMIT License (same as RuView)Made with <3 for the WiFi sensing community.
