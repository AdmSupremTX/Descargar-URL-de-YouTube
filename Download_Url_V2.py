from pytube import YouTube
import os

def download_youtube_video(url, download_format):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Define the path to the Downloads directory and create a subdirectory
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads", "YouTubeDownloads")
        if not os.path.exists(downloads_dir):
            os.makedirs(downloads_dir)
        
        if download_format == 'mp4':
            # Get the highest resolution stream available
            stream = yt.streams.get_highest_resolution()
        elif download_format == 'mp3':
            # Get the audio stream only
            stream = yt.streams.filter(only_audio=True).first()
        
        # Download the video/audio
        out_file = stream.download(downloads_dir)
        
        if download_format == 'mp3':
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"Audio '{yt.title}' 𝐒𝐞 𝐡𝐚 𝐝𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐝𝐨 𝐲 𝐜𝐨𝐧𝐯𝐞𝐫𝐭𝐢𝐝𝐨 𝐚 𝐌𝐏𝟑 𝐜𝐨𝐧 é𝐱𝐢𝐭𝐨")
        else:
            print(f"Video '{yt.title}' 𝐒𝐞 𝐡𝐚 𝐝𝐞𝐬𝐜𝐚𝐫𝐠𝐚𝐝𝐨 𝐞𝐱𝐢𝐭𝐨𝐬𝐚𝐦𝐞𝐧𝐭𝐞")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input YouTube video URL
    print("██╗░░░██╗████████╗░░░░░░░██████╗░█████╗░██████╗░██╗██████╗░████████╗")
    print("╚██╗░██╔╝╚══██╔══╝░░░░░░██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝")
    print("░╚████╔╝░░░░██║░░░█████╗╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░")
    print("░░╚██╔╝░░░░░██║░░░╚════╝░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░")
    print("░░░██║░░░░░░██║░░░░░░░░░██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░")
    print("░░░╚═╝░░░░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░")
    print()
    print()

    print("——————————✧◦♚◦✧————————————⋆")
    video_url = input("𝐈𝐧𝐠𝐫𝐞𝐬𝐚 𝐭𝐮 𝐔𝐑𝐋 𝐩𝐚𝐫𝐚 𝐜𝐨𝐦𝐞𝐧𝐳𝐚𝐫 ➪")
    print("——————————✧◦♚◦✧————————————⋆")
    
    # Input download format
    download_format = input("𝐄𝐥𝐢𝐠𝐞 𝐞𝐥 𝐟𝐨𝐫𝐦𝐚𝐭𝐨 𝐪𝐮𝐞 𝐝𝐞𝐬𝐞𝐚𝐬 ➾ (mp4/mp3) ").strip().lower()
    
    if download_format not in ['mp4', 'mp3']:
        print("𝐅𝐨𝐫𝐦𝐚𝐭𝐨 𝐢𝐧𝐯𝐚𝐥𝐢𝐝𝐨, 𝐞𝐥𝐢𝐠𝐞 𝐚𝐥𝐠𝐮𝐧𝐨 ➾ 'mp4' o 'mp3'.")
    else:
        # Download the video
        download_youtube_video(video_url, download_format)
