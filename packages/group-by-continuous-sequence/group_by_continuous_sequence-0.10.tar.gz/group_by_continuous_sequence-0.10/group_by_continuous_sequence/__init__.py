import operator
from functools import reduce
from collections import defaultdict
import pandas as pd
import numpy as np
from flatten_everything import flatten_everything, ProtectedList
from intersection_grouper import group_lists_with_intersections


def groupBy(key, seq):
    # https://stackoverflow.com/a/60282640/15096247
    return reduce(
        lambda grp, val: grp[key(val)].append(val) or grp, seq, defaultdict(list)
    )


def group_sequence_in_iter(iterable, difference=1):
    ordering = lambda x: x
    resu = []
    for k in groupBy(
        lambda x: difference * x[0] - ordering(x[1]), enumerate(iterable)
    ).items():
        resu.append(k)

    return resu


def search_sequence_numpy(arr, seq):
    # https://stackoverflow.com/questions/36522220/searching-a-sequence-in-a-numpy-array
    # Store sizes of input array and sequence
    Na, Nseq = arr.size, seq.size
    # Range of sequence
    r_seq = np.arange(Nseq)
    # Create a 2D array of sliding indices across the entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    M = (arr[np.arange(Na - Nseq + 1)[:, None] + r_seq] == seq).all(1)
    # Get the range of those indices as final output
    if M.any() > 0:
        return np.where(np.convolve(M, np.ones((Nseq), dtype=int)) > 0)[0]
    else:
        return []  # No match found


def check_if_in_one_line(x):
    try:
        return len(np.unique(x[0][..., -2])) == 1
    except Exception:
        return True


def find_sequence_in_np_array(arr, seq):
    if not isinstance(seq, np.ndarray):
        seq = np.asarray(seq)
    sq = search_sequence_numpy(arr.flatten(), seq=seq)
    grp = search_sequence_in_list(
        sq, difference=1, return_index=False, return_values=True
    )
    nparrayrblack_ = np.zeros(arr.shape, dtype=np.uint0).flatten()
    allcoords = []
    for nparrayr in grp:
        nparrayrblack = nparrayrblack_.copy()
        nparrayrblack[nparrayr] = 1
        nparrayrblack2 = nparrayrblack.reshape(arr.shape)
        allresus = np.nonzero(nparrayrblack2)
        coo = np.array(allresus).T
        allcoords.append(coo.copy())
    allcoordsfinal = [
        (bb, [reduce(operator.getitem, cc, arr) for cc in bb]) for bb in allcoords
    ]
    allcoordsfinal2 = [
        {
            "inoneline": check_if_in_one_line(x) if len(x[0].shape) > 1 else True,
            "location": x[0],
            "values": x[1],
        }
        for x in allcoordsfinal
    ]
    return allcoordsfinal2


def _sort1(k):
    listbig = []
    allreadydone = []
    for kk in k:
        if len(kk[1]) > 1:
            templist = [ProtectedList()]
            for i, j in zip(kk[1], kk[1][1:]):
                if abs(i[0] - j[0]) == 1:
                    if i not in allreadydone:
                        templist[-1].append(i)
                        allreadydone.append(i)
                    if j not in allreadydone:
                        templist[-1].append(j)
                        allreadydone.append(j)

                else:
                    if i not in allreadydone:
                        templist[-1].append(i)
                        allreadydone.append(i)
                    templist.append(ProtectedList())

                    if j not in allreadydone:
                        templist[-1].append(j)
                        allreadydone.append(j)
            listbig.append(templist.copy())
        else:
            listbig.append(ProtectedList(tuple(kk[1][0])))
    return listbig


def _get_values_from_one_search(iterable, difference):
    k = group_sequence_in_iter(iterable, difference=difference)
    listbig = _sort1(k)
    df = pd.Series([list(flatten_everything(u)) for u in listbig]).explode()
    df = df.loc[df.apply(len) > 0]
    df = df.apply(
        lambda x: list(sorted(frozenset(x))) if isinstance(x[0], tuple) else tuple(x)
    )
    df = df.to_frame()
    df[1] = df[0].apply(lambda x: tuple(flatten_everything(x))[0])
    df = df.sort_values(by=1)
    df = df.reset_index(drop=True)
    df[0] = df[0].apply(lambda x: [x] if isinstance(x, tuple) else x)

    return df


def merge_repeating_values_with_sequence(df, df1):
    df1 = df1.explode(0).reset_index(drop=True)
    df = df.explode(0).reset_index(drop=True)
    df3 = pd.merge_asof(df, df1, left_on=1, right_on=1)
    df4 = pd.merge_asof(df1, df, left_on=1, right_on=1)
    df5 = pd.merge_asof(df4, df3, left_on=1, right_on=1)
    alli = []
    for key, item in df5.iterrows():
        sv = item["0_x_x"]
        erg = df5.loc[
            (df5["0_x_x"] == sv)
            | (df5["0_y_x"] == sv)
            | (df5["0_x_y"] == sv)
            | (df5["0_y_y"] == sv),
            ["0_x_x", "0_y_x", "0_x_y", "0_y_y"],
        ].__array__()
        alli.append((frozenset(erg.flatten().tolist())))
    alli = group_lists_with_intersections(alli, keep_duplicates=False)

    od = {}
    for __ in alli:
        s1 = tuple(sorted(__, key=lambda x: x[0]))
        od[s1[0][0]] = s1

    return sorted(od.items(), key=lambda x: x[0], reverse=False)


def search_sequence_in_list(
    iterable, difference, return_index=True, return_values=True
):
    df = _get_values_from_one_search(iterable, difference=difference)
    bei = df[0].to_list()
    if return_index and return_values:
        return bei
    if return_index:
        return [[y[0] for y in x] for x in bei]
    if return_values:
        return [[y[1] for y in x] for x in bei]


def search_sequence_in_list_with_repeated_numbers(
    iterable,
    difference,
    return_index=True,
    return_values=True,
    ignore_only_repeated=True,
):
    df1 = _get_values_from_one_search(iterable, difference=difference)
    df = _get_values_from_one_search(iterable, difference=0)
    fd = merge_repeating_values_with_sequence(df, df1)
    bei = [x[1] for x in fd]
    if ignore_only_repeated:
        bei = (
            pd.DataFrame(
                [
                    (([x],),) if len(np.unique([y[1] for y in x])) > 1 else [(x,)]
                    for x in bei
                ]
            )
            .explode(0)[0]
            .to_list()
        )
        try:
            bei = [x[0] if isinstance(x, (list, tuple, set)) else x for x in bei]
            bei = [
                (x,) if isinstance(x, tuple) and isinstance(x[0], int) else x
                for x in bei
            ]
        except Exception as bi:
            return []
    if return_index and return_values:
        return bei
    if return_index:
        try:
            return [[y[0] for y in xx] for xx in bei]
        except Exception as o:
            return []
    if return_values:
        try:
            return [[y[1] for y in xx] for xx in bei]
        except Exception as v:

            return []
