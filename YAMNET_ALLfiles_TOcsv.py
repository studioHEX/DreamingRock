import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv

import matplotlib.pyplot as plt
from IPython.display import Audio
from scipy.io import wavfile
import scipy
import os

from google.colab import drive
drive.mount('/content/drive')

# Load the model.
model = hub.load('https://tfhub.dev/google/yamnet/1')

#directory = 'C:/Users/Admin/Documents/dreamTime'
directory = '/content/drive/MyDrive/audioset'

#Change into directory where files are located
os.chdir(directory)


# Find the name of the class with the top score when mean-aggregated across frames.
def class_names_from_csv(class_map_csv_text):
  """Returns list of class names corresponding to score vector."""
  class_names = []
  with tf.io.gfile.GFile(class_map_csv_text) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      class_names.append(row['display_name'])

  return class_names

class_map_path = model.class_map_path().numpy()
class_names = class_names_from_csv(class_map_path)

def ensure_sample_rate(original_sample_rate, waveform,
                       desired_sample_rate=16000):
  """Resample waveform if required."""
  if original_sample_rate != desired_sample_rate:
    desired_length = int(round(float(len(waveform)) /
                               original_sample_rate * desired_sample_rate))
    waveform = scipy.signal.resample(waveform, desired_length)
  return desired_sample_rate, waveform


#opening a csv file in writer mode to export the data into an understandable format for RNN

with open('/content/drive/MyDrive/audio_event.csv', 'w', newline='') as file:
    writer = csv.writer(file)


    #cycling through all the files in a folder, extract name from file, split at '-' and write into svg row appending the inferred_class.

    for filename in os.listdir(directory):
        file_name = os.path.basename(filename)
        date_time = file_name.split('_')
        date = date_time[0]
        time = date_time[1][:-4]
        wav_file_name = file_name
        sample_rate, wav_data = wavfile.read(wav_file_name, 'rb')
        sample_rate, wav_data = ensure_sample_rate(sample_rate, wav_data)

        # Show some basic information about the audio.
        duration = len(wav_data)/sample_rate
        #print(f'Sample rate: {sample_rate} Hz')
        #print(f'Total duration: {duration:.2f}s')
        #print(f'Size of the input: {len(wav_data)}')

        # Listening to the wav file.
        Audio(wav_data, rate=sample_rate)

        waveform = wav_data / tf.int16.max

        # Run the model, check the output.
        scores, embeddings, spectrogram = model(waveform)

        #print(scores)

        scores_np = scores.numpy()
        spectrogram_np = spectrogram.numpy()
        infered_class = class_names[scores_np.mean(axis=0).argmax()]
        #print(f'The main sound is: {infered_class}')

        print(date, end=' ')
        print(time, end=' ')
        print(f'{infered_class}'
)        print_statement = date, time, f'{infered_class}'
        writer.writerow(print_statement)
        print('added a row to the csv-file, yo.')

