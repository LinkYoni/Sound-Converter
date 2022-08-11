import os
from pathlib import Path
from pydub import AudioSegment

from tkinter import Tk, ttk, Label, OptionMenu, StringVar
from tkinter import filedialog as fd
from tkinter import messagebox

if not os.path.isdir('Results'):
    os.mkdir('Results')

class App(Tk):
    def __init__(self):
        super().__init__()
        self.filename = 'No file selected'
        self.text = None
        self.name = None
        self.button2 = None

        self.text = Label()
        self.text['text'] = self.filename
        self.text.grid(row = 0, column = 0, pady = 5)

        options = [
            ".ogg to .mp3",
            ".wav to .mp3",
            ".mp3 to .ogg",
            ".mp3 to .wav"
        ]
        self.name = StringVar(self)
        self.name.set('Choose a format')
        choose = OptionMenu(self, self.name, *options)
        choose.grid(row = 3, column = 0, pady = 0, sticky = 'E')

        button1 = ttk.Button(self, text='Select file', command=self.select_files)
        button1.grid(row = 1, column = 0, pady = 10, padx = 210)

        self.button2 = ttk.Button(self, text='Start conversion')
        self.button2['command'] = self.error
        self.button2.grid(row = 2, column = 0, pady = 7)

    def select_files(self):
        if self.name.get() != 'Choose a format':
            if self.name.get() == '.ogg to .mp3': self.filename = fd.askopenfilename(title='Select a file', filetypes=[('Video', '*.ogg')])
            elif self.name.get() == '.wav to .mp3': self.filename = fd.askopenfilename(title='Select a file', filetypes=[('Video', '*.wav')])
            elif self.name.get() == '.mp3 to .ogg': self.filename = fd.askopenfilename(title='Select a file', filetypes=[('Video', '*.mp3')])
            elif self.name.get() == '.mp3 to .wav': self.filename = fd.askopenfilename(title='Select a file', filetypes=[('Video', '*.mp3')])
            self.text['text'] = self.filename
            if self.filename == '':
                self.button2['command'] = self.error
                self.filename = 'No file selected'
                self.text['text'] = self.filename
        else: messagebox.showerror('Error', 'You have to select an option to transform a file before search it')

    def start(self):
        if self.name.get() != 'Choose a format':
            AudioSegment.converter = r"ffmpeg.exe"
            AudioSegment.ffprobe = r"ffprobe.exe"

            _filename = os.path.basename(self.filename)
            _filename = _filename.split('.')[0]
            song = Path(self.filename)

            if self.name.get() == '.ogg to .mp3':
                song = AudioSegment.from_ogg(song)
                song.export(f"Results/{_filename}.mp3", format="mp3")
            elif self.name.get() == '.wav to .mp3':
                song = AudioSegment.from_wav(song)
                song.export(f"Results/{_filename}.mp3", format="mp3")
            elif self.name.get() == '.mp3 to .ogg':
                song = AudioSegment.from_mp3(song)
                song.export(f"Results/{_filename}.ogg", format="ogg")
            elif self.name.get() == '.mp3 to .wav':
                song = AudioSegment.from_mp3(song)
                song.export(f"Results/{_filename}.wav", format="wav")

            messagebox.showinfo('Finished', 'File exported successfully')
        else: messagebox.showerror('Error', 'You have to select an option to transform a file')

    def error(self):
        if self.filename == 'No file selected':
            messagebox.showerror('Error', 'You have to upload a file to transform it')
        else:
            self.button2['command'] = self.start
            self.start()

root = App()
root.title('Sound converter | Coded by $ Yøni 🚬#0005')
root.resizable(False, False)
root.geometry('500x150')

root.mainloop()