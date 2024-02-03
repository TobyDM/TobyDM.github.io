from yattag import Doc
from yattag import indent
import os
class content:
    def __init__(self, itemind):
        self.itemind = itemind
        self.headertext = ''
        self.subheadertext = ''
        self.bodytext = ''
        self.links = []
    def parsetext(self):
        inptext = open("./content/" + str(self.itemind) +"/text.txt", "r")
        self.headertext = inptext.readline()
        self.subheadertext = inptext.readline()
        self.bodytext = inptext.readline()
        self.links = inptext.readlines()

def pathitemcount(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        count+=1
    return count

numproj = pathitemcount('./content')


doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')
doc.asis('<html lang="en">')
with tag('html'):
    with tag('head'):
        doc.stag('meta', name = 'description', content = "Toby Moss Darci-Maher Portfolio")
        doc.stag('meta', charset = 'utf-8')
        doc.stag('meta', name = 'viewport', content = 'width=device-width, initial-scale=1')
        doc.stag('meta', name = 'author', content = "Toby Moss Darci-Maher")
        with tag('title'):
            text('Toby Moss Darci-Maher')
        doc.stag('link', rel = 'stylesheet', href = './makepretty.css')
        doc.stag('link', rel = 'icon', type = 'image/x-icon', href = './favicon.png')
    with tag('body'):
        with tag('div',('class','homepagebackground')):
            doc.stag('img',id = 'myimage', src = './background.png', alt = "background")
            with tag('div', ('class', 'wrapper')):
                with tag ('div',('class','mosslogo')):
                        doc.stag('img',id = 'myimage', src = './mosslogo.png', alt = "mosslogo")
                with tag('div',('class','homepage')):
                    with tag('h1'):
                        text("Toby Moss Darci-Maher Portfolio")
                    with tag('h4'):
                        for i in range(1, numproj):
                            contenti = content(i)
                            contenti.parsetext()
                            with tag('a',('href','./page' +str(i)+ '.html')):
                                text(contenti.headertext)
                            doc.asis('<br>')
html_document = indent(doc.getvalue(), indentation = '\t')
with open('index.html', 'w') as f:
    f.write(html_document)




for i in range(1, numproj):
    contenti = content(i)
    contenti.parsetext()
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    doc.asis('<html lang="en">')
    with tag('html'):
        with tag('head'):
            doc.stag('meta', name = 'description', content = "Toby Moss Darci-Maher Portfolio")
            doc.stag('meta', charset = 'utf-8')
            doc.stag('meta', name = 'viewport', content = 'width=device-width, initial-scale=1')
            doc.stag('meta', name = 'author', content = "Toby Moss Darci-Maher")
            with tag('title'):
                text('Toby Darci-Maher')
            doc.stag('link', rel = 'stylesheet', href = './makepretty.css')
            doc.stag('link', rel = 'icon', type = 'image/x-icon', href = './favicon.png')
        with tag('body'):
            with tag('div', ('class', 'wrapper')):
                # text and media columns
                with tag('div', ('class', 'page-main')):
                    with tag('div',('class','homebutton')):
                        with tag('a',('href','./index.html')):
                            doc.stag('img', src = './favicon.png', alt = 'icon')
                    with tag('div', ('class', 'detaildesc')):
                        text("hover for info")
                        with tag('span', ('class', 'hovertext')):
                            with tag('h2'):
                                text(contenti.headertext)
                            with tag('h3'):
                                text(contenti.subheadertext)
                            with tag('p'):
                                text(contenti.bodytext)
                            for linkandlabel in contenti.links:
                                label, link = linkandlabel.split(',')
                                with tag('p'):
                                    with tag('a',('href',link)):
                                        text(label)
                    with tag('div', ('class', 'detailmedia')):
                        numimg = pathitemcount('./content/' + str(i) + '/images')
                        doc.stag('img',id = 'myimage', src = './content/' + str(i) + '/images/img1.jpeg', alt = "image1")
                        if numimg>2:
                            with tag('div',('class','prevbutton')):
                                with tag('button',('type','button'),('onclick','previmage(' + str(i)+ ", " + str(numimg-1) + ')')):
                                    text(" < ")
                            with tag('div',('class','nextbutton')):
                                with tag('button',('type','button'),('onclick','nextimage(' + str(i)+ ", " + str(numimg-1) + ')')):
                                    text(" > ")
                            with tag('script',('src','./imagerotate.js')):
                                pass
    html_document = indent(doc.getvalue(), indentation = '\t')
    with open('page'+ str(i) + '.html', 'w') as f:
        f.write(html_document)
    i+=1
