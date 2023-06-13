# coding:utf-8
import re
from markdown import Extension
from markdown.postprocessors import Postprocessor

import unittest


class TestExtension(Extension):
    def extendMarkdown(self, md ):
        md.registerExtension(self)
        # 数字が若いほうが後で処理されるのか。
        md.postprocessors.register( ContinueIframe() , 'ContinueIframe' , 1 )
        #md.postprocessors.register( ContinueIframe( "text foo bar" ) , 'ContinueIframe' , 1 )


#textは</iframe>タグの後ろで勝手に改行されたものになってしまう。
class ContinueIframe(Postprocessor):
    #def __init__(self, text ):
    #    print( text )
    
    def run(self , text ):
        text = re.sub( '</iframe>\n<iframe' , '</iframe><iframe' , text )
        return text

def makeExtension(*args, **kwargs):
    return TestExtension(*args, **kwargs)


class TextClass( unittest.TestCase ):
    def test_extends( self ):
        import markdown
        #md = markdown.Markdown()
        md = markdown.Markdown( extensions = ["markdownExtension_ContinueIframe"] )
        text = '''
##title
<iframe AAA sandbox="allow-popups allow-scripts allow-modals allow-forms allow-same-origin" style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=roost-22&language=ja_JP&o=9&p=8&l=as4&m=amazon&f=ifr&ref=as_ss_li_til&asins=B0B1DJ3W1P&linkId=7c27e6a2b577268d56923715f34a3e78"></iframe><iframe BBB sandbox="allow-popups allow-scripts allow-modals allow-forms allow-same-origin" style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=roost-22&language=ja_JP&o=9&p=8&l=as4&m=amazon&f=ifr&ref=as_ss_li_til&asins=B0B1DJ3W1P&linkId=7c27e6a2b577268d56923715f34a3e78"></iframe><iframe CCC sandbox="allow-popups allow-scripts allow-modals allow-forms allow-same-origin" style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=roost-22&language=ja_JP&o=9&p=8&l=as4&m=amazon&f=ifr&ref=as_ss_li_til&asins=B0B1DJ3W1P&linkId=7c27e6a2b577268d56923715f34a3e78"></iframe>
'''
        print(md.convert(text))

if __name__ == "__main__":
    unittest.main()
