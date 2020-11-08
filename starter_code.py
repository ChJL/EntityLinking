import gzip
from bs4 import BeautifulSoup
from bs4.element import Comment
from warcio.archiveiterator import ArchiveIterator
# https://pypi.org/project/warcio/
from html_to_text import html_to_text, html2text
from NLP_utils import NLProcess, get_NER

KEYNAME = "WARC-TREC-ID"
#KEYNAME = "WARC-Record-ID"

# The goal of this function process the webpage and returns a list of labels -> entity ID
def find_keys(payload):
    if payload == '':
        return

    # The variable payload contains the source code of a webpage and some additional meta-data.
    # We firt retrieve the ID of the webpage, which is indicated in a line that starts with KEYNAME.
    # The ID is contained in the variable 'key'
    key = None
    for line in payload.splitlines():
        if line.startswith(KEYNAME):
            key = line.split(': ')[1]
            return key;


def split_records(stream):
    payload = ''
    for line in stream:
        if line.strip() == "WARC/1.0":
            yield payload
            payload = ''
        else:
            payload += line
    yield payload
'''
def retrieveText(record):
    if record:
        soup = BeautifulSoup(record,"html5lib")
'''
if __name__ == '__main__':
    import sys
    try:
        _, INPUT = sys.argv
    except Exception as e:
        print('Usage: python starter-code.py INPUT(war.gz file)')
        sys.exit(0)
    count = 0
    with gzip.open(INPUT, 'rb') as stream:
        for record in ArchiveIterator(stream):
            if record.rec_type == 'response':
                    #print(record.rec_headers.get_header(KEYNAME))
                    # the key_ID storing WebpageID, the text storing the text converted by html
                    key_ID = record.rec_headers.get_header(KEYNAME)
                    htmlcontent = record.content_stream().read()
                    '''
                    if count <=245:
                        count+=1
                        continue
                    '''
                    # method 1 for html1 to text
                    soup = BeautifulSoup(htmlcontent, "html5lib")
                    if soup.body == None:
                        continue

                    text = html_to_text(soup)
                    if text == "" or text =="XML RPC server accepts POST requests only ":
                        continue

                    # method 2 for html to text, not very useful
                    #htmlcontent = str(htmlcontent, 'utf-8')
                    #print(type(htmlcontent))
                    #text2 = html2text(htmlcontent)
                    # The Token will return a list with ("string","type")
                    Token = NLProcess(text)

                    if count < 12:
                        print(key_ID)
                        #print(soup)
                        #print("text1=========================")
                        print(text)
                        print("token=========================")
                        print(Token)
                        print("==========",count,"==========")
                        #print('token type:',type(Token))
                    count +=1
                    if count == 12:
                        break




