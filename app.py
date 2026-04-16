import gradio as gr
import pandas as pd
import time
import matplotlib.pyplot as plt









titles = []                                                    #Global lists to be used in multiple functions (easier to access and more readable code than constantly passing and returning)
energies = []
durations = []
def parse_songs(user):
    if not user:                                                #Checks right away if the input is false
        return ["WrongInput"]
    lines = user.strip().split("\n")                            #Removes extra spaces and splits by lines of input
    playlist = []                                               #New list of dictionaries
    for line in lines:
        parts = line.split(",")                                 #Split lines into its four different parts
        if len(parts) != 4:
            return ["WrongInput"]                               #Input must include 4 parts, otherwise there is an issue
        title = parts[0].strip()
        titles.append(title)
        artist = parts[1].strip()                               #titles, energy and duration are only used internally, but artist is only needed externally
        energy = int(parts[2].strip())
        energies.append(energy)
        duration = int(parts[3].strip())
        durations.append(duration)
        playlist.append({
            "title": title,                                     #every piece is attached to a corresponding key in the dictionary for easy calling/indexing
            "artist": artist,
            "Energy": energy,
            "Duration": duration
        })
    return playlist

def plot(key):                                                  #Creates first dataframe for the initial plot
    if key=="Energy":
        sorting=energies
    else:
        sorting=durations
    df = pd.DataFrame({"Song":titles, "Type":sorting})
    return df

def merge_sort(playlist,key,snapshots):                              #Key is sorting key, and snapshots is a list of dataframes to remember the sublists of the sorting process
    if len(playlist) <= 1:                                      #Base case for the code
        return playlist
    else:
        mid = len(playlist) // 2
        merged=merge(merge_sort(playlist[:mid],key,snapshots), merge_sort(playlist[mid:],key,snapshots),key)    #Merging the two lists together and creating a call stack and saving the values throughout to merged
        snapshots.append([pd.DataFrame({"Song": [x["title"] for x in merged],"Type": [y[key] for y in merged]}),merged]) #creating a dataframe for plotting by running through the titles and keys currently involved in the sorted sublist. Also records the merged value as is
        return merged
def merge(left, right,key):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):             #sorting merging sublists
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):                                 #Adding any extra from the left
        result.append(left[i])
        i += 1
    while j < len(right):                               #Adding any extra from the right
        result.append(right[j])
        j += 1
    return result


def df_readable(snapshot):                              #turning the snapshot df into a readable list of names to be output
    current_titles=""
    for x in snapshot[-1]:                              #Snapshot runs through the non-dataframe part of this snapshot
        current_titles+=x["title"]+"\n"
    return current_titles

def clean_input(playlist):
    songs=[]
    newsong=""
    for song in playlist:
        songs.append(song["title"]+","+song["artist"]+","+str(song["Energy"])+","+str(song["Duration"]))        #turns all values into strings and puts commas in between
        newsong+=str(songs)
        if song!=playlist[-1]:                                                                                  #Only the last song should not have a line break
            newsong+="\n"
        songs.clear()
    return newsong.strip().replace("'","").replace("[","").replace("]","")  #removes excess spaces and replaces weird characters


def make_plot(df, key):
   figure,ax=plt.subplots(figsize=(10,5))                                       #Creates the plot and sets the figure size to fit a wide-screen layout
   ax.bar(df["Song"],df["Type"])

   ax.set_xlabel("Song")
   ax.set_ylabel(key)

   return figure



def run(user, key):
    playlist=parse_songs(user)
    if playlist==["WrongInput"]:
        yield(
            gr.Plot(x="Song", y="Type", kind='bar'), "Incorrect Input. Please try again."           #returns an empty chart and prompts to try again
        )
        return
    df = plot(key)                                                                                  #First initial dataframe for plotting
    yield (
        make_plot(df,key), "Initial List"
    )
    time.sleep(1.0)
    snaps=[]
    sorted_list = merge_sort(playlist, key, snaps)
    for snapshot in snaps:
        yield (
            make_plot(snapshot[0],key), "Sorting...\n"+df_readable(snapshot)            #runs through all of the snapshots taken and prints plots for each one with some delay
        )
        time.sleep (2.0)
    if len(snaps)>=1:                                                                   #Prevents Index error
        yield(
            make_plot(snaps[-1][0],key), "Sorted list: \n"+clean_input(sorted_list)
        )
    else:
        yield(
            make_plot(df,key), "Sorted list: \n "+clean_input(sorted_list)              #Just need to print the original bar
        )
    titles.clear()
    energies.clear()
    durations.clear()

with gr.Blocks() as demo:
    gr.Markdown("# Playlist Sorter")
    name = gr.Textbox(                                                                  #Creates a textbox with basic length and starter text to show how to do everything
        label="Enter songs",
        lines=8,
        placeholder="Title, Artist, Energy, Duration"
    )
    sort_key = gr.Dropdown(                                                             #Creates a dropdown menu to choose the sort-key
        choices=["Energy", "Duration"],
        label="Choose sorting key"
    )

    output_box = gr.Textbox(label="Sorted Playlist")                                    #Outputs basic textbox and plot
    sort_button = gr.Button("Sort")
    myplot=gr.Plot(label="Visualization")

    sort_button.click(fn=run, inputs=[name, sort_key], outputs=[myplot, output_box], api_name="Sorted Playlist")    #runs the run function to do the rest



demo.launch()
