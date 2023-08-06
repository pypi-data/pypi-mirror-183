import os, sys
import shutil
import matplotlib.pyplot as plt
import numpy as np
import torch
import matplotlib

def get_rgba_from_cmap(cmap, val):
    cmap = matplotlib.cm.get_cmap(cmap)
    return np.asarray(cmap(val)).reshape(1,-1)

def get_device(gpu_id=-1):
    if gpu_id < 0:
        return torch.device('cpu')
    else:
        return torch.device(f'cuda:{gpu_id}')

def get_coloset_elem_dist(row, arr):
    assert len(arr.shape) == 2
    row = np.asarray(row)
    dist = np.sum((arr - row) ** 2, axis=1, keepdims=True)
    idx_min = dist.argmin(axis=0)[0]
    return dist[idx_min], idx_min

def get_row_index_in_arr(row, arr):
    assert len(arr.shape) == 2
    row = np.asarray(row)
    min_dist, min_dist_idx = get_coloset_elem_dist(row, arr)
    return min_dist_idx if min_dist < 1e-6 else False


def make_path_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def remove_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def remove_make_path(path):
    remove_path(path)
    os.makedirs(path)


def copy_move_file(source, target):
    shutil.copy(source, target)

def draw_confusion_matrix(y_pred, y_true):
    # https: // vitalflux.com / accuracy - precision - recall - f1 - score - python - example /
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

    conf_matrix = confusion_matrix(y_true=y_true, y_pred=y_pred)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(conf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')

    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('confusion_matrix.png')
    print('Num. of Obj.: %.3d' % len(y_true))
    print('Num. Pos./ Num. Neg.: {}/{}'.format(y_true.count(1), y_true.count(0)))
    print('Precision: %.3f' % precision_score(y_true, y_pred))
    print('Recall: %.3f' % recall_score(y_true, y_pred))
    print('Accuracy: %.3f' % accuracy_score(y_true, y_pred))
    print('F1 Score: %.3f' % f1_score(y_true, y_pred))

