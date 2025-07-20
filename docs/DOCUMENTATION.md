
# Documentation for contributers

The project is built using Python as the programming language and PyQt5 as the GUI library. It also takes the help of pyinstaller extension to convert the python script into a single executable file.

- The code used to build the program can be found inside `scripts` folder. The main python script is the file `mouse_click_prank.py` (you can run this file to see the changes before making the .exe file) and the additional custom modules can be found in `scripts/modules`.

- The assets used can be found inside `assets` folder.

- The `resource_path` module is a function that creates an absolute path by taking in a relative path.

- The `sound_effects` module contain the dictionary containing the audio library, and the audio files are stored inside `assets/sounds` folder. 

- If you are planning to add additional sound effects, please add the audio description and the file name in the `sound_effects` dictionary following the format of the previous entries, and store the audio file (.mp3) inside the `assets/sounds` folder

- After the changes are made, the script is converted to an executable using the code `pyinstaller build/mouse_click_prank.spec`. 

- The `mouse_click_prank.spec` file contains the settings built-in. The compiled `mouse_click_prank.exe` file can be found inside the `dist` folder.

- After the pull request is merged, I will build the setup wizard file in my local computer. I use Inno Setup for this process, and the code differ from system to system so it's better to leave it to me :)

- After building the setup wizard file, I will release it. You can find it in the releases section of the repository.

[Learn how to contribute to this project](docs/CONTRIBUTE)