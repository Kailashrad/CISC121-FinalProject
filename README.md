---
title: Kailash Sorting Demonstration
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---


# Playlist Vibe Builder with Merge Sort

## Demo video/gif/screenshot of test
<img width="1227" height="810" alt="image" src="https://github.com/user-attachments/assets/16317f79-5833-45ce-9bb5-286079c81ba7" />

Screenshots of first test steps:
<img width="1233" height="327" alt="image" src="https://github.com/user-attachments/assets/84d9da71-1149-4509-b098-4b2a972f458d" />

<img width="1234" height="327" alt="image" src="https://github.com/user-attachments/assets/62b9e04c-5b1a-42c3-a981-6a9cfe214b99" />

<img width="1238" height="332" alt="image" src="https://github.com/user-attachments/assets/9ce5ea82-3509-4d6b-bb67-51bbc5beb8a8" />

<img width="1236" height="324" alt="image" src="https://github.com/user-attachments/assets/bae05acc-7cac-4fff-9281-35d86b441f4d" />

<img width="1234" height="332" alt="image" src="https://github.com/user-attachments/assets/827a4b5e-d544-4b6a-9ec7-5c5b0cc26993" />

<img width="1234" height="332" alt="image" src="https://github.com/user-attachments/assets/71078d82-fb02-44a2-ad47-2c77f35735e0" />

<img width="1236" height="333" alt="image" src="https://github.com/user-attachments/assets/fbe7d336-70d1-44aa-8f7e-4a7d46ce8ff5" />

<img width="1233" height="328" alt="image" src="https://github.com/user-attachments/assets/ebde7639-7734-4b8d-a1bd-aa15588dd336" />

<img width="1238" height="332" alt="image" src="https://github.com/user-attachments/assets/cabe6096-ce8c-4494-9f39-e91fe1ae4802" />

<img width="1232" height="323" alt="image" src="https://github.com/user-attachments/assets/6b02ffb4-dbb2-4b7c-9166-8e2ace4b051e" />



Test 2: Another regular input
<img width="1242" height="722" alt="image" src="https://github.com/user-attachments/assets/b613db9a-114e-4417-9ee8-561e4a20baec" />

Performed as expected

Test 3: Already sorted
<img width="1232" height="705" alt="image" src="https://github.com/user-attachments/assets/b6158070-085e-4cf4-8e13-33a4e08f5db8" />

Performed as expected

Test 4: Reverse Sorted
<img width="1240" height="706" alt="image" src="https://github.com/user-attachments/assets/271ed825-96bc-4153-a29d-7868009881bd" />

Performed as expected

Test 5: No input, just button
No image unfortunately

Ran an error because it was not prepared for there not to be input. This led to adding the extra protective mechanism in parse_songs

Test 6: Single song
<img width="1235" height="666" alt="image" src="https://github.com/user-attachments/assets/df7a710b-96b9-475e-97ac-5772e7785449" />

Remembered all of the old songs in the plot. Led to changing the global lists to reset at the end of run



## Problem Breakdown & Computational Thinking

Why I chose this algorithm for the problem: Merge sort is stable and is much easier for viewers to understand in visualizations. The preconditions are that the songs must be input as: Title, Author, Energy, Duration. If it is not in this order, it will not work. This will be validated by making sure that energy is an integer and the duration is a float.

(You can add a flowchart and write the four pillars of computational thinking briefly in bullets)
Decomposition:
-Take in a list of songs with the title, artist, energy score (from 0-100), and duration
-Allow the used to decide if sorting by energy or duration
-sort the list by the chosen method and show steps
    -break the list into smaller and smaller halves recursively
    -once a list of one is obtained, compare individual lists
    -go back up the call stack by comparing and switching parts of list until the list is sorted
-Display the final sorted list


Pattern Recognition:
-The best method is to use merge sort for this problem
-The pattern in inputs is that the sorting will be the same method whether energy or duration is being used

Abstraction:
Focus on:
    -whichever of duration or energy is chosen by the user
Ignore:
    -The title, author and duration or energy

Algorithmic Thinking:
<img width="1321" height="532" alt="image" src="https://github.com/user-attachments/assets/eb95f9cc-b98d-49d0-b9ab-35dc09ca0ea7" />

<img width="1858" height="759" alt="image" src="https://github.com/user-attachments/assets/0aca86d4-5ca6-469f-b9bb-dc232d64f320" />

<img width="932" height="750" alt="image" src="https://github.com/user-attachments/assets/811afbf2-7810-49c0-b4b8-f9ef57b4fbab" />


## Steps to Run
1. Read in user input and allow user to select from the two options for sorting (energy, and Duration) through a dropdown.
2. Parse the input into a list of dictionaries and if there are any issues in the input, output "Incorrect Input. Please try again."
3. Display a graph of the initial data (converted into a dataframe using an external function) and pause for a second before continuing
4. Merge sort the list:
       a) break the list down into half lists recursively until the base case of 1 is reached
       b) once the base case is reached, sort the lists of one, then the lists of two, all the way back up the stack
       c) before returning the next call, record the current songs being sorted and their value for the current "key" (sorting key) in this sublist as a snapshot dataframe
5. Loop through the list of snapshots (dataframes):
       a) display the dataframe of the snapshot with a plot (created in another function), and the current sublist (in the output box), which has the information decoded in a separate function
       b) pause on the plot for 2.0s
6.  Display the final snapshot in a plot and print the final sorted list (again decoded from the list of dictionaries to regular english with a separate function)


## Hugging Face Link
https://kailashrad-kailash-sorting-demonstration.hf.space



## Author & AI Acknowledgment
Kailash Radhakrishnan
AI Acknowledgement/Disclosure: Level 4 AI was used throughout the process of creating this assignment. ChatGPT was used along with the gradio webpage to inspire ideas, help build test-cases, troubleshoot, and steps for the deployment of the app. ChatGPT in particular was used for helping to understand how to make my vision for the assignment come to life through gradio, but no code was AI generated.
