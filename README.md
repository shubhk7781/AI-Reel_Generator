# 🚀 VidSnapAI - AI-Powered Video Reel Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey.svg)](https://flask.palletsprojects.com/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-orange.svg)](https://elevenlabs.io/)

VidSnapAI is an innovative web application that transforms your text descriptions and images into engaging video reels using AI-powered text-to-speech and automated video editing. Create stunning short-form videos effortlessly with just a few clicks!

## ✨ Features

- 🎤 **AI Text-to-Speech**: Convert any text into natural-sounding audio using ElevenLabs' advanced TTS technology
- 🎬 **Automated Video Creation**: Seamlessly combine images with audio to generate professional-looking reels
- 🖼️ **Image Upload Support**: Upload multiple images (PNG, JPG, JPEG) to create dynamic slideshows
- ⚡ **Fast Processing**: Optimized FFmpeg integration for quick video rendering
- 🌐 **Web-Based Interface**: User-friendly Flask web app with responsive design
- 📱 **Mobile-Friendly**: Responsive templates for all device sizes
- 🔄 **Batch Processing**: Process multiple reels automatically

## 📸 Demo

![VidSnapAI Demo](demo.gif)

*Watch VidSnapAI in action! Upload images, add your script, and generate a professional video reel in minutes.*

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg (for video processing)
- ElevenLabs API key (sign up at [elevenlabs.io](https://elevenlabs.io/))

### Step-by-Step Setup

1. **Install Python dependencies**
   ```bash
   pip install flask elevenlabs
   ```

2. **Install FFmpeg**
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

4. **Configure API Key**
   - Open `config.py`
   - Replace the placeholder API key with your ElevenLabs API key:
     ```python
     APIKEY = "your_elevenlabs_api_key_here"
     ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Start creating your video reels!

## 📖 Usage

### Creating a Video Reel

1. **Access the Create Page**: Click "Create New Reel" from the homepage
2. **Upload Images**: Select multiple images (PNG, JPG, JPEG) for your slideshow
3. **Write Your Script**: Enter the text description that will be converted to speech
4. **Generate**: Click submit to process your reel
5. **Download**: Find your generated video in the `static/reels/` directory

### Gallery View

- Browse all your generated reels in the gallery
- View and download completed videos

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
ELEVENLABS_API_KEY=your_api_key_here
FLASK_ENV=development
```

### Customizing Video Settings

Modify `generate_reel.py` to adjust:
- Video resolution (default: 1080x1920 for vertical reels)
- Frame rate (default: 30 FPS)
- Audio settings

## 🚀 Deployment

### Local Development

```bash
export FLASK_APP=main.py
flask run
```


## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed

## 🙏 Acknowledgments

- [ElevenLabs](https://elevenlabs.io/) for the amazing text-to-speech API
- [FFmpeg](https://ffmpeg.org/) for video processing capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework


---

Made with ❤️ by [Shubham Kashyap](https://www.linkedin.com/in/shubham-kashyap-1b8047210/)

⭐ Star this repo if you find it useful!</content>
<parameter name="filePath">c:\shubh\Codes\PYTHON\Python_CWH\VidSnapAI\README.md
