#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sudo pip install pysrt google-api-python-client
#


"""Udacity subtitle helper for zh_CN
"""

__author__ = 'yplam@yplam.com (Bruce Lam)'

import argparse
import httplib2
import pysrt
import os
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

config = {
    'proxy_host' : '127.0.0.1',
    'proxy_port' : 1080,
    'api_key' : 'your key here'
}

def translate(inputfile, outputfile):
  if config['proxy_host'] :
    proxy = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_SOCKS5, proxy_host=config['proxy_host'], proxy_port=config['proxy_port'])
    http = httplib2.Http(proxy_info = proxy)
  else:
    http = httplib2.Http()
    

  service = build('translate', 'v2',
            developerKey=config['api_key'], http=http)
  
  try:
    subs = pysrt.open(inputfile, encoding='utf-8')
    query = [subs[i].text for i in range(len(subs))]
    result = service.translations().list(
        source='en',
        target='zh_CN',
        q=query
      ).execute()
    for i in range(len(subs)):
      tmp_text = result[u'translations'][i][u'translatedText']
      tmp_text = tmp_text.replace(u'，', ' ')
      tmp_text = tmp_text.replace(u'。', ' ')
      tmp_text = tmp_text.replace(u'？', ' ?')
      tmp_text = tmp_text.replace(u'--', u'——')
      tmp_text = tmp_text.replace(u'-', u'——')
      tmp_text = tmp_text.replace(u'“', u' " ')
      tmp_text = tmp_text.replace(u'”', u' " ')
      subs[i].text = tmp_text + " <<<-- " +  subs[i].text + " -->>>"
    subs.save(outputfile, encoding='utf-8')
    print('Oops! Translate OK!')
  except HttpError:
    print('Oops! Google service error!')
    
def fix_format(inputfile, outputfile):
  subs = pysrt.open(inputfile, encoding='utf-8')
  for i in range(len(subs)):
    subs[i].text = re.sub(u"<<<--.*?-->>>", "", subs[i].text, flags=re.MULTILINE)
  subs.save(outputfile, encoding='utf-8')

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("command", help="sub command")
  parser.add_argument("input", help="the input file")
  parser.add_argument("-o", "--output", help="the output file")
  args = parser.parse_args()
  
  inputfile = args.input
  if args.output :
    outputfile = args.output
  else :
    outputfile = os.path.basename(inputfile)
  
  if args.command == 'translate' :
    translate(inputfile, outputfile)
  elif args.command == 'format' :
    fix_format(inputfile, outputfile)
           
if __name__ == '__main__':
  main()
