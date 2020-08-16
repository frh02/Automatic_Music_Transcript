## Setup and Necessary Downloads
* <code>!pip install librosa</code>
* <code>!pip install noisereduce</code>
* <code>!pip install IPython</code>
* <code>!pip install MIDIUtil</code>
* <code>!pip install --upgrade music21</code>
*  Install **Musescore** from <code>https://musescore.org/en</code> for your operating system.

## Steps 

* After installing the necessary libraries and software, open the <code>Music_automatic_transcription.ipynb</code> file in collab.</br>
* The file <code>mp3_wav_conversion.py</code> is used to convert the **mp3** file into **.wav** file.</br>
* **audio_files** file contains the demo used for this project but we can use our own audio file.</br>
* To load the audio file saved in **audio_files**, we need to upload both the test files into google drive.</br>
* Now we need to mount the google drive into our colab file using <code>from google.colab import drive</code> and <code>drive.mount(‘/content/gdrive’)</code>.</br>
* Wherever we need to add path to audio files use the path of the saved google drive audio files and run the cells of the collab file.</br>
* The sections in the .ipynb are used to:</br>
    * Generating the **.wav** file and plotting the audio file.</br>
    * Using *noisereduce* library to de noise the audio signal if needed.</br>
    * Using **Librosa** library, we calculate the pitch and tempo.</br>
    * with the help of **music21** and **MIDIUtil** library, we can plot the UI for musical notes.</br>
    * Now we convert the audio file into <code>**.mid**</code> format and then download it loacally or in the google collab workspace.</br>
    * **Musescore** helps us to visaulize the musical note sheet, where we have to open the <code>.mid</code> file and observe the transcript. </br>

## Results 

![Alt Text](https://github.com/frh02/Automatic_Music_Transcript/blob/master/cqt_plot.png)
CQT plot for sweet child of mine intro. </br>
![Alt Text](https://github.com/frh02/Automatic_Music_Transcript/blob/master/Musical_Notes.JPG)

Final musical note output for midi file. </br>

* The output of the **.wav** file is given in the <code>**sweet_child_music21.mid**</code> file. </br>
# Reference 

* Mounting google drive --<code>https://www.marktechpost.com/2019/06/07/how-to-connect-google-colab-with-google-drive/</code>.</br>
* noise reduction --<code>https://pypi.org/project/noisereduce/</code>.</br>
* Librosa --<code>https://timsainburg.com/noise-reduction-python.html</code>.</br>
* Musescore --<code>https://musescore.org/en</code>.</br>
* music21 --<code>http://web.mit.edu/music21/</code>.</br>



