from bs4 import BeautifulSoup, NavigableString, Tag, Comment
# https://gist.github.com/racitup/2ded9c06c2563049e7e12b25bf2a8369
import re

def html_to_text(html):
    #"Creates a formatted text email message as a string from a rendered html template (page)"
    soup = html
    # Ignore anything in head
    body, text = soup.body, []
    #print(body)
    if body == None:
        return ""

    nouse_id = ['header','code','title']
    [t.extract() for t in body.find_all(id = nouse_id)]
    [t.extract() for t in body(nouse_id)]
    # first way =======================
    for element in body.descendants:
        # We use type and not isinstance since comments, cdata, etc are subclasses that we don't want
        if type(element) == NavigableString:
            parent_tags = (t for t in element.parents if type(t) == Tag)
            hidden = False
            for parent_tag in parent_tags:
                # Ignore any text inside a non-displayed tag
                # We also behave is if scripting is enabled (noscript is ignored)
                # The list of non-displayed tags and attributes from the W3C specs:
                if (parent_tag.name in ('area', 'base', 'basefont', 'datalist', 'head', 'link',
                                        'meta', 'noembed', 'noframes', 'param', 'rp', 'script',
                                        'source', 'style', 'template', 'track', 'title', 'noscript') or
                    parent_tag.has_attr('hidden') or
                    (parent_tag.name == 'input' and parent_tag.get('type') == 'hidden')):
                    hidden = True
                    break
            if hidden:
                continue
            # remove any multiple and leading/trailing whitespace
            string = ' '.join(element.string.split())
            if string:
                if element.parent.name == 'p':
                    # Add extra paragraph formatting newline
                    string = ' ' + string

                text += [string]
    doc = ' '.join(text)
    doc = re.sub('[^a-zA-Z0-9]', ' ', doc)
    #doc = re.sub(r"([^\s.,';:\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",doc)
    #pattern = re.compile(r"[^\s\w',.!?;:-]")
    #doc = pattern.sub('', doc)
    doc = re.sub(r'\s+', ' ', doc)
    return doc



    

if __name__ == '__main__':
    html1 = """You can put your html here to test"""
    print(html_to_text(html1))
    #print(h_t2(html2))