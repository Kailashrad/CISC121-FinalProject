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



## Steps to Run

## Hugging Face Link
https://kailashrad-kailash-sorting-demonstration.hf.space



## Author & AI Acknowledgment
