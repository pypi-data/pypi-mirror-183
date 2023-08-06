from __future__ import print_function
from scription import *
from antipathy import Path
from . import Document


@Command(
        source=Spec('name of source file to convert', type=Path),
        target=Spec('name of output file [default: source base name with .html extension]', default='', type=Path),
        header_sizes=Spec('sizes for the three header categories', MULTI, abbrev='sizes', force_default=(1,2,3)),
        header_title=Spec('make first header a title', FLAG, abbrev='title'),
        css=Spec('use specified css file instead of default css settings', OPTION, force_default='stonemark.css'),
        fragment=Spec('do not include <body>, css, etc., in target file', FLAG),
        )
def stonemark(source, target, header_sizes, header_title, css, fragment):
    if not source.exists():
        abort("'%s' does not exist" % source)
    if target == '':
        target = source.strip_ext() + '.html'
    elif target.isdir():
        target += source.filename.strip_ext() + '.html'
    with open(source) as f:
        text = f.read()
    doc = Document(text, header_sizes=header_sizes, first_header_is_title=header_title)
    page = []
    if not fragment:
        page.append(html_page_head)
        if doc.title:
            page.append(html_page_title % doc.title)
        page.append(html_page_css % css)
        page.append(html_page_body)
    page.append(doc.to_html())
    if not fragment:
        page.append(html_page_post)
    with open(target, 'w') as f:
        f.write('\n'.join(page).strip())

html_page_head = '''\
<!doctype html>
<html>
<head>
    <meta charset="UTF-8"/>'''

html_page_title = '    <title>%s</title>'
html_page_css =   '    <link rel="stylesheet" type="text/css" href="./%s"/>'

html_page_body = '''\
</head>
<body>'''

html_page_post = '''\
</body>
</html>'''

css = '''\
@charset "utf-8";
/*
 *  portions adapted from:
 *  - Chris Coyier [https://css-tricks.com/snippets/css/simple-and-nice-blockquote-styling/]
 *  - Dom (dcode) at [https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l]
 *  - [https://css-tricks.com/styling-code-in-and-out-of-blocks/]
 */

table {
    border-collapse: collapse;
    margin: 10px 0;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

table th {
  text-align: left;
  min-width: 150px;
  background-color: #f3f3f3;
  border-bottom: thin black solid;
}

table th:first-child {
  text-align: left;
}

table td {
  padding: 7px 25px 7px 0px;
  margin: 5px;
  text-align: left;
}

tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

tbody tr.active-row {
    font-weight: bold;
    color: #009879;
}

select {
  max-width: 225px;
}

blockquote {
  background: #f9f9f9;
  border-left: 10px solid #ccc;
  margin: 1.5em 10px;
  padding: 0.5em 10px;
  quotes: "\201C""\201D""\2018""\2019";
}

blockquote:before {
  color: #ccc;
  content: open-quote;
  font-size: 4em;
  line-height: 0.1em;
  margin-right: 0.25em;
  vertical-align: -0.4em;
}

blockquote p {
  display: inline;
}

/* For all <code> */
code {
  font-family: monospace;
  font-size: inherit;
  background: #efefff;
}

/* Code in text */
p > code,
li > code,
dd > code,
td > code {
  word-wrap: break-word;
  box-decoration-break: clone;
  padding: .1rem .3rem .2rem;
  border-radius: .75rem;
}

h1 > code,
h2 > code,
h3 > code,
h4 > code,
h5 > code {
  padding: .0rem .2rem;
  border-radius: .5rem;
  background: inherit;
  border: thin black solid;
}

pre code {
  display: block;
  white-space: pre;
  -webkit-overflow-scrolling: touch;
  overflow-x: scroll;
  max-width: 100%;
  min-width: 100px;
  padding: 10px;
  border: thin black solid;
  border-radius: .2rem;
}

sup {
  padding: 0px 3px;
  }

.footnote {
  padding: 5px 0px;
  }

*
ol,
ul {
    padding: 0px 15px;
}

li {
  padding: 2px;
}

h1 {
    display: block;
    font-size: 2em;
    margin-top: 0.25em;
    margin-bottom: 0em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold
}

h2 {
    display: block;
    font-size: 1.5em;
    margin-top: 1.25em;
    margin-bottom: 0em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
}

h3 {
    display: block;
    font-size: 1.25;
    margin-top: 1.25em;
    margin-bottom: 0em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
}

h4 {
    display: block;
    font-size: 1.0em;
    margin-top: 1.25em;
    margin-bottom: 0em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
    font-style: italic;
}


'''

Run()
