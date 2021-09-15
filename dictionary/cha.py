#coding=gbk
import requests
import bs4 as bs
import argparse

YOUDAO_API = 'http://dict.youdao.com/search?q=%s&keyfrom=dict.index'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/46.0.2490.71 Safari/537.36'
YOUDAO = 'http://dict.youdao.com/'
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

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
    return parser

def get_interp(word,p=0):
    result = []
    r = requests.get(YOUDAO_API % word,
                             headers={
                                 'referer': YOUDAO,
                                 'user-agent': USER_AGENT
            })
    b = bs.BeautifulSoup(r.content)
    #print(b)
    lis = b.find('div', {'class':'trans-container'})
    #print(lis)
    if lis is not None:
        for i in lis.findAll('li'):
            result.append(i.text)
    exams = []
    phones = []
    try:
        phonetics = b.findAll('span',{'class':"phonetic"})
        if phonetics is not None:
            for ph in phonetics:
                phones.append(ph.text)
        #print(phones)
        examples = b.findAll('a',{'class':'sp dictvoice voice-js log-js'})
        if examples is not None:
           for i in examples:
               if "dict.main.blng" in str(i):
                   a = i.get('data-rel')
                   if a is not None:
                      e = " ".join( a.split("+"))  
                      exams.append(e.strip("&le=eng"))
    except:
        pass
    if p == 1:
        if len(result) == 0 and word != "":
            print(word)
        #print(word," "*20,result)
        #for i in range(len(exams)):
        #    print(" "*25, exams[i])
        #print()
    
    return result,exams,phones


def file_itp(input_file, output_file):
    with open(input_file, 'r') as f:
        for each in f.readlines():
            #print(each.split('  '))
            word = each.strip("\n")
            #word ="good"
            count = 1 
            make_parser()
            result = get_interp(word,p=1)
            '''
            with open(output_file, 'a') as fi:
                fi.write('\n%s' % (word))
                if len(result) == 0:
                    fi.write('\t暂未找到')
                    continue
                for i in xrange(len(result)):
                    try:
                        fi.write('\t%d. %s\n' % (i+1, result[i].encode('gbk')))
                    except Exception as e:
                        print (word, e.message)
                        fi.write('\t暂未得到')
            '''


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    INPUT_FILE = args.file
    file_itp(INPUT_FILE, OUTPUT_FILE)
