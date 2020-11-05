from bs4 import BeautifulSoup, NavigableString, Tag

def html_to_text(html):
    "Creates a formatted text email message as a string from a rendered html template (page)"
    #soup = BeautifulSoup(html, 'html5lib')
    soup = html
    # Ignore anything in head
    body, text = soup.body, []
    #print(body)
    if body == None:
        return ""

    nouse_id = ['header']
    [s.extract() for s in body.find_all(id = nouse_id)]
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
    return doc


    

if __name__ == '__main__':
    html2 = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <title>
              France image Pool 2012-02-10 16:22:52 </title>

    <meta name="generator" content="WordPress 3.3.1" />
    <meta name="author" content="Aymen" />
    <link rel="stylesheet" href="http://tsawer.net/wpaggregator/wp-content/themes/ocular-professor/style.css" type="text/css" media="screen" />
    <link rel="alternate" type="application/rss+xml" title="Photos aggregator RSS Feed" href="http://tsawer.net/feed/" />
    <link rel="pingback" href="http://tsawer.net/wpaggregator/xmlrpc.php" />
    <!--[if lte IE 7]>
    <link href="http://tsawer.net/wpaggregator/wp-content/themes/ocular-professor/ie.css" type="text/css" rel="stylesheet" media="screen" />
    <![endif]-->
<link rel="alternate" type="application/rss+xml" title="Photos aggregator &raquo; France image Pool 2012-02-10 16:22:52 Comments Feed" href="http://tsawer.net/2012/02/10/france-image-pool-2012-02-10-162252/feed/" />
<link rel='stylesheet' id='contact-form-7-css'  href='http://tsawer.net/wpaggregator/wp-content/plugins/contact-form-7/styles.css?ver=3.1' type='text/css' media='all' />
<link rel='stylesheet' id='A2A_SHARE_SAVE-css'  href='http://tsawer.net/wpaggregator/wp-content/plugins/add-to-any/addtoany.min.css?ver=1.4' type='text/css' media='all' />
<script type='text/javascript' src='http://tsawer.net/wpaggregator/wp-includes/js/jquery/jquery.js?ver=1.7.1'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://tsawer.net/wpaggregator/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://tsawer.net/wpaggregator/wp-includes/wlwmanifest.xml" /> 
<link rel='prev' title='Le Canigou dans la brume' href='http://tsawer.net/2012/02/10/le-canigou-dans-la-brume/' />
<link rel='next' title='maracaibo' href='http://tsawer.net/2012/02/10/maracaibo/' />
<meta name="generator" content="WordPress 3.3.1" />
<link rel='canonical' href='http://tsawer.net/2012/02/10/france-image-pool-2012-02-10-162252/' />
<link rel='shortlink' href='http://tsawer.net/?p=160101' />

<script type="text/javascript"><!--
var a2a_config=a2a_config||{},wpa2a={done:false,html_done:false,script_ready:false,script_load:function(){var a=document.createElement('script'),s=document.getElementsByTagName('script')[0];a.type='text/javascript';a.async=true;a.src='http://static.addtoany.com/menu/page.js';s.parentNode.insertBefore(a,s);wpa2a.script_load=function(){};},script_onready:function(){if(a2a.type=='page'){wpa2a.script_ready=true;if(wpa2a.html_done)wpa2a.init();}},init:function(){for(var i=0,el,target,targets=wpa2a.targets,length=targets.length;i<length;i++){el=document.getElementById('wpa2a_'+(i+1));target=targets[i];a2a_config.linkname=target.title;a2a_config.linkurl=target.url;if(el)a2a.init('page',{target:el});wpa2a.done=true;}}};a2a_config.tracking_callback=['ready',wpa2a.script_onready];
a2a_config.show_title=1;
//--></script>
<!-- Start Of Script Generated By Post-Thumb Revisited Library -->
    <script type="text/javascript" src="http://tsawer.net/wpaggregator/wp-content/plugins/alakhnors-post-thumb/js/xfade2.js"></script>
    <link rel="stylesheet" href="http://tsawer.net/wpaggregator/wp-content/plugins/alakhnors-post-thumb/js/slideshow.css" type="text/css" media="screen" />
    <!-- End Of Script Generated By Post-Thumb Revisited Library -->
<!--[if IE]>
<style type="text/css">
.addtoany_list a img{filter:alpha(opacity=70)}
.addtoany_list a:hover img,.addtoany_list a.addtoany_share_save img{filter:alpha(opacity=100)}
</style>
<![endif]-->


</head>

<body>

<div id="header">

        <div id="blog_title">

            <div id="cap">
            
            <span class="feeds">
<a href="http://tsawer.net/feed/">rss &sect;</a>
<a href="http://tsawer.net/feed/atom/">atom &sect;</a>
<a href="http://tsawer.net/feed/rdf/">rdf</a>
            </span>
            </div>
             

            <h1><a href="http://www.tsawer.net">Photos aggregator</a></h1>
                        <p class="description"> dynamic content </p>
            
                        <div id="search">
              <form method="get" id="searchform" action="http://tsawer.net/">
<div><span class="search">Search:</span><input type="text" value="" size="15" name="s" id="s" />
<input type="submit" id="searchsubmit" value="Go" />

</div>
</form>
                        </div>

                </div>

        <div id="topnav">
        <ul>
            <li class="home "><a href="http://tsawer.net"><IMG SRC="http://tsawer.net/wpaggregator/wp-content/themes/ocular-professor/home.jpg"WIDTH=30 HEIGHT=19></a></li>
            <li class="page_item page-item-4036"><a href="http://tsawer.net/add-blog-photo-album/">Add album/Contact us</a></li>
<li class="page_item page-item-10269"><a href="http://tsawer.net/news/">News</a></li>
<li class="page_item page-item-10277"><a href="http://tsawer.net/reviewstips/">Reviews</a></li>
        </ul>
        </div>



        
</div>
<div id="wrapper">
    
    <div id="single">
    
                       
                <div class="post">
                <p><a href="http://www.flickr.com/people/teesha/">shaggyshoo</a> has added a photo to the pool:</p>
<p><a href="http://www.flickr.com/photos/teesha/6851802115/" title=""><img src="http://farm8.staticflickr.com/7009/6851802115_cc39369d4b_m.jpg" width="240" height="171" alt="" /></a><script type="text/javascript"><!--
google_ad_client = "pub-5874030004227789";
/* 234x60, created 11/2/08 */
google_ad_slot = "7556993120";
google_ad_width = 234;
google_ad_height = 60;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script></p>
<p>annecy. france.</p>
<div class="addtoany_share_save_container"><div class="a2a_kit a2a_target addtoany_list" id="wpa2a_1"><a class="a2a_dd addtoany_share_save" href="http://www.addtoany.com/share_save"><img src="http://tsawer.net/wpaggregator/wp-content/plugins/add-to-any/share_save_171_16.gif" width="171" height="16" alt="Share"/></a></div>
<script type="text/javascript"><!--
wpa2a.script_load();
//--></script>
</div>              </div>
                
                <div class="main_meta">
                    <h2>France image Pool 2012-02-10 16:22:52</h2>
                    <ul>
                        <li>February 10th, 2012</li>
                                                
        
                    </ul>
                    <p class="edit"></p>
                </div>

        

            <div class="clear"></div>
    </div>




</div> <!-- end wrapper -->
<!--cos-html-cache-safe-tag-->  <div id="secondary_nav">
        
        <div id="secondary_nav_content">
        
        <ul>
                    <li id="wp-cumulus" class="widget wp_cumulus_widget">                           <h2 class="widgettitle">Tags cloud</h2>
                        <!-- SWFObject embed by Geoff Stearns geoff@deconcept.com http://blog.deconcept.com/swfobject/ --><script type="text/javascript" src="http://tsawer.net/wpaggregator/wp-content/plugins/wp-cumulus/swfobject.js"></script><div id="wpcumuluswidgetcontent5948318"><p style="display:none;"><a href='http://tsawer.net/tag/2008/' class='tag-link-1033' title='515 topics' style='font-size: 12.3513513514pt;'>2008</a>
<a href='http://tsawer.net/tag/amateur-photographer/' class='tag-link-1683' title='2,320 topics' style='font-size: 18.5945945946pt;'>amateur photographer</a>
<a href='http://tsawer.net/tag/baby/' class='tag-link-61' title='241 topics' style='font-size: 9.22972972973pt;'>baby</a>
<a href='http://tsawer.net/tag/blue/' class='tag-link-188' title='275 topics' style='font-size: 9.7972972973pt;'>blue</a>
<a href='http://tsawer.net/tag/car/' class='tag-link-168' title='283 topics' style='font-size: 9.89189189189pt;'>car</a>
<a href='http://tsawer.net/tag/cat/' class='tag-link-25' title='324 topics' style='font-size: 10.4594594595pt;'>cat</a>
<a href='http://tsawer.net/tag/con/' class='tag-link-1427' title='292 topics' style='font-size: 10.0810810811pt;'>con</a>
<a href='http://tsawer.net/tag/ct/' class='tag-link-104' title='1,203 topics' style='font-size: 15.8513513514pt;'>ct</a>
<a href='http://tsawer.net/tag/ds/' class='tag-link-1410' title='1,108 topics' style='font-size: 15.472972973pt;'>ds</a>
<a href='http://tsawer.net/tag/el/' class='tag-link-877' title='1,149 topics' style='font-size: 15.6621621622pt;'>el</a>
<a href='http://tsawer.net/tag/est/' class='tag-link-921' title='332 topics' style='font-size: 10.5540540541pt;'>est</a>
<a href='http://tsawer.net/tag/flickr/' class='tag-link-1296' title='4,469 topics' style='font-size: 21.2432432432pt;'>flickr</a>
<a href='http://tsawer.net/tag/hot/' class='tag-link-834' title='5,162 topics' style='font-size: 21.8108108108pt;'>hot</a>
<a href='http://tsawer.net/tag/ice/' class='tag-link-129' title='178 topics' style='font-size: 8pt;'>ice</a>
<a href='http://tsawer.net/tag/image/' class='tag-link-1675' title='439 topics' style='font-size: 11.6891891892pt;'>image</a>
<a href='http://tsawer.net/tag/la/' class='tag-link-518' title='1,614 topics' style='font-size: 17.0810810811pt;'>la</a>
<a href='http://tsawer.net/tag/lady/' class='tag-link-732' title='401 topics' style='font-size: 11.3108108108pt;'>lady</a>
<a href='http://tsawer.net/tag/man/' class='tag-link-612' title='384 topics' style='font-size: 11.2162162162pt;'>man</a>
<a href='http://tsawer.net/tag/me/' class='tag-link-662' title='1,397 topics' style='font-size: 16.5135135135pt;'>me</a>
<a href='http://tsawer.net/tag/men/' class='tag-link-494' title='501 topics' style='font-size: 12.2567567568pt;'>men</a>
<a href='http://tsawer.net/tag/mer/' class='tag-link-567' title='205 topics' style='font-size: 8.56756756757pt;'>mer</a>
<a href='http://tsawer.net/tag/nb/' class='tag-link-1300' title='338 topics' style='font-size: 10.6486486486pt;'>nb</a>
<a href='http://tsawer.net/tag/ol/' class='tag-link-613' title='1,617 topics' style='font-size: 17.0810810811pt;'>ol</a>
<a href='http://tsawer.net/tag/one/' class='tag-link-169' title='183 topics' style='font-size: 8.09459459459pt;'>one</a>
<a href='http://tsawer.net/tag/people/' class='tag-link-48' title='4,450 topics' style='font-size: 21.2432432432pt;'>people</a>
<a href='http://tsawer.net/tag/photo/' class='tag-link-89' title='5,322 topics' style='font-size: 22pt;'>photo</a>
<a href='http://tsawer.net/tag/photos/' class='tag-link-1681' title='5,157 topics' style='font-size: 21.8108108108pt;'>photos</a>
<a href='http://tsawer.net/tag/photospicturesamateur-photographer/' class='tag-link-1671' title='1,372 topics' style='font-size: 16.4189189189pt;'>photos
pictures
amateur photographer</a>
<a href='http://tsawer.net/tag/pictures/' class='tag-link-1682' title='2,370 topics' style='font-size: 18.5945945946pt;'>pictures</a>
<a href='http://tsawer.net/tag/port/' class='tag-link-285' title='192 topics' style='font-size: 8.37837837838pt;'>port</a>
<a href='http://tsawer.net/tag/q/' class='tag-link-1113' title='700 topics' style='font-size: 13.6756756757pt;'>q</a>
<a href='http://tsawer.net/tag/ran/' class='tag-link-1629' title='407 topics' style='font-size: 11.4054054054pt;'>ran</a>
<a href='http://tsawer.net/tag/red/' class='tag-link-39' title='275 topics' style='font-size: 9.7972972973pt;'>red</a>
<a href='http://tsawer.net/tag/riot/' class='tag-link-1385' title='236 topics' style='font-size: 9.13513513514pt;'>riot</a>
<a href='http://tsawer.net/tag/tunis/' class='tag-link-7' title='732 topics' style='font-size: 13.8648648649pt;'>Tunis</a>
<a href='http://tsawer.net/tag/tunisia/' class='tag-link-8' title='506 topics' style='font-size: 12.3513513514pt;'>Tunisia</a>
<a href='http://tsawer.net/tag/up/' class='tag-link-158' title='327 topics' style='font-size: 10.5540540541pt;'>up</a>
<a href='http://tsawer.net/tag/us/' class='tag-link-716' title='760 topics' style='font-size: 13.9594594595pt;'>us</a>
<a href='http://tsawer.net/tag/vie/' class='tag-link-1498' title='250 topics' style='font-size: 9.41891891892pt;'>vie</a>
<a href='http://tsawer.net/tag/xt/' class='tag-link-57' title='189 topics' style='font-size: 8.28378378378pt;'>xt</a></p><p>WP Cumulus Flash tag cloud by <a href="http://www.roytanck.com">Roy Tanck</a> and <a href="http://lukemorton.co.uk/">Luke Morton</a> requires <a href="http://www.macromedia.com/go/getflashplayer">Flash Player</a> 9 or better.</p></div><script type="text/javascript">var widget_so5461934 = new SWFObject("http://tsawer.net/wpaggregator/wp-content/plugins/wp-cumulus/tagcloud.swf?r=9653306", "tagcloudflash", "1000", "200", "9", "#ffffff");widget_so5461934.addParam("wmode", "transparent");widget_so5461934.addParam("allowScriptAccess", "always");widget_so5461934.addVariable("tcolor", "0xffffff");widget_so5461934.addVariable("tcolor2", "0xffffff");widget_so5461934.addVariable("hicolor", "0xffffff");widget_so5461934.addVariable("tspeed", "40");widget_so5461934.addVariable("distr", "true");widget_so5461934.addVariable("mode", "tags");widget_so5461934.addVariable("tagcloud", "%3Ctags%3E%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2F2008%2F%27+class%3D%27tag-link-1033%27+title%3D%27515+topics%27+style%3D%27font-size%3A+12.3513513514pt%3B%27%3E2008%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Famateur-photographer%2F%27+class%3D%27tag-link-1683%27+title%3D%272%2C320+topics%27+style%3D%27font-size%3A+18.5945945946pt%3B%27%3Eamateur+photographer%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fbaby%2F%27+class%3D%27tag-link-61%27+title%3D%27241+topics%27+style%3D%27font-size%3A+9.22972972973pt%3B%27%3Ebaby%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fblue%2F%27+class%3D%27tag-link-188%27+title%3D%27275+topics%27+style%3D%27font-size%3A+9.7972972973pt%3B%27%3Eblue%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fcar%2F%27+class%3D%27tag-link-168%27+title%3D%27283+topics%27+style%3D%27font-size%3A+9.89189189189pt%3B%27%3Ecar%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fcat%2F%27+class%3D%27tag-link-25%27+title%3D%27324+topics%27+style%3D%27font-size%3A+10.4594594595pt%3B%27%3Ecat%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fcon%2F%27+class%3D%27tag-link-1427%27+title%3D%27292+topics%27+style%3D%27font-size%3A+10.0810810811pt%3B%27%3Econ%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fct%2F%27+class%3D%27tag-link-104%27+title%3D%271%2C203+topics%27+style%3D%27font-size%3A+15.8513513514pt%3B%27%3Ect%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fds%2F%27+class%3D%27tag-link-1410%27+title%3D%271%2C108+topics%27+style%3D%27font-size%3A+15.472972973pt%3B%27%3Eds%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fel%2F%27+class%3D%27tag-link-877%27+title%3D%271%2C149+topics%27+style%3D%27font-size%3A+15.6621621622pt%3B%27%3Eel%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fest%2F%27+class%3D%27tag-link-921%27+title%3D%27332+topics%27+style%3D%27font-size%3A+10.5540540541pt%3B%27%3Eest%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fflickr%2F%27+class%3D%27tag-link-1296%27+title%3D%274%2C469+topics%27+style%3D%27font-size%3A+21.2432432432pt%3B%27%3Eflickr%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fhot%2F%27+class%3D%27tag-link-834%27+title%3D%275%2C162+topics%27+style%3D%27font-size%3A+21.8108108108pt%3B%27%3Ehot%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fice%2F%27+class%3D%27tag-link-129%27+title%3D%27178+topics%27+style%3D%27font-size%3A+8pt%3B%27%3Eice%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fimage%2F%27+class%3D%27tag-link-1675%27+title%3D%27439+topics%27+style%3D%27font-size%3A+11.6891891892pt%3B%27%3Eimage%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fla%2F%27+class%3D%27tag-link-518%27+title%3D%271%2C614+topics%27+style%3D%27font-size%3A+17.0810810811pt%3B%27%3Ela%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Flady%2F%27+class%3D%27tag-link-732%27+title%3D%27401+topics%27+style%3D%27font-size%3A+11.3108108108pt%3B%27%3Elady%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fman%2F%27+class%3D%27tag-link-612%27+title%3D%27384+topics%27+style%3D%27font-size%3A+11.2162162162pt%3B%27%3Eman%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fme%2F%27+class%3D%27tag-link-662%27+title%3D%271%2C397+topics%27+style%3D%27font-size%3A+16.5135135135pt%3B%27%3Eme%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fmen%2F%27+class%3D%27tag-link-494%27+title%3D%27501+topics%27+style%3D%27font-size%3A+12.2567567568pt%3B%27%3Emen%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fmer%2F%27+class%3D%27tag-link-567%27+title%3D%27205+topics%27+style%3D%27font-size%3A+8.56756756757pt%3B%27%3Emer%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fnb%2F%27+class%3D%27tag-link-1300%27+title%3D%27338+topics%27+style%3D%27font-size%3A+10.6486486486pt%3B%27%3Enb%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fol%2F%27+class%3D%27tag-link-613%27+title%3D%271%2C617+topics%27+style%3D%27font-size%3A+17.0810810811pt%3B%27%3Eol%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fone%2F%27+class%3D%27tag-link-169%27+title%3D%27183+topics%27+style%3D%27font-size%3A+8.09459459459pt%3B%27%3Eone%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fpeople%2F%27+class%3D%27tag-link-48%27+title%3D%274%2C450+topics%27+style%3D%27font-size%3A+21.2432432432pt%3B%27%3Epeople%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fphoto%2F%27+class%3D%27tag-link-89%27+title%3D%275%2C322+topics%27+style%3D%27font-size%3A+22pt%3B%27%3Ephoto%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fphotos%2F%27+class%3D%27tag-link-1681%27+title%3D%275%2C157+topics%27+style%3D%27font-size%3A+21.8108108108pt%3B%27%3Ephotos%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fphotospicturesamateur-photographer%2F%27+class%3D%27tag-link-1671%27+title%3D%271%2C372+topics%27+style%3D%27font-size%3A+16.4189189189pt%3B%27%3Ephotos%0Apictures%0Aamateur+photographer%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fpictures%2F%27+class%3D%27tag-link-1682%27+title%3D%272%2C370+topics%27+style%3D%27font-size%3A+18.5945945946pt%3B%27%3Epictures%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fport%2F%27+class%3D%27tag-link-285%27+title%3D%27192+topics%27+style%3D%27font-size%3A+8.37837837838pt%3B%27%3Eport%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fq%2F%27+class%3D%27tag-link-1113%27+title%3D%27700+topics%27+style%3D%27font-size%3A+13.6756756757pt%3B%27%3Eq%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fran%2F%27+class%3D%27tag-link-1629%27+title%3D%27407+topics%27+style%3D%27font-size%3A+11.4054054054pt%3B%27%3Eran%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fred%2F%27+class%3D%27tag-link-39%27+title%3D%27275+topics%27+style%3D%27font-size%3A+9.7972972973pt%3B%27%3Ered%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Friot%2F%27+class%3D%27tag-link-1385%27+title%3D%27236+topics%27+style%3D%27font-size%3A+9.13513513514pt%3B%27%3Eriot%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Ftunis%2F%27+class%3D%27tag-link-7%27+title%3D%27732+topics%27+style%3D%27font-size%3A+13.8648648649pt%3B%27%3ETunis%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Ftunisia%2F%27+class%3D%27tag-link-8%27+title%3D%27506+topics%27+style%3D%27font-size%3A+12.3513513514pt%3B%27%3ETunisia%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fup%2F%27+class%3D%27tag-link-158%27+title%3D%27327+topics%27+style%3D%27font-size%3A+10.5540540541pt%3B%27%3Eup%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fus%2F%27+class%3D%27tag-link-716%27+title%3D%27760+topics%27+style%3D%27font-size%3A+13.9594594595pt%3B%27%3Eus%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fvie%2F%27+class%3D%27tag-link-1498%27+title%3D%27250+topics%27+style%3D%27font-size%3A+9.41891891892pt%3B%27%3Evie%3C%2Fa%3E%0A%3Ca+href%3D%27http%3A%2F%2Ftsawer.net%2Ftag%2Fxt%2F%27+class%3D%27tag-link-57%27+title%3D%27189+topics%27+style%3D%27font-size%3A+8.28378378378pt%3B%27%3Ext%3C%2Fa%3E%3C%2Ftags%3E");widget_so5461934.write("wpcumuluswidgetcontent5948318");</script>          </li>
        <li id="twitter-1" class="widget widget_twitter"><h2 class="widgettitle"><a href="http://twitter.com/photobabble" class="twitter_title_link">Twits from 'photobabble'</a></h2>
<ul class="twitter"><li>No public Twitter messages.</li></ul></li>
        
         </ul>
        </div>
        <div class="clear"></div>
    </div>
    
    <div id="footer">
    <div class="copyright">
    <p><a href="http://andreamignolo.com/themes/wordpress/ocular-professor">Based on Ocular Professor</a> &sect; Powered by <a href="http://wordpress.org">WordPress</a>
    </p>
    </div>

</div>


<center>
<!-- Site Meter -->
<script type="text/javascript" src="http://s24.sitemeter.com/js/counter.js?site=s24tsawer">
</script>
<noscript>
<a href="http://s24.sitemeter.com/stats.asp?site=s24tsawer" target="_top">
<img src="http://s24.sitemeter.com/meter.asp?site=s24tsawer" alt="Site Meter" border="0"/></a>
</noscript>
<!-- Copyright (c)2009 Site Meter -->


<script type="text/javascript"><!--
google_ad_client = "pub-5874030004227789";
/* 728x15, created 9/1/10 */
google_ad_slot = "2505791487";
google_ad_width = 728;
google_ad_height = 15;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>


</center>



</body>

<script type="text/javascript"><!--
wpa2a.targets=[
{title:'France image Pool 2012-02-10 16:22:52',url:'http://tsawer.net/2012/02/10/france-image-pool-2012-02-10-162252/'}];
wpa2a.html_done=true;if(wpa2a.script_ready&&!wpa2a.done)wpa2a.init();wpa2a.script_load();
//--></script>

<script>
var related_posts_container = 'search_content',
    related_posts_title     = 'Photos aggregator',
    related_posts_lang      = 'en-US';
</script>
<script src="http://tsawer.net/wpaggregator/wp-content/plugins/search-engine-related-posts/asset/serp-min.js"></script>
<script type='text/javascript' src='http://tsawer.net/wpaggregator/wp-content/plugins/contact-form-7/jquery.form.js?ver=2.52'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var _wpcf7 = {"loaderUrl":"http:\/\/tsawer.net\/wpaggregator\/wp-content\/plugins\/contact-form-7\/images\/ajax-loader.gif","sending":"Sending ...","cached":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='http://tsawer.net/wpaggregator/wp-content/plugins/contact-form-7/scripts.js?ver=3.1'></script>
</html>"""
    print(html_to_text(html2))
    #print(h_t2(html2))