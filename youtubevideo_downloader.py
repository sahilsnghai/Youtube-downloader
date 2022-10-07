from pytube import YouTube

link = input("Link: ")
youtube = YouTube(link)

choice = input("Audio/Video: ")
if choice.lower() =='Video'.lower():
    Videos = youtube.streams.filter(mime_type='video/mp4')
    for video in Videos:
        pos = str(video).find('res=\"')
        first_quote = str(video).find('\"',pos)
        second_quote = str(video).find('\"',first_quote+1)
        qualitys = str(video)[first_quote+1:second_quote]
        print('quality: ',qualitys)
        print(video)
        # print(str(video))
    res = input("Quality: ")
    Videos.filter(res=res).first().download()# r'C:\Users\sahil'
    print("Successfully Downloaded")
elif choice.lower() == 'Audio'.lower():
    Audios = youtube.streams.filter(only_audio=True,mime_type='audio/mp4')
    for audio in Audios:
        pos = str(audio).find('abr=\"')
        first_quote = str(audio).find('\"',pos)
        second_quote = str(audio).find('\"',first_quote+1)
        qualitys = str(audio)[first_quote+1:second_quote]
        print('quality: ',qualitys)
        print(audio)
        # print(str(audio))
    abr = input("Quality: ")
    aa= Audios.filter(abr=abr).first().download()
    # print(aa)
    print("Successfully Downloaded")

# quality = input("Choose Quality: ")
