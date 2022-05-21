import pickle
import os

cwd = os.getcwd()
storage = os.path.join(cwd, 'storage')
save_1 = os.path.join(storage, 'save_1.dat')


blank_game_data = {
    'rickrolls': 0,
    'rickrolls_per_click': 1
}

# Saving
def save(**kwargs):
    with open(save_1, 'wb') as f:
        pickle.dump(kwargs, f, protocol=2)

# loading
def load():
    with open(save_1, 'rb') as f:
        return pickle.load(f)

def clear_save():
    with open(save_1, 'wb') as f:
        pickle.dump(blank_game_data, f, protocol=2)