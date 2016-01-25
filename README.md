# ToyUID
UUID alternative with an overkill algorithm.

Generate an Unique Identifier, based on computer's informations and power, timestamp, random hash and lot of very random things.
It's a toy because i don't know if it's very unique but i think it is.

##Usage

```python
    >>> from ToyUID import ToyUID
    >>> id = ToyUID()
    >>> id.str
    '566fb04d5bfd3dea0f7c40893fb9dcb5e29'
    >>> id.algorithm
    'SHA1'
```

As you can see, it's very easy to use. Is there lot of things to change but it work nice.
