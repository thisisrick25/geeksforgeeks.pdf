#!/usr/bin/env python3.6
import os
import sys

from subprocess import call

ROOT = "Topics"
ROOT_HTML = "HTML"
ROOT_PDF = "PDF"
ROOT_JSON = "JSON"


def generate_pdf(src, dst=""):
    if dst:
        dst = os.path.join(ROOT_PDF, dst)
    else:
        # dst = os.path.join(ROOT_PDF, src.replace(".html", ".tex"))
        dst = os.path.join(ROOT_PDF, src.replace(".html", ".pdf"))

    src = os.path.join(ROOT_HTML, src)

    # If source doesn't exist or destination already does
    if not os.path.isfile(src):
        print("Source HTML doesn't exist")
        return

    if os.path.isfile(dst):
        print("Destination PDF doesn't exist")
        return

    title = os.path.basename(src)
    title = title[0:title.rfind(".")]

    command = [
        "/usr/bin/pandoc",
        # "--template=template.tex",
        "--template=jgm.tex",
        "--toc",
        "--pdf-engine", "xelatex",
        "-V" "geometry:margin=1.5in",
        # "-V" "geometry:papersize=a3paper",
        "-V", "documentclass=report",
        "-V", "urlcolor=blue",
        "-V", "linkcolor=blue",
        # "-V", "title="+title,
        "-f", "html",
        src,
        "-o", dst,
    ]

    # print(" ".join(command))
    print(command[-1])
    call(command)


if __name__ == '__main__':

    # from _data import html_to_pdf_file_names
    # for file in html_to_pdf_file_names.items():
    #     generate_pdf(*file)

    TAG = sys.argv[1]
    generate_pdf("%s.html" % TAG)
