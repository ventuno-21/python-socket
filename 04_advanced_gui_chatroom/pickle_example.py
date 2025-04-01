import pickle


unpickled_list = ["dill", "bread and butter", "hlaf sour"]
print(f"{unpickled_list} and type is = {type(unpickled_list)}")

# Try to encode a list using .encode()
# trial_list = unpickled_list.encode("utf-8")
## You can't encode it a 'list', becasue 'list' has no attribute encode,& encode is get use for 'string'
# print(f"{trial_list} and type is = {type(trial_list)}")


# Threfore lets encode it with pickling
# as the result come back , pickle will return 'byte' object, wich is we can use in SOCKET
pickled_list = pickle.dumps(unpickled_list)
print(f"{pickled_list} and type is = {type(pickled_list)}")
