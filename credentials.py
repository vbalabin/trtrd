def load_obj(path):
    import pickle
    from collections import namedtuple

    ApiCred = namedtuple("ApiCred", ("api_key", "secret_key"))
    with open(path, 'rb') as input:
        d = pickle.load(input)

    res = ApiCred(d["api_key"], d["secret_key"])
    return res
    

config = load_obj("E:/Books/archive/hm/ssky.api")
