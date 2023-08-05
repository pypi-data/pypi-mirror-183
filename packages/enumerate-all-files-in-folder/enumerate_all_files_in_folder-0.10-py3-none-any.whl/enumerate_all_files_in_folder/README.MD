<h2>A function that enumerates all files in a folder (and subfolders)</h2>


```python
$pip install enumerate-all-files-in-folder

```


<h3>Original</h3>
<img src="https://github.com/hansalemaos/screenshots/raw/main/enumeratefiles/original.png"/>



```python

from enumerate_all_files_in_folder import copy_enumerate_files
alli = copy_enumerate_files(
    folders=[r"F:\flattest"],
    outputfolder=r"F:\flattestresult1",
    maxsubdirs=0,
    groupsuffix=True,
    restart_index_new_suffix=True,
    zfill=8,
    prefix = '1test_'
)
```


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/enumeratefiles/2022-12-26 20_22_11-flattestresult1.png"/>



```python
alli = copy_enumerate_files(
    folders=[r"F:\flattest"],
    outputfolder=r"F:\flattestresult2",
    maxsubdirs=0,
    groupsuffix=False,
    restart_index_new_suffix=False,
    zfill=8, prefix='2test_'

)

```


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/enumeratefiles/2022-12-26 20_16_51-flattestresult2.png"/>



```python

alli = copy_enumerate_files(
    folders=[r"F:\flattest"],
    outputfolder=r"F:\flattestresult3",
    maxsubdirs=0,
    groupsuffix=True,
    restart_index_new_suffix=False,
    zfill=8, prefix='3test_'

)

```


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/enumeratefiles/2022-12-26 20_16_00-flattestresult3.png"/>


