"""
d = {
 'a': 5,
 'b': 6,
 'c': {
   'f': 9,
   'g': {
     'm': 17,
     'n': 3
   }
 }
}

flatten(d) = {
 'a': 5,
 'b': 6,
 'c.f': 9,
 'c.g.m': 17,
 'c.g.n': 3,
}

def flatten(d):
""" Takes a dictionary and if any values are a dictionary, flatten that
and return a dictionary object"""

    flatten_dict={}
    for key,val in d.iteritems():
        if isinstance(val, dict):
            for nested_key,nested_val in flatten(val).iteritems():
                flatten_dict[key+'.'+nested_key]=nested_val
        else:
            flatten_dict[key]=val
    return flatten_dict

print flatten(d)
