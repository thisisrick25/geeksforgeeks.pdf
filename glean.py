"""Use boilerpipy + LXML to clean downloaded html files."""

import sys
import logging

import lxml.etree
import lxml.html as html

from boilerpipy import Extractor


def clean(content):
    head_pos = content.find('<head>')

    # insert the encoding of the file
    content = (
        content[:head_pos + 6] +
        '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">' +
        content[head_pos + 6:]
    )

    article = Extractor(content, loglevel=logging.INFO).extracted()
    if article is None:
        print("Error processing html file.")
        sys.exit(1)

    # Replace
    lang_replace = {
        '<h1 class="tabtitle">C++</h1>': '<p><strong>C++</strong></p>',
        '<h1 class="tabtitle">C</h1>': '<p><strong>C</strong></p>',
        '<h1 class="tabtitle">C/C++</h1>': '<p><strong>C/C++</strong></p>',
        '<h1 class="tabtitle">Java</h1>': '<p><strong>Java</strong></p>',
        '<h1 class="tabtitle">Python</h1>': '<p><strong>Python</strong></p>',
    }

    for to, frm in lang_replace.items():
        article = article.replace(to, frm)

    html_parser = html.HTMLParser(encoding="utf-8")
    html_doc = html.fromstring(content, parser=html_parser)

    # if the title is unfortunately removed by boilerpipy, then add it back in
    title = html_doc.find('.//title').text_content()
    if "h2" not in article:
        article = "<h1>" + title[:title.rfind('-')] + "</h1>" + article

    reconstructed_body = (
        "<html><body>" +
        article .replace("<h2", "<h1") .replace("</h2>", "</h1>") +
        "</body></html>"
    )

    if "<body><h1>" not in reconstructed_body:
        reconstructed_body = reconstructed_body.replace(
            "<body>", "<body><h1>" + title[:title.rfind('-')] + "</h1>")

    # further remove useless stuff
    body_doc = html.fromstring(reconstructed_body).find('body')

    bad_tags = (
        body_doc.xpath("//button") +
        body_doc.xpath("//nav") +
        body_doc.xpath("//footer") +
        body_doc.xpath("//div[@id='personalNoteDiv']") +
        body_doc.xpath("//div[@class='comments-main']") +
        body_doc.xpath("//ins[@class='adsbygoogle']") +
        body_doc.xpath("//h3")
    )

    for tag in bad_tags:
        tag.getparent().remove(tag)

    for pre_tag in body_doc.xpath("//pre"):
        if 'class' in pre_tag.attrib:
            pre_tag.attrib.pop('class')
        if 'title' in pre_tag.attrib:
            pre_tag.attrib.pop('title')

    head_doc = html_doc.find('head')
    src_url = head_doc.cssselect('meta[property="og:url"]')[0].get('content')
    src_link = "<p><a href='" + src_url + "' rel='tag'>" + src_url + "</a></p>"

    src_header_string = "<h3>Source</h3>"
    post_content_doc = body_doc.xpath("//div[@class='entry-content']")[0]
    post_content_doc.append(lxml.etree.XML(src_header_string))
    post_content_doc.append(lxml.etree.XML(src_link))
    result = html.tostring(body_doc)

    # replace <code> with <code><pre> for styling later.
    result = (
        result
        .replace('<pre>', '<pre> <code>')
        .replace('</pre>', '</code> </pre>')
    )

    return result
