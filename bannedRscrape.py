from bs4 import BeautifulSoup
from requests import get
headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
# add urls to archiveUrls var 
archiveUrls = ['https://web.archive.org/web/20160612162812/reddit.com/r/uncensorednews']
# IGNORE TIME STAMPS, THEY'RE INACCURATE
info = {}
for i in archiveUrls:
    response = get(i, headers=headers)
    html = BeautifulSoup(response.text, 'html.parser')
    title = html.find_all('a', class_='title may-blank')
    author = html.find_all('p', class_='tagline')
    comments = html.find_all('li', class_='first')
    updoots = html.find_all('div', class_='score unvoted')
    for i in range(len(title)):
        postAuthor = author[i]
        postAuthor = postAuthor.text
        postTitle = title[i]
        postTitle = postTitle.text
        commentNum = comments[i]
        commentNum = commentNum.text
        postUpdoots = updoots[i]
        postUpdoots = postUpdoots.text
        i = str(i)
        info['Post ' + i] = [postTitle, postAuthor, commentNum, postUpdoots]


print('*' * 20)
print('Format: Post number, Post Title, Post Author, # of comments, # of upvotes')
print('*' * 20)

for k,v in info.items():
    print(k, v)
