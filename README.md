# ToyUID
UUID alternative with an overkill algorithm.

Generate an Unique Identifier, based on computer's informations, timestamp and lot of very random things.

ADVERT : I've never done statistic on the uniqueness of the algorithm. Please use carefully.

##Usage

```python

    >>> from ToyUID import ToyUID
    
    >>> id = ToyUID()
    
    >>> id.normalized
    
    'TOYUID-29e9-d79a-2ea4-4b61-1126-554f-be85-5c2f-c584-fc08-c5c3-7549-8a6b-bc3e-2776-975e-df2e-55bc'
    
```

### API

``ToyUID()`` :  Basic class of the module.

``self.str`` :  Get UID in a not-normalized *String*. You can use ``str(self)`` too.

``self.int`` :  Get UID in *Int* object. You can use ``int(self)`` too.

``self.bytes`` :  Get UID in *Bytes*. You can use ``bytes(self)`` too.

``self.normalized`` :  Get UID in a normalized *String*.

