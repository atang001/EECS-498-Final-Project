from hmmlearn import hmm
import os
import numpy as np
import pandas as pd
import python_speech_features as speech
from os import listdir
from os.path import isfile, join
from python_speech_features import mfcc
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from sklearn.metrics import confusion_matrix
from pydub import AudioSegment
from pydub.playback import play
from tqdm.notebook import tqdm

def getTrainSet(list_of_genres, dir = './genres/'):
    trainSet = []
    for genre in list_of_genres:
        songList = listdir(join(dir,genre))
        trainSet = trainSet + songList
    return(trainSet)
	