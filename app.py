import gradio as gr
import pandas as pd
import time
import matplotlib.pyplot as plt




def merge(left, right,key):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result




titles = []
energies = []
durations = []
def parse_songs(user):
    if not user:
        return ["WrongInput"]
    lines = user.strip().split("\n")
    playlist = []
    for line in lines:
        parts = line.split(",")
        if len(parts) != 4:
            return ["WrongInput"]
        title = parts[0].strip()
        titles.append(title)
        artist = parts[1].strip()
        energy = int(parts[2].strip())
        energies.append(energy)
        duration = int(parts[3].strip())
        durations.append(duration)
        playlist.append({
            "title": title,
            "artist": artist,
            "energy": energy,
            "duration": duration
        })
    return playlist
def fix_input(playlist):
    songs=[]
    newsong=""
    for song in playlist:
        songs.append(song["title"]+","+song["artist"]+","+str(song["energy"])+","+str(song["duration"]))
        newsong+=str(songs)
        if song!=playlist[-1]:
            newsong+="\n"
        songs.clear()
    return newsong.strip().replace("'","").replace("[","").replace("]","")

def plot(key):
    if key=="energy":
        sorting=energies
    else:
        sorting=durations
    df = pd.DataFrame({"Song":titles, "Type":sorting})

    return df

def merge_sort(playlist,key,snap):
    if len(playlist) <= 1:
        return playlist
    else:
        mid = len(playlist) // 2
        merged=merge(merge_sort(playlist[:mid],key,snap), merge_sort(playlist[mid:],key,snap),key)
        snap.append([pd.DataFrame({"Song": [x["title"] for x in merged],"Type": [y[key] for y in merged]}),merged])
        return merged

def dfuntangled(snapshot):
    mstring=""
    for x in snapshot[-1]:
        mstring+=x["title"]+"\n"
    return mstring


def make_plot(df, key):
   figure,ax=plt.subplots(figsize=(10,5))
   ax.bar(df["Song"],df["Type"])

   ax.set_xlabel("Song")
   ax.set_ylabel(key)

   return figure



def run(user, key):
    playlist=parse_songs(user)
    if playlist==["WrongInput"]:
        yield(
            gr.Plot(x="Song", y="Type", kind='bar'), "Incorrect Input. Please try again."
        )
        return
    df = plot(key)
    yield (
        make_plot(df,key), "First List"
    )
    time.sleep(1.0)
    snaps=[]
    final = merge_sort(playlist, key, snaps)
    for snapshot in snaps:
        yield (
            make_plot(snapshot[0],key), "Sorting...\n"+dfuntangled(snapshot)
        )
        time.sleep (2.0)
    if len(snaps)>=1:
        yield(
            make_plot(snaps[-1][0],key), "Sorted list: \n"+fix_input(final)
        )
    else:
        yield(
            make_plot(df,key), "Sorted list: \n "+fix_input(final)
        )

with gr.Blocks() as demo:
    gr.Markdown("# Playlist Sorter")
    name = gr.Textbox(
        label="Enter songs",
        lines=8,
        placeholder="Title, Artist, Energy, Duration"
    )
    sort_key = gr.Dropdown(
        choices=["Energy", "Duration"],
        label="Choose sorting key"
    )

    output_box = gr.Textbox(label="Sorted Playlist")
    sort_button = gr.Button("Sort")
    myplot=gr.Plot(label="Visualization")

    sort_button.click(fn=run, inputs=[name, sort_key], outputs=[myplot, output_box], api_name="Sorted Playlist")



demo.launch()