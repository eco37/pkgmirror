#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
#
# FreeBSD Repos: http://pkg.freebsd.org/


import requests
import urlparse
import argparse
import errno
import os, re

def download_file(url, path):
    
    data = requests.get(url)
    open(path, 'wb').write(data.content)


def mkdir(path):

    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            print "Error: " + e.errno
            return False

    return True


def crawler(url, base_path, verbose):
    
    code = requests.get(url)
    plain = code.text
    
    link_regex = 'href="(.*?)"'
    hits = re.findall(link_regex, plain)

    for row in hits:
        if row.find('?') >= 0 or row.find('../') >= 0:
            continue

        url_file = url + '/' + row       
        store_dir = base_path + '/' + urlparse.urlparse(url).path
        
        if row.find('/') >= 0:
            if mkdir(store_dir + '/' + row) == False:
                return;
            
            crawler(url_file, base_path, verbose)
        else:
            store_path = store_dir + '/' + row

            if verbose:
                print url_file + " -> " + store_path
            download_file(url_file, store_path)


def argparser():
    
    parser = argparse.ArgumentParser(description='pkgmirror is a tool to download and mirror a FreeBSD pkg repo webserver. Select one of the repo/paths that can be found here: http://pkg.freebsd.org/')
    
    parser.add_argument('url', action="store", help='URL to a FreeBSD pkg repo')
    parser.add_argument('path', action="store", help='Output directory')
    parser.add_argument('-v', action = 'store_true', default = False,
                        dest='verbose',
                        help='Prints verbose information')

    return parser.parse_args()


if __name__ == "__main__":
    results = argparser()

    dirname = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.join(dirname, results.path)

    print "Repo URL: " + results.url
    print "Output Path: " + abs_path

    crawler(results.url, abs_path, results.verbose)

