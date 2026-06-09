#!/usr/bin/env python3
"""
TikTok Channel Downloader - Fixed Version
"""

import os
import sys
import subprocess
from datetime import datetime

def check_yt_dlp_installed():
    try:
        subprocess.run([sys.executable, '-m', 'yt_dlp', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def install_yt_dlp():
    print("📦 Installing yt-dlp...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp'], check=True)
        print("✅ Installed!")
        return True
    except:
        print("❌ Failed")
        return False

def download_tiktok(channel_url, output_folder="./tiktok_videos"):
    
    if not check_yt_dlp_installed():
        if not install_yt_dlp():
            return False
    
    os.makedirs(output_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_folder = os.path.join(output_folder, f"tiktok_{timestamp}")
    os.makedirs(final_folder, exist_ok=True)
    
    print(f"\n🎬 TikTok Download...")
    print(f"📍 Channel: {channel_url}")
    print(f"💾 Folder: {final_folder}")
    print("-" * 50)
    
    command = [
        sys.executable,
        '-m', 'yt_dlp',
        channel_url,
        '-o', os.path.join(final_folder, '%(id)s_%(title)s.%(ext)s'),  # ✅ ID added
        '--format', 'best',
        '-N', '4',
        '--ignore-errors',   # ✅ ek fail ho to baki chalti rahein
        '--no-warnings',
    ]
    
    try:
        print("\n⏳ Downloading...\n")
        subprocess.run(command, check=True)
        
        # Count downloaded files
        files = [f for f in os.listdir(final_folder) if f.endswith('.mp4')]
        
        print("\n" + "=" * 50)
        print(f"✅ Done! {len(files)} videos downloaded")
        print(f"📂 Location: {final_folder}")
        print("=" * 50)
        
        try:
            if sys.platform == 'win32':
                os.startfile(final_folder)
            elif sys.platform == 'darwin':
                subprocess.run(['open', final_folder])
            else:
                subprocess.run(['xdg-open', final_folder])
        except:
            pass
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Cancelled")
        return False

def main():
    print("""
╔═════════════════════════════════════╗
║  TikTok Downloader (Fixed)          ║
║  Just Link → Download               ║
╚═════════════════════════════════════╝
    """)
    
    channel_url = input("\n📱 TikTok Channel Link:\n> ").strip()
    if not channel_url:
        print("❌ Link required!")
        return
    
    output_folder = input("\n💾 Folder (default: ./tiktok_videos):\n> ").strip()
    if not output_folder:
        output_folder = "./tiktok_videos"
    
    print(f"\n{'='*50}")
    print(f"Channel: {channel_url}")
    print(f"Folder: {output_folder}")
    print(f"{'='*50}")
    
    confirm = input("\nStart? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancelled")
        return
    
    download_tiktok(channel_url, output_folder)

if __name__ == "__main__":
    main()