from props import reader


def read(s, nl=True):
    s = '\n' + s if nl else s
    reader.labels[0].text += s
