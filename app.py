import gradio as gr

b=True

def run(user,key):
    playlist=parse_songs(user)
    return fix_input(merge_sort(playlist,key))


def merge_sort(playlist,key):

    if len(playlist) <= 1:
        return playlist
    else:
        mid = len(playlist) // 2
        return merge(merge_sort(playlist[:mid],key), merge_sort(playlist[mid:],key),key)

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

def parse_songs(user):
    playlist = []
    lines = user.strip().split("\n")

    for line in lines:
        parts = line.split(",")
        if len(parts) != 4:
            raise ValueError("Each line must have 4 values: title, artist, energy, duration")
        title = parts[0].strip()
        artist = parts[1].strip()
        energy = int(parts[2].strip())
        duration = int(parts[3].strip())
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
with gr.Blocks() as demo:
    gr.Markdown("# Playlist Sorter")
    name = gr.Textbox(
        label="Enter songs",
        lines=8,
        placeholder="Title, Artist, Energy, Duration"
    )
    sort_key = gr.Dropdown(
        choices=["energy", "duration"],
        label="Choose sorting key"
    )

    output_box = gr.Textbox(label="Sorted Playlist")
    sort_button = gr.Button("Sort")
    sort_button.click(fn=run, inputs=[name, sort_key], outputs=output_box, api_name="Sorted Playlist")


demo.launch()
"""def run_sort_demo(user_input):
    if not user_input.strip():
        return "Please enter some values."

    values = [x.strip() for x in user_input.split(",")]
    values=int(values)
    return merge_sort(values)


def merge_sort(playlist):
    if len(playlist) <= 1:
        return playlist
    else:
        mid = len(playlist) // 2
        return merge(merge_sort(playlist[:mid]), merge_sort(playlist[mid:]))

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

song_input = gr.Textbox(
    label="Enter songs",
    lines=8,
    placeholder="Title, Artist, Energy, Duration"
)


def format_songs(songs):
    result = ""
    for song in songs:
        result += f"{song['title']} - {song['artist']} | Energy: {song['energy']} | Duration: {song['duration']}\n"
    return result


demo = gr.Blocks(
    fn=run_sort_demo,
    inputs=gr.Textbox(label="Enter values separated by commas"),
    outputs=gr.Textbox(label="Output"),
    title="Sorting Project Demo",
    description="This is my starter Gradio app for my sorting project."
)

if __name__ == "__main__":
    demo.launch()"""






