import os
import pathlib
from flatten_everything import flatten_everything
from more_itertools import chunked
from FastCopyFast import copyfile
from functools import reduce
from collections import defaultdict

from touchtouch import touch


def groupBy(key, seq):
    # https://stackoverflow.com/a/60282640/15096247
    return reduce(
        lambda grp, val: grp[key(val)].append(val) or grp, seq, defaultdict(list)
    )


def copy_enumerate_files(
    folders,
    outputfolder,
    maxsubdirs=1,
    groupsuffix=True,
    restart_index_new_suffix=True,
    zfill=8,
        prefix = ''
):
    if not isinstance(folders, list):
        folders = [folders]
    all_results = {}

    mainfi = []
    for rootdir in folders:

        allfi = []
        baselevel = len(rootdir.split(os.path.sep))
        for subdirs, dirs, files in os.walk(rootdir):
            curlevel = len(subdirs.split(os.path.sep))
            if curlevel <= baselevel + maxsubdirs:
                allfi.append([os.path.join(subdirs, k) for k in files])

        mainfi.extend([(os.path.join(rootdir, x)) for x in (flatten_everything(allfi))])
    filesto = mainfi
    filesto_ = {}
    for ini, f in enumerate(filesto):
        suffi = pathlib.Path(f).suffix
        filesto_[ini] = {
            "old": f,
            "new": outputfolder,
            "suffix": str(suffi),
        }
        if not groupsuffix:
            nfi = os.path.join(outputfolder, prefix + str(ini).zfill(zfill) + str(suffi))
            touch(nfi)
            try:
                copyfile(f, nfi, copystat=False)
                all_results[f] = nfi
            except Exception as fe:
                print(fe)
                continue

    if not groupsuffix:
        return all_results

    result = {
        key: tuple(flatten_everything(values))
        for key, values in groupBy(
            lambda pair: pair[1]["suffix"], filesto_.items()
        ).items()
    }
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
    counter = 0
    for i in result.items():
        k = i[-1]

        for c, d in zip(g := list(chunked(k, 4)), range(len(g))):
            filenow = c[1]
            if restart_index_new_suffix:
                newfile = os.path.join(c[2], prefix + str(d).zfill(zfill) + c[3])
            else:
                newfile = os.path.join(c[2], prefix + str(counter).zfill(zfill) + c[3])

            try:
                touch(newfile)
                copyfile(filenow, newfile, copystat=False)
                all_results[filenow] = newfile

                counter += 1
            except Exception as fe:
                print(fe)
                continue
    return all_results

