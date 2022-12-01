import pickle
with open('localisation.bin', 'rb') as bf:
    dct = pickle.load(bf)
    print(dct['Responce_await_login_expected'])