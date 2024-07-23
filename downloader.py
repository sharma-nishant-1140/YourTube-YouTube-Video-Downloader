from pytube import YouTube

def downloader(input_url, download_format):
    link = YouTube(input_url)
    if len(download_format) == 1:
        if(download_format[0] == '1'):
            res = link.streams.get_highest_resolution()
            res.download()
        if(download_format[0] == '2'):
            res = link.streams.filter(only_audio=True).first()
            res.download()
    if len(download_format) == 2:
        res = link.streams.get_highest_resolution()
        res.download()
        res = link.streams.filter(only_audio=True).first()
        res.download()
    return "Completed"
