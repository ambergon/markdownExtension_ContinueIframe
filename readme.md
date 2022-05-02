# markdown-iframe-continue
markdown_iframe_continueはiframeタグが連続して続く場合に改行されないようにするために作られました。
```
#default
##md
<iframe ...></iframe><iframe ...></iframe> ->
##html
<iframe ...></iframe>
<iframe ...></iframe>

#default
##md
<iframe ...></iframe>
<iframe ...></iframe> ->
##html
<iframe ...></iframe>
<iframe ...></iframe> 
```
```
#extension markdown_iframe_continue
##md
<iframe ...></iframe><iframe ...></iframe> ->
##html
<iframe ...></iframe><iframe ...></iframe> 

##md
<iframe ...></iframe>
<iframe ...></iframe> ->
##html
<iframe ...></iframe><iframe ...></iframe> 

#他の文字列が混入した場合
iframeのみが連続することのみを想定している
##md
<iframe></iframe>
<iframe></iframe>aaa
<iframe></iframe>
##html
<iframe></iframe><iframe></iframe>
<p>aaa</p>
<iframe></iframe>

##md
<iframe></iframe>
aaa<iframe></iframe>
<iframe></iframe>
##html
<iframe></iframe>
<p>aaa<iframe></iframe></p>
<iframe></iframe>
```

## Usage
```
md = markdown.Markdown(extensions=['markdown_iframe_continue'])
```

## Requirements
```
import markdown
```

## Installation
```
pip install git+https://github.com/ambergon/markdown_iframe_continue
```

## License
MIT

## Author
ambergon


[twitter](https://twitter.com/Sc_lFoxGon)
