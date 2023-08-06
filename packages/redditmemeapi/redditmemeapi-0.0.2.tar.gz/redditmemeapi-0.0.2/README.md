# redditmemeapi

A pythonic API wrapper to fetch memes from https://meme-api.com

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install redditmemeapi
```

## Usage

```python
from redditmemeapi import gimme
# get a random meme from 'memes', 'dankmemes', 'me_irl' subreddits
print(gimme())

from redditmemeapi import gimmenum
# get specified number of memes
x = gimmenum(2) #max value 50
for i in x['memes']:
    print(i['url'])

from redditmemeapi import specifysub
# get memes from a specified subreddit
print(specifysub('okbuddyretard')) #max value 1

from redditmemeapi import subnum
# get specified number of memes from a specified subreddit
x = subnum('okbuddyretard',3) #max one sub, max 50 memes
for i in x['memes']
   print(i['url'])
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)