# -*- coding: utf-8 -*-

###########################################################
# Script to read outloud a math document writen in LaTeX
# Syntax:
#
#   python3 mathspeaker_file.py --filepath <filepath> --lang <lang: es | en>
#
# Author: Ricardo Apú, Alonso Mondal
# UCR
###########################################################
import os 
import math_speaker
import re
import time
import pygame
from optparse import OptionParser
import sys,tty,termios
class _Getch:
    """
        simulate unix's getch to control flow with arrowkeys
    """
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get_arrow_key():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
        else:
                return None
    

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
                        while get_arrow_key() != 'right':
                            continue
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