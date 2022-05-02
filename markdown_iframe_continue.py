# coding:utf-8
import markdown
from markdown import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor
from markdown.htmlparser import HTMLExtractor
import re

import unittest


class MyExtension(Extension):
    def extendMarkdown(self, md ):
        md.postprocessors.register(MyClass(),'name',1)

class MyClass(Postprocessor):
    def run(self , text ):
        output_text = ''
        hold_line = ''

        line_max = len(text.splitlines())
        count = 0

        for line in text.splitlines():
            count = count + 1

            #行の終わりが</iframe>$なら一度ストックする。
            start_match = re.search('</iframe>$', line)
            if start_match:
                if hold_line == '':
                    hold_line = line
                else:
                    hold_line = hold_line + line
                #この行が最後の場合に出力
                if line_max == count:
                    output_text = output_text + '\n'+ hold_line
                continue
            
            #未処理の行が残っている
            if hold_line != '':
                #この行の先頭が<iframe>
                end_match = re.search('^<iframe', line)
                if end_match:
                    hold_line = hold_line + line
                else:
                    output_text = output_text + '\n' + hold_line + '\n' + line
                    hold_line = ''

            else:
                output_text = output_text + '\n' + line

        return output_text


def makeExtension(*args, **kwargs):
    return MyExtension(*args, **kwargs)

class TextClass(unittest.TestCase):
    def test_extends(self):
        import markdown
        md = markdown.Markdown(extensions=['markdown_iframe_continue'])

        text = '''
##title
<iframe></iframe>
<iframe></iframe>
<iframe></iframe>
'''
        print(md.convert(text))

if __name__ == "__main__":
    unittest.main()
    
