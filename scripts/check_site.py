"""Validate a complete CORE build in root or subdirectory hosting."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, parse_qs
import argparse
import json
import re
import xml.etree.ElementTree as ET

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.ids=set()
        self.titles=0
        self.h1=0
        self.select_values=set()
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if 'id' in values:self.ids.add(values['id'])
        if tag=='title':self.titles+=1
        if tag=='h1':self.h1+=1
        if tag=='option' and values.get('value'):self.select_values.add(values['value'])
        for key in ('href','src','action'):
            if key in values:self.links.append(values[key])

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('directory',nargs='?',default='dist')
    parser.add_argument('--base-path',default='')
    args=parser.parse_args()
    root=Path(args.directory).resolve()
    base=('/'+args.base_path.strip('/')) if args.base_path.strip('/') else ''
    pages={}
    errors=[]
    for path in root.rglob('*.html'):
        page=Page();page.feed(path.read_text());pages[path]=page
    if len(pages)!=19:errors.append(f'Expected 18 pages and 404; found {len(pages)} HTML files.')
    choices=pages.get(root/'contato/index.html',Page()).select_values
    references=0
    for path,page in pages.items():
        if page.titles!=1 or page.h1!=1:errors.append(f'{path.relative_to(root)}: expected one title and h1.')
        for link in page.links:
            target_url=urlsplit(link)
            if target_url.scheme or target_url.netloc:continue
            references+=1
            public_path=unquote(target_url.path)
            if public_path.startswith('/'):
                if base and not (public_path==base or public_path.startswith(base+'/')):
                    errors.append(f'{path.relative_to(root)}: link outside deployment base: {link}');continue
                relative=public_path[len(base):].lstrip('/') if base else public_path.lstrip('/')
                target=root/relative
            elif public_path:target=path.parent/public_path
            else:target=path
            if target.is_dir():target=target/'index.html'
            if not target.exists():errors.append(f'{path.relative_to(root)}: missing {link}')
            elif target_url.fragment and target in pages and target_url.fragment not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing fragment {link}')
            service=parse_qs(target_url.query).get('servico',[None])[0]
            if service and service not in choices:errors.append(f'Unknown form service: {service}')
    css=root/'assets/style.css'
    if not css.exists():errors.append('Missing stylesheet.')
    else:
        for public_path in re.findall(r'url\([\'\"]?(/[^)\'\"]+)',css.read_text()):
            if base and not public_path.startswith(base+'/'):errors.append('CSS asset ignores base path: '+public_path)
            relative=public_path[len(base):].lstrip('/') if base else public_path.lstrip('/')
            if not (root/relative).exists():errors.append('Missing CSS asset: '+public_path)
    for path in pages:
        text=path.read_text()
        if 'core-gestao-saude.curlyspice6.chatgpt.site' in text:errors.append(f'{path.relative_to(root)}: legacy Site origin in generated HTML.')
        for encoded in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
            try:json.loads(encoded)
            except ValueError:errors.append(f'{path.relative_to(root)}: invalid structured data.')
    try:
        sitemap=ET.parse(root/'sitemap.xml')
        urls=sitemap.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        if len(urls)!=18:errors.append('Sitemap must list 18 public pages.')
    except (OSError,ET.ParseError):errors.append('Missing or invalid sitemap.xml.')
    for asset in ('logo.svg','logo-white.svg','symbol.svg','manrope-vf.woff2','site.js','surgery.jpg','hero.jpg','care.jpg','technology.jpg','laundry-industrial.jpg','OFL-Manrope.txt'):
        if not (root/'assets'/asset).is_file():errors.append('Missing asset: '+asset)
    if errors:
        for error in errors:print('ERROR:',error)
        raise SystemExit(1)
    print(f'OK: {len(pages)} HTML pages; {references} local references; assets, anchors, form choices and metadata; base={base or "/"}.')

if __name__=='__main__':main()
