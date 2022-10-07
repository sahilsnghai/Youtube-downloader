import tkinter
from pytube import YouTube
from tkinter import *
from tkinter import filedialog, ttk
import wget

screen = Tk()
title = screen.title("YouTube Download")
canvas = Canvas(screen, width=600, height=500)
canvas.pack()


# Functions
def select_path():
    # to select path from the explore
    global path 
    path = filedialog.askdirectory()
    if path == None:
        path = r'C:\Users\sahil\Downloads'
    path_label.config(text=path)


def video(youtube):
    Videos = youtube.streams.filter(mime_type='video/mp4', progressive=True)
    qualitys = list()
    for video in Videos:
        pos = str(video).find('res=\"')
        first_quote = str(video).find('\"', pos)
        second_quote = str(video).find('\"', first_quote+1)
        qualitys.append(str(video)[first_quote+1:second_quote])
        # print(video)
    quality(qualitys)


def audio(youtube):
    Audios = youtube.streams.filter(only_audio=True, mime_type='audio/mp4')
    qualitys = list()
    for Audio in Audios:
        pos = str(Audio).find('abr=\"')
        first_quote = str(Audio).find('\"', pos)
        second_quote = str(Audio).find('\"', first_quote+1)
        qualitys.append(str(Audio)[first_quote+1:second_quote])
        # print(Audio)
    quality_label.config(
        text="Select the quality for the Audio: ", font=('Roboto', 12))
    quality(qualitys)


def quality(qualitys):
    qualitys.sort()
    qaulity_combobox = ttk.Combobox(screen, width=15,
                                    values=tuple(qualitys), textvariable=format_of_item, state='readonly')
    canvas.create_window(420, 400, window=qaulity_combobox)


def download_file():
    youtube = YouTube(link_field.get())
    print(format_of_item.get())
    link_label.config(
            text=f"Downloading Your Stuff. Please Wait!", fg='#5ec7f7')
    if choose.get().lower() == 'video':
        # print('videos')
        Videos = youtube.streams.filter(
            mime_type='video/mp4', progressive=True)
        Videos.filter(res=format_of_item.get()).first().download(
            output_path=path)
        
    elif choose.get().lower() == 'audio':
        # print('videos')
        Audios = youtube.streams.filter(only_audio=True, mime_type='audio/mp4')
        Audios.filter(abr=format_of_item.get()).first().download(
            output_path=path)

    elif choose.get().lower() == 'thumbnail':
        # print('thumbnail')
        url = youtube.thumbnail_url
        wget.download(url, r'C:\Users\sahil\Downloads')
    
    link_label.config(
            text=f"Downloading Completed", fg='#22d41c')


def done():
    choice = choose.get().lower()
    youtube = YouTube(link_field.get())
    if choice == 'video':
        video(youtube)
    elif choice == 'audio':
        audio(youtube)
    elif choice == 'thumbnail':
        pass
    else:
        link_label.config(text="Please Enter Link below!: ", fg='red')


# image logo
logo_img = PhotoImage(file='ytlogo.png')
canvas.create_image(300, 80, image=logo_img)

# link field
link_label = Label(screen, text=" Enter Youtube link: ", font=('Roboto', 12))
link_field = Entry(screen, width=70, text="Type or Past your link here")
link_field.place(width=150, height=50)

quality_label = Label(
    screen, text="Select the quality for the Video: ", font=('Roboto', 12))

# Select Saving file Location
path_label = Label(
    screen, text='Select Path for Download location', font=('Roboto', 12))
locate_btn = Button(screen, text='Locate', width=10,
                    height=2, command=select_path)
format_of_item = tkinter.StringVar()

# add widget to window
canvas.create_window(300, 170, window=link_label)
canvas.create_window(300, 200, window=link_field)

# Download Buttons
done_btn = Button(screen, width=15, text='Done', command=done)
download_btn = Button(screen, text="Download", width=20, height=2, font=(
    'summary notes', 12), command=download_file, bg='#2dcc47')

# Combobox with demo qualitys
combobox = ttk.Combobox(width=15, state='readonly')
combobox['values'] = ('1080p', '720p', '480p', '360p', '240p', '144p')

# choise by radiobutton
choose = tkinter.StringVar()
choice_radio1 = ttk.Radiobutton(
    screen, text="Video", value='Video', variable=choose)
choice_radio2 = ttk.Radiobutton(
    screen, text="Audio", value='Audio', variable=choose)
choice_radio3 = ttk.Radiobutton(
    screen, text="Thumbnail", value='Thumbnail', variable=choose)

# Add to window
canvas.create_window(300, 270, window=done_btn)
canvas.create_window(420, 400, window=combobox)
canvas.create_window(300, 310, window=path_label)
canvas.create_window(300, 350, window=locate_btn)
canvas.create_window(300, 450, window=download_btn)
canvas.create_window(130, 230, window=choice_radio1)
canvas.create_window(300, 230, window=choice_radio2)
canvas.create_window(460, 230, window=choice_radio3)
canvas.create_window(250, 400, window=quality_label)


screen.mainloop()