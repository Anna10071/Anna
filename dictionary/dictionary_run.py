import argparse
import random
import time
from collections import Iterable
import sys
import os
#ffmpeg_path = "/usr/local/ffmpeg/bin/"
#os.environ["PATH"] += os.pathsep + ffmpeg_path
import numpy as np

import requests
import simpleaudio as sa
from pydub import AudioSegment
#AudioSegment.ffmpeg = "/usr/local/ffmpeg/bin"
#AudioSegment.converter = "/usr/local/ffmpeg/bin/ffmpeg"
#AudioSegment.ffmpeg = "/usr/local/ffmpeg/bin/ffmpeg"
#AudioSegment.ffprobe ="/usr/local/ffmpeg/bin/ffprobe"
from contextlib import contextmanager
from os import chdir, getcwd, listdir, remove, makedirs
from os.path import isfile, exists, join, expanduser
import cha
import sys

def check_cache(f):
    def _wrapper(words):
        if not isinstance(words, Iterable):
            words = (words)
        for word in words:
            if not isfile(word + '.wav'):
                f([word])
    return _wrapper


def format_transfer(name, ori_format, target_format, remove_ori=False):
    """ori_format, target_format: only 'mp3' and 'wav' and supported"""
    try:
        song = getattr(AudioSegment, "from_" + ori_format)(name + "." + ori_format)
        song.export(name + "." + target_format, format=target_format)
    except:
        print("audio error " + name)
        pass
        #raise ValueError("Only 'mp3' and 'wav' format are supported")
    if remove_ori:
        remove(name + "." + ori_format)


@check_cache
def download_audio(words, target_format='wav'):
    num_words = len(words)
    index_i = 0
    for word in words:
        r = requests.get(
            url='http://dict.youdao.com/dictvoice?audio=' + word + '&type=1',
            stream=True)
        with open(word + '.mp3', 'wb+') as f:
            f.write(r.content)
        format_transfer(word, 'mp3', target_format, remove_ori=True)
        index_i += 1
        print("Download audio : ",word,num_words,index_i)

def play_audio(audio, wait=False, sleep=0):
    wave_obj = sa.WaveObject.from_wave_file(audio)
    play_obj = wave_obj.play()
    if wait:
        play_obj.wait_done()


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--interval-time",
        help="the interval time (seconds) between two words (default: 1)",
        type=int,
        default=1)

    parser.add_argument(
        "-f",
        "--file",
        help="specify the origin of words (default: words.txt)",
        type=str,
        default="words.txt")

    parser.add_argument(
        "-pre",
        "--prefix",
        help="specify the origin of words (default: words.txt)",
        type=str,
        default="")

    parser.add_argument(
        "-o",
        "--output",
        help="specify a file storing words with actual order (default ans.txt)",
        type=str,
        default="ans.txt")

    parser.add_argument(
        "-cd",
        "--cache-directory",
        help="specify the directory storing cache (default cache)",
        type=str,
        default="cache")

    parser.add_argument(
        "-rd",
        "--random",
        help="play words according to the random order",
        action="store_true",
        default=False)

    parser.add_argument(
        "-s",
        "--sort",
        help="sort all the words in alphabetical order",
        action="store_true",
        default=False)

    parser.add_argument(
        "-rs",
        "--reverse-sort",
        help="sort reversely all the words in alphabetical order",
        action="store_true",
        default=False)

    parser.add_argument(
        "-no",
        "--normal-order",
        help="play words according to order of the appearance in file (default)",
        action="store_true",
        default=True)

    parser.add_argument(
        "-ro",
        "--reverse-order",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)
    
    parser.add_argument(
        "-cn",
        "--chinese",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)
    
    parser.add_argument(
        "-sp",
        "--spell",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)
    parser.add_argument(
        "-tr",
        "--trans",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)
    parser.add_argument(
        "-c2e",
        "--cn2en",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)
    
    parser.add_argument(
        "-exam",
        "--exams",
        help="play words according to reverse order of the appearance in file",
        action="store_true",
        default=False)

    return parser

@contextmanager
def change_dir(target_path):
    """A function assisting change working directory temporarily

    >>> import os
    >>> os.chdir(os.path.expanduser('~'))
    >>> os.getcwd() == os.path.expanduser('~')  # You're in your home directory now
    True
    >>> with change_dir('/usr/local'): # change working directory to '/usr/local'
    ...     print(os.getcwd())
    ...     pass # Anything you want to do in this directory
    ...
    /usr/local
    >>> os.getcwd() == os.path.expanduser('~') # You're back in your previous working directory
    True

    """
    current_path = getcwd()
    chdir(target_path)
    yield
    chdir(current_path)

import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def translation_list(lst):
    print("start translation")
    result_dict = {}
    word_num = len(lst)
    result_dict = load_obj("translation_cache")
    '''for line in open("error_11.txt"):
        #print(line)
        lines = line.strip("\n").split("，")
        print(lines)
        if len(lines) == 2:
            word_key = lines[0]
            word_trans = [lines[1]]
            result_dict[word_key] = (word_trans,[]) 
    print(result_dict)'''
    word_index = 0
    for word in lst:
        word_index += 1
        if word not in result_dict:
            result_dict[word] = cha.get_interp(word)
        if word in result_dict:
            if len(list(result_dict[word])) == 2:
                _,_,p = cha.get_interp(word)
                result_dict[word] = (result_dict[word][0],result_dict[word][1],p) 
        print(word,result_dict[word],"  ",word_index,"/",word_num)
    print("end translation!")
    save_obj(result_dict,"translation_cache") 
    return result_dict

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    
    with open(args.file) as f:
        lst = f.readlines()
        lst = (item.strip() for item in lst)
        lst = [item for item in lst if item != '']

    if args.random:
        random.shuffle(lst)
    elif args.reverse_order:
        lst = lst[::-1]
    elif args.sort or args.reverse_sort:
        lst = sorted(lst, reverse=args.reverse_sort)

    args.cache_directory = expanduser(args.cache_directory)
    if not exists(args.cache_directory):
        makedirs(args.cache_directory)
    input_words = []
    error_words = []
    chinese_error_words = []
    error_count_dict = {}
    for line in open("awl_history_error_"+args.prefix):
        if len(line.strip("\n").split(",")) != 2:
            continue
        w_1, count_1 = line.strip("\n").split(",")
        error_count_dict[w_1] = int(count_1)
     
    with change_dir(args.cache_directory):
        now_num = 0
        error_num = 0
        download_audio(lst)
        translation_dict = translation_list(lst)
        for item,w in [(item+ '.wav',item) for item in lst]:
         try:
            print ("%s / %s ERROR %s"%(str(now_num) , str(len(lst)), str(error_num)))
            now_num += 1
            if not args.cn2en and not args.trans:
                play_audio(item)
            translation,e,ph = translation_dict[w]
            ph_str = ""
            if len(list(ph)) >= 1:
                ph_str = ph[0]
          
            if args.cn2en:
                print(translation)
            input_str = ''
            if args.spell:
                input_str = input("Enter your input: ")
            input_words.append(input_str)
            if args.spell and input_str.lower() != w.lower():
                error_num += 1
                if w not in error_count_dict:
                    error_count_dict[w] = 1
                else:
                    error_count_dict[w] += 1
                
                #print ("\n\n Error : %s -> %s  %s \n\n"%(input_str,w, ph_str))
                print(" "*20,"ERROR")
                print(" "*20,w)
                print(" "*20,input_str)
                print(" "*20,ph_str)
                if args.exams == False:
                    
                    for i in range(3):
                        play_audio(item)
                        in_s = input("\n\n\nPlease correct your spell \n                     : ")
                        if in_s.strip().lower() == w.lower():
                            print(" "*19,w)
                            print(translation)
                            for i in range(3):
                                play_audio(item)
                                input(" "*20)
                            break
                #play_audio(item)
                #input_str = input(": ")
                error_words.append(w)
            if args.cn2en:
               play_audio(item)
            
            if args.chinese == False:
                print (w)
            else:
                ts = ""
                #translation,e = cha.get_interp(w)
                if args.trans:
                    s ="\n"*10 + " "*10 + w + "\n"*10
                    input_ts = input(s + " "*10 + ":")
                    if input_ts not in " ".join(translation) and input_ts != "9":
                        print("\n".join(e),"\n\n")
                        input("GO..........")
                    play_audio(item)
                
                print(w,ph_str,translation,"\n")
                print("\n".join(e),"\n\n")
                
                #input("Continue ..........")

                if args.trans:
                    if input_ts not in " ".join(translation) and input_ts != "9":
                        error_num += 1
                        if w not in error_count_dict:
                            error_count_dict[w] = 1
                        else:
                            error_count_dict[w] += 1
                            error_num += 1
                        chinese_error_words.append(w)
                        #print("Error : ",input_ts,translation)
            if not args.spell or args.trans:        
                time.sleep(args.interval_time)
         except:
            print("Error") 
            pass
    if args.spell and len(error_words)!=0:
        error_rate = len(error_words)/len(lst)
        print("Error rate:", error_rate) 
        t = time.strftime("%m%d%H%M", time.localtime()) 
        print(args.file+"_"+ t)
        with open(args.file+"_"+ t, "w") as f:
            f.write("\n".join(error_words))
        print("\n".join(error_words))
   
    if args.trans and len(chinese_error_words)!=0:
        error_rate = len(chinese_error_words)/len(lst)
        print("Error rate:", error_rate) 
        t = time.strftime("%m%d%H%M", time.localtime())
        print(args.file+"_"+ t)
        with open(args.file+"_"+ t, "w") as f:
            f.write(str(error_rate)+"\n"+"\n".join(chinese_error_words))
        print("\n".join(chinese_error_words))
    with open("awl_history_error_"+args.prefix,"w") as f:
        for k,v in error_count_dict.items():
            f.write(k+","+str(v)+"\n")
    if args.output:
        with open(args.output, 'w+') as f:
            f.write("\n".join(lst))
