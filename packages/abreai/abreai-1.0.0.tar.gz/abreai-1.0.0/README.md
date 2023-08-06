# Install
**Pypi**
```
pip install abreai
```

**GitHub**
```
pip install git+https://github.com/1Marcuth/encurtanet-py.git
```

# Simple use example
```py
from abreai import AbreAi

shortener = AbreAi()

url_info = shortener.shorten(
    url="https://google.com", # Your url
    alias="goggle84778448679dasdadsdasdasdasdsadasdasafs" # Alias of the url
)
shortened_url = url_info.get_shortened_url()

print(url_info.get_shortened_url())
```