import os
from subprocess import call

root = "Topics"
root_html = "#HTML"
root_pdf = "/mnt/Stuff/Android/Documents/Geeks for Geeks"


def generate_pdf(src, dest):
    if dest:
        dest = os.path.join(root_pdf, dest)
    else:
        dest = os.path.join(root_pdf, src.replace(".html", ".pdf"))

    src = os.path.join(root_html, src)

    if not os.path.isfile(src) or os.path.isfile(dest):
        return

    title = os.path.basename(src)
    title = title[0:title.rfind(".")]

    command = [
        "/usr/bin/pandoc",
        "--template=template.tex",
        "--toc",
        "--latex-engine", "xelatex",
        "-V", "documentclass=report",
        # "-V", "title="+title,
        "-f", "html",
        src,
        "-o", dest,
    ]

    # print(" ".join(command))
    print(command[-1])
    call(command)

files = {
    "Stacks.html": "",
    "Queue.html": "",
    "Linked Lists.html": "",
    "Hashing.html": "",
    "Heaps.html": "",
    "Matrix.html": "",
    "Binary Search Trees.html": "",
    "Arrays.html": "",
    "Advanced Data Structures.html": "",
    "Binary Trees.html": "",
    "Graphs.html": "",
    "Analysis of Algorithms.html": "",
    "Backtracking.html": "",
    "Divide and Conquer.html": "",
    "Geometric Algorithms.html": "",
    "Greedy Algorithms.html": "",
    "Randomized Algorithms.html": "",
    "Strings and Pattern Searching.html": "",
    "Misc Algorithms.html": "",
    "Recursion.html": "",
    "Bit Algorithms.html": "",
    "Searching and Sorting.html": "",
    "Dynamic Programming.html": "",
    "Mathematical Algorithms.html": "",
    "Automata Theory.html": "GATE/Automata Theory.pdf",
    "Compilers.html": "GATE/Compilers.pdf",
    "Computer Networks.html": "GATE/Computer Networks.pdf",
    "Operating Systems.html": "GATE/Operating Systems.pdf",
    "Database Management Systems.html": "GATE/DBMS.pdf",
    "GATE Data Structures and Algorithms.html": "GATE/Data Structures and Algorithms.pdf",
    "Payu.html": "Interview/PayU.pdf",
}

# for file in os.listdir(root_html):
for file in files.items():
    generate_pdf(*file)
