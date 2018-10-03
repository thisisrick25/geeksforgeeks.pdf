
echo "Download links"

python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/greedy/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/bit-magic/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/divide-and-conquer/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/geometric/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/combinatorial/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/randomized/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/searching/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/sorting/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/recursion/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/analysis/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/game-theory/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/pattern-searching/
python3 list_links.py https://www.geeksforgeeks.org/category/algorithm/branch-and-bound/
python3 list_links.py https://www.geeksforgeeks.org/category/backtracking/
python3 list_links.py https://www.geeksforgeeks.org/tag/dynamic-programming/
python3 list_links.py https://www.geeksforgeeks.org/category/graph/
python3 list_links.py https://www.geeksforgeeks.org/category/tree/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/hash/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/matrix/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/heap/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/stack/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/queue/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/linked-list/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/c-strings/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/c-arrays/
python3 list_links.py https://www.geeksforgeeks.org/category/data-structures/binary-search-tree/

echo "You should now manually edit / clean the JSON files"

echo "Downloading HTML pages"

python3 download_html.py JSON/Analysis.json
python3 download_html.py JSON/Backtracking.json
python3 download_html.py JSON/Binary-Search-Tree.json
python3 download_html.py JSON/Bit-Magic.json
python3 download_html.py JSON/Branch-And-Bound.json
python3 download_html.py JSON/C-Arrays.json
python3 download_html.py JSON/C-Strings.json
python3 download_html.py JSON/Combinatorial.json
python3 download_html.py JSON/Divide-And-Conquer.json
python3 download_html.py JSON/Dynamic-Programming.json
python3 download_html.py JSON/Game-Theory.json
python3 download_html.py JSON/Geometric.json
python3 download_html.py JSON/Graph.json
python3 download_html.py JSON/Greedy.json
python3 download_html.py JSON/Hash.json
python3 download_html.py JSON/Heap.json
python3 download_html.py JSON/Linked-List.json
python3 download_html.py JSON/Matrix.json
python3 download_html.py JSON/Pattern-Searching.json
python3 download_html.py JSON/Queue.json
python3 download_html.py JSON/Randomized.json
python3 download_html.py JSON/Recursion.json
python3 download_html.py JSON/Searching.json
python3 download_html.py JSON/Sorting.json
python3 download_html.py JSON/Stack.json
python3 download_html.py JSON/Tree.json


echo "Converting HTML pages to PDF"

python3 html_to_pdf.py HTML/Analysis.html
python3 html_to_pdf.py HTML/Backtracking.html
python3 html_to_pdf.py HTML/Binary-Search-Tree.html
python3 html_to_pdf.py HTML/Bit-Magic.html
python3 html_to_pdf.py HTML/Branch-And-Bound.html
python3 html_to_pdf.py HTML/C-Arrays.html
python3 html_to_pdf.py HTML/C-Strings.html
python3 html_to_pdf.py HTML/Combinatorial.html
python3 html_to_pdf.py HTML/Divide-And-Conquer.html
python3 html_to_pdf.py HTML/Dynamic-Programming.html
python3 html_to_pdf.py HTML/Game-Theory.html
python3 html_to_pdf.py HTML/Geometric.html
python3 html_to_pdf.py HTML/Graph.html
python3 html_to_pdf.py HTML/Greedy.html
python3 html_to_pdf.py HTML/Hash.html
python3 html_to_pdf.py HTML/Heap.html
python3 html_to_pdf.py HTML/Linked-List.html
python3 html_to_pdf.py HTML/Matrix.html
python3 html_to_pdf.py HTML/Pattern-Searching.html
python3 html_to_pdf.py HTML/Queue.html
python3 html_to_pdf.py HTML/Randomized.html
python3 html_to_pdf.py HTML/Recursion.html
python3 html_to_pdf.py HTML/Searching.html
python3 html_to_pdf.py HTML/Sorting.html
python3 html_to_pdf.py HTML/Stack.html
python3 html_to_pdf.py HTML/Tree.html
