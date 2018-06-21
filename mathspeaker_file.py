# -*- coding: utf-8 -*-

###########################################################
# Main to control al of the project´s modules.
# Syntax:
#    python scriptname --pip <ip> --pport <port>
# 
#    --pip <ip>: specify the ip of your robot (without specification it will use the NAO_IP defined some line below
#
# Author: Ricardo Apú, Pablo Vargas, Jean Carlo Zúñiga
# UCR
###########################################################
import os 
import math_speaker
import re
import time
import pygame
from optparse import OptionParser

MATHMODE_PATTERN = re.compile("\$.*\$")



def main():
    """ 
    Main entry point
    """
    parser = OptionParser()
    parser.add_option("--filepath",
        help="path to the tex file to read",
        dest="filepath")
    parser.add_option("--lang",
        help="language to read",
        dest="lang")
    parser.set_defaults(
        filepath=None,
        lang='es')

    (opts, args_) = parser.parse_args()
    filepath   = opts.filepath
    lang = opts.lang
    # said_title = False
    # said_author = False
    math_speaker.init(lang)
    pygame.mixer.init()
    if filepath is not None:
        try:
            with open(file=filepath, mode='r', encoding='utf-8') as f:
                # while line and not said_title and not said_author:
                    # if line.startswith('%'):
                        # continue
                    # """
                        # Dice título y autor
                    # """
                    # if line.startswith('\\begin{document}'):
                    # line = f.readline()
                line = f.readline()
                while not line.startswith('\\begin{document}'):
                    line = f.readline()
                while line:
                    if line.startswith('%'):
                        line = f.readline()
                        continue
                    result = MATHMODE_PATTERN.search(line)
                    if result is not None:
                        result = result.group().replace("$","")
                        print(result)
                        # print(line)
                        math_speaker.math_tts(result)                        
                        pygame.mixer.music.load('output.mp3')
                        pygame.mixer.music.play()
                        while pygame.mixer.music.get_busy(): 
                            pygame.time.Clock().tick(10)
                    line = f.readline()

        except OSError as e:
            # 'File not found' error message.
            print("File not found" + str(e))
        except KeyboardInterrupt as e:
            print("Bye bye")

    else:
        print('Invalid filepath')

def generate_sample(preview):
    print("* Generating sample...")
    OUTPUT_SAMPLE_RATE = 48000
    if preview:
        print("* Previewing audio file...")
        import pyaudio
        from gtts import gTTS
        tts = gTTS(text='Hello', lang='en')
        tts.save("synthesized.mp3")
        import vlc
        path = os.getcwd() 
        p = vlc.MediaPlayer(path+"/synthesized.mp3")
        p.play()

    else:
        write('sound.wav', SAMPLE_RATE, tone_out)
        print("* Wrote audio file!")
        



if __name__ == "__main__":
    main()