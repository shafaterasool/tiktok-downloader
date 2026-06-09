# tiktok-downloader
A Python CLI tool to download all videos from any TikTok channel using yt-dlp. Features parallel downloads, timestamped folder organization, auto error-skipping, and cross-platform support (Windows, macOS, Linux).

# 📱 TikTok Channel Downloader

A simple Python CLI tool to download all videos from any TikTok channel using `yt-dlp`. Fast, lightweight, and cross-platform.

---

## ✨ Features

- 📥 Downloads all videos from any TikTok channel or profile
- 📂 Organizes downloads into timestamped folders automatically
- ⚡ Supports 4 parallel downloads for faster speed
- 🔧 Auto-installs `yt-dlp` if not already present
- 🛡️ Skips failed videos and continues downloading the rest (`--ignore-errors`)
- 🖥️ Cross-platform support: Windows, macOS, Linux
- 📁 Auto-opens the download folder after completion
- 🏷️ Saves files with video ID + title for easy identification

---

## 🛠️ Requirements

- Python 3.7 or higher
- `yt-dlp` (auto-installed if missing)
- Internet connection

---

## 📦 Installation

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/tiktok-downloader.git
cd tiktok-downloader
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
python tiktok_downloader.py
```

You will be prompted to enter:

1. **TikTok Channel Link** — e.g., `https://www.tiktok.com/@username`
2. **Download folder** — default is `./tiktok_videos`

**Example input:**

```
📱 TikTok Channel Link:
> https://www.tiktok.com/@exampleuser

💾 Folder (default: ./tiktok_videos):
> [press Enter for default]
```

---

## 📁 Output Structure

```
tiktok_videos/
└── tiktok_20241215_143022/
    ├── 7123456789_video title 1.mp4
    ├── 7123456790_video title 2.mp4
    └── 7123456791_video title 3.mp4
```

Each run creates a new timestamped subfolder so previous downloads are never overwritten. Files are named with their **TikTok video ID** + title to avoid duplicates.

---

## 🔧 How It Works

1. Takes the TikTok channel/profile URL as input
2. Uses `yt-dlp` with `best` format to get highest available quality
3. Downloads up to 4 videos in parallel (`-N 4`)
4. Skips any unavailable/private videos and continues (`--ignore-errors`)
5. Saves files as `%(id)s_%(title)s.%(ext)s`
6. Counts and displays total `.mp4` files downloaded

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `yt-dlp` not found | Run `pip install -U yt-dlp` manually |
| Download fails / 0 videos | Update yt-dlp: `pip install -U yt-dlp` |
| Private/restricted videos | Only public videos can be downloaded |
| Folder won't auto-open | Open the folder path shown in the terminal manually |
| Rate limited by TikTok | Wait a few minutes and try again |

---

## ⚠️ Disclaimer

This tool is for **personal and educational use only**. Only download content you own or have explicit permission to download. The author is not responsible for any misuse. Respect TikTok's [Terms of Service](https://www.tiktok.com/legal/page/us/terms-of-service/en).

---

## 📄 License

This project is open for personal use. For redistribution, please credit the original author.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

Open an [Issue](https://github.com/your-username/tiktok-downloader/issues) for bugs or feature requests.
