Create dict from (key, value) tuples
====================================

When creating dictionary from input where same key can be mapped to multiple 
values it's useful to use dictionary's `setdefault` method.  
Let's say we have following input data:   
```
ITEMS = (('key1', 'val1'),
	 ('key1', 'val2'),
	 ('key2', 'val3'),
	 ('key1', 'val4'),
	 ('key2', 'val5'),
	)
```

Goal is to create following mapping  
```
{'key1': ['val1', 'val2', 'val4'], 'key2': ['val3', 'val5']}
```

One way to solve this is to create dictionary and check whether key was already
added. If key exists append value to list, otherwise add key with list with 
first element as the value for the newly create key.

```
ITEMS_DICT = {}
for k,v in ITEMS:
    if ITEMS_DICT.has_key(k):
        ITEMS_DICT[k].append(v)
    else:
        ITEMS_DICT[k] = [v]
```

Same can be achieved with far fewer lines using `setdefault` method:  

```
ITEMS_DICT = {}
for k,v in ITEMS:
    ITEMS_DICT.setdefault(k, []).append(v)
```

`setdefault` does `has_key()` check for you, creates new key . If key is in 
dictionary, it's value is returned; in this case `list`. That means we can use 
`append` or any other list method.  
The second parameter to this method is default value to be assigned to key. It 
defaults to `None`.  
