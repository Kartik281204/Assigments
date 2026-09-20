import os
import random
import time
from pytube import YouTube  # type:ignore
import tkinter as tk
from tkinter import filedialog


def download(url, savepath):
    try:
        yt = YouTube(url)
        stream = yt.streams(url)
    except Exception as e:
        print(e)
