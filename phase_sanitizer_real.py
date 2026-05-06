import numpy as np
import requests
import time
from scipy.ndimage import median_filter
import json
import os

print("🔬 RuView Phase Sanitization - Full Data Saving Mode")
print("Now saving actual raw + sanitized phase arrays in JSON\n")

os.makedirs("phase_data", exist_ok=True)
counter = 0

def sanitize_phase(raw_phase):
    """Phase sanitization from DensePose From WiFi paper"""
    phase = np.unwrap(raw_phase, axis=0)
    phase = median_filter(phase, size=(9, 5, 1))
    return phase

while True:
    try:
        resp = requests.get("http://localhost:3000/api/v1/sensing/latest", timeout=2)
        if resp.status_code == 200:
            data = resp.json()
            persons = data.get('persons', 0)
            fps = data.get('fps', 0)
            counter += 1

            # === Structured simulation (replace with real CSI later) ===
            t = np.linspace(0, 30, 60)
            f = np.linspace(0, 15, 30)
            raw_phase = np.zeros((60, 30, 9))
            for i in range(9):
                raw_phase[:, :, i] = np.sin(t[:, None] * (1 + i*0.3) + f[None, :]) * 2.0 + np.random.randn(60, 30) * 0.4

            sanitized = sanitize_phase(raw_phase)

            # === Save FULL data to JSON ===
            save_data = {
                "frame": counter,
                "timestamp": time.time(),
                "persons": persons,
                "fps": fps,
                "raw_phase": raw_phase.tolist(),           # Actual array
                "sanitized_phase": sanitized.tolist(),     # Sanitized array
                "raw_shape": raw_phase.shape,
                "sanitized_shape": sanitized.shape
            }

            filename = f"phase_data/frame_{counter:05d}.json"
            with open(filename, "w") as f:
                json.dump(save_data, f, indent=2)

            if counter % 10 == 0:
                print(f"✅ Saved full data: {filename} | Persons: {persons}")

    except Exception as e:
        print(f"Connection issue: {e}")

    time.sleep(0.3)
