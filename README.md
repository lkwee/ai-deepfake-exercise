## AI Deepfake Audio and Video

A local pipeline to generate deepfake voice and videos **responsibly** using open-sourced models—without the need for GPU.

### 💡 Purpose

Deepfake voice and video technologies can be powerful tools when used ethically and responsibly. Some of the beneficial use cases include:

- **Cybersecurity awareness**: Demonstrating the risks and detectability of deepfake media.
- **Training & education**: Showing how AI-generated media works to improve digital literacy.
- **Entertainment & content creation**: Enhancing storytelling through voice cloning or realistic character rendering.
- **Accessibility**: Enabling people with disabilities to speak through synthetic voices tailored to their identity.

> ⚠️ **Note:** This project is intended for educational and ethical use only.

---

### 🧰 Pipeline Components

All components run on **local machines (CPU-compatible)**. No training is needed—just inference.

---

#### 1. [Resemble-Enhance](https://github.com/resemble-ai/resemble-enhance)
🔊 For **enhancing voice quality** before cloning.

- Works better using **Docker** on Windows.
- Helpful forks and issues:
  - Windows support: [Issue #1](https://github.com/resemble-ai/resemble-enhance/issues/1)
  - Dockerfile: [Issue #12](https://github.com/resemble-ai/resemble-enhance/issues/12)

---

#### 2. [F5-TTS](https://github.com/SWivid/F5-TTS)
🗣️ For **voice cloning**—no model training required. Fast inference, even on CPU.

**Docker setup:**
```bash
docker pull ghcr.io/swivid/f5-tts:main
docker run -it -p 7860:7860 ghcr.io/swivid/f5-tts:main
f5-tts_infer-gradio --port 7860 --host 0.0.0.0
```

---

#### 3. [Wav2Lip](https://github.com/Rudrabha/Wav2Lip)
👄 For **lip-syncing any video** to cloned audio.

- No training needed.
- Just run `inference.py` with input video and audio files.

---

#### 4. [GFPGAN](https://github.com/TencentARC/GFPGAN)
🧑‍🎤 For **face restoration** to enhance visual quality.

**Pipeline:**
1. Extract frames from the input video.
2. Run GFPGAN `inference.py` on each frame.
3. Recombine frames into video and overlay cloned audio.

---

