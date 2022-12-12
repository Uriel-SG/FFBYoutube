import tkinter as tk
import tkinter.messagebox
import os
import webbrowser
import pytube
import customtkinter as ct

# Output dir
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
desktop_dir = os.listdir(desktop)
if "FFBYoutube" not in desktop_dir:
    desk_path = desktop + "\FFBYoutube"
    os.mkdir(desk_path)
else:
    desk_path = desktop + "\FFBYoutube"


finestra = tk.Tk()
finestra.title("FFByoutube")
finestra.geometry("600x690")
finestra.configure(bg="light blue")
finestra.iconbitmap("download.ico")
logo = tk.PhotoImage(file="ffbyou.png")
smallerlogo = logo.subsample(2, 2)
ffbyou = tk.Label(image=smallerlogo, bg='white')
ffbyou.pack(fill=tk.X)
frame1 = tk.Frame(finestra, bg="light blue")
frame1.pack()
frame2 = tk.Frame(finestra, bg="light blue")
frame2.pack()


def download_video():
    link = entry.get()
    try:
        yt = pytube.YouTube(link)
        display_info(yt)
        yt.streams.get_highest_resolution().download(desk_path)
        tkinter.messagebox.showinfo(title="Success!", message="Video succesfully downloaded!")
        entry.delete("0", tk.END)
        informations.delete("1.0", tk.END)
        informations["state"] = "disabled"
        webbrowser.open(desk_path)
    except:
        tkinter.messagebox.showerror(title="Error", message="An error occured with the download")


#download audio only
def download_audio():
    link = entry.get()
    try:
        yt = pytube.YouTube(link)
        display_info(yt)
        yt.streams.filter(abr="160kbps", progressive=False).first().download(desk_path)
        tkinter.messagebox.showinfo(title="Success!", message="Mp3 succesfully downloaded!")
        entry.delete("0", tk.END)
        informations.delete("1.0", tk.END)
        informations["state"] = "disabled"
        webbrowser.open(desk_path)
    except:
        tkinter.messagebox.showerror(title="Error", message="An error occured with the download")

def exit_program():
    finestra.destroy()

# Link label and text
link_label = tk.Label(frame1, text="Paste your link here: ", bg="light blue", height=5)
link_label.pack()

entry = ct.CTkEntry(master=frame1, placeholder_text="Your Link", width=350)
entry.pack(padx=20, pady=10)

empty = tk.Label(frame1, bg="light blue")
empty.pack()

button = tk.Button(master=frame1, text="Download Video", command=download_video)
button.pack(padx=20, pady=10, side=tk.LEFT)

button = tk.Button(master=frame1, text="Download mp3", command=download_audio)
button.pack(padx=20, pady=10, side=tk.RIGHT)

info = tk.Label(frame2, bg="light blue", text="Video informations")
info.pack()
informations = tk.Text(frame2, width=50, height=18, padx=15, pady=15, state="disabled")
informations.tag_configure("center", justify='center')
informations.pack()
exit_butt = tk.Button(frame2, text="Exit", width=9, command=exit_program)
exit_butt.pack(padx=20, pady=20)

powered = tk.Label(frame2, text="Powered by Salvatore Garasto", font=("Arial", 7))
powered.pack(side="bottom")

def display_info(yt):
    informations["state"] = "normal"
    informations.insert(tk.END, f"\nTitle:\n{yt.title}")
    informations.insert(tk.END, f"\n\nAuthor:\n{yt.author}")
    informations.insert(tk.END, f"\n\nPublished date:\n{yt.publish_date.strftime('%Y-%m-%d')}")
    informations.insert(tk.END, f"\n\nViews:\n{yt.views}")
    informations.insert(tk.END, f"\n\nLength of video:\n{yt.length} seconds")
    informations.tag_add("center", "1.0", "end")
    


finestra.mainloop()



