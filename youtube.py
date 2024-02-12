import streamlit as st
from pytube import YouTube

def download_youtube_video(url, output_path='downloads'):
    try:
        st.info("Downloading... Please wait.")
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        stream.download(output_path)
        st.success(f"Video downloaded successfully at {output_path}/{yt.title}.mp4")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    # Get YouTube video URL from the user
    video_url = st.text_input("Enter YouTube video URL:")

    # Set a default download directory
    download_directory = st.text_input("Enter download directory (default is 'downloads'):", "downloads")

    # Download button
    if st.button("Download"):
        if video_url:
            download_youtube_video(video_url, download_directory)
        else:
            st.warning("Please enter a valid YouTube video URL.")

if __name__ == "__main__":
    main()
