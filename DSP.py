import IPython.display as ipd
import librosa as lr
import librosa.display
import matplotlib.pyplot as plt

def audio_vis(audio_path):
    x, sr = lr.load(audio_path) # sr <- sample rate
    librosa.load(audio_path, sr=44100) # set sample rate
    ipd.Audio(audio_path)
    X = librosa.stft(x) # Short Time Fourier Transform
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14,5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.figure(figsize = (14,5))
    librosa.display.waveplot(x, sr = sr)
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    audio_path = '/Users/liuyu/Desktop/weather.wav'
    audio_vis(audio_path)

