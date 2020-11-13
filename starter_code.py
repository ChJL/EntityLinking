import gzip
from bs4 import BeautifulSoup
from bs4.element import Comment
from warcio.archiveiterator import ArchiveIterator
# https://pypi.org/project/warcio/
from html_to_text import html_to_text, parse_html
from NLP_utils import NLProcess, get_NER
from test_elasticsearch_server import ELSsearch, search
from strsimpy.cosine import Cosine
import textdistance

KEYNAME = "WARC-TREC-ID"
#KEYNAME = "WARC-Record-ID"

def jaccard_sim(str1,str2):
    token1 = str1.split()
    token2 = str2.split()
    jaccard_score = textdistance.jaccard(token1,token2)
    return jaccard_score

def cos_sim(str1,str2):
    cosine = Cosine(2)
    p1 = cosine.get_profile(str1)
    p2 = cosine.get_profile(str2)
    score = cosine.similarity_profiles(p1, p2)
    return score

def generate_candidates(NER_mention):
    candidates = None
    candidates = ELSsearch(NER_mention).items()
    return candidates

def split_records(stream):
    payload = ''
    for line in stream:
        if line.strip() == "WARC/1.0":
            yield payload
            payload = ''
        else:
            payload += line
    yield payload

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

                    # try for few pages:
                    #if key_ID == "clueweb12-0000tw-00-00017":
                    #    break

                    htmlcontent = record.content_stream().read()
                    
                    # method for html to text, if the soup return is none, drop current webpage
                    soup = BeautifulSoup(htmlcontent, "lxml")
                    if soup == None:
                        continue

                    # if there is no raw text return, we drop the current webpage
                    text = html_to_text(soup)
                    if text == "" or text == " XML RPC server accepts POST requests only ":
                        continue

                    # The NER_mentions is a list with ("string","type")
                    NER_mentions = NLProcess(text)
                    # drop duplicate in NER_mentions
                    NER_mentions = list(dict.fromkeys(NER_mentions))

                    
                    final_entities = []
                    for mention in NER_mentions:
                        # candidates is a dictionary with 10 results
                        candidates = generate_candidates(mention[0])
                        #print("mention: ",mention)
                        #print("mention type: ", type(mention[0]))

                        can_with_max_score = ""
                        max_score = 0
                        max_entity = []
                        if candidates == None:
                            continue
                        for entity_id, labels in candidates:

                            # convert labels into string type 
                            labels_str = ', '.join(labels)
                            
                            
                            # if words of mention are "completely" in labels, add a bonus score 0.1
                            contain_score = 0
                            if mention[0] in labels_str:
                                contain_score = 0.1
                            # do the string similarity
                            temp_score = jaccard_sim(labels_str,mention[0]) + contain_score
                            if temp_score > max_score:
                                max_score = temp_score
                                max_entity = [mention[0],entity_id]
                            #print("temp_score: ", temp_score)
                        if len(max_entity) != 0 and max_score >= 0.7:
                            final_entities.append(max_entity)
                        

                    #print("--final_entities--")
                    if len(final_entities) > 0:
                        #print(final_entities)
                        for final_enity in final_entities:
                            print(key_ID + '\t' + final_enity[0] + '\t' + final_enity[1])


        



