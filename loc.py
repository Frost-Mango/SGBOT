import pickle
import config
def __dump_localisation():
    dt = {}
    with open(config.LOCALIZATION_TEXT, 'r', encoding='utf_8') as rf:
        rs = rf.readline().rstrip()
        while rs != '':
            if rs[0] == '#':
                rs = rf.readline().rstrip()
                continue
            lk, tx = rs.split(':0')
            rs = rf.readline().rstrip()
            dt[lk] = tx
    return dt

try:
    with open(config.LOCALIZATION_DICTIONARY, 'rb') as rf:
        dct = pickle.load(rf)
except FileNotFoundError:
    dct = {}

def __main():
    dct_addition = __dump_localisation()

    for lk in dct_addition:
        dct[lk] = dct_addition[lk]
    with open(config.LOCALIZATION_DICTIONARY, 'wb') as wf:
        pickle.dump(dct, wf)

def update_localisation_json():
    __main()

if __name__ == "__main__":
    print("sucess")
    __main()