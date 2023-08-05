<h1>ProcDump memory dump to Pandas DataFrame</h1>

```python

# Download ProcDump: https://learn.microsoft.com/pt-br/sysinternals/downloads/procdump
# I had to make some changes to winappdbg
# If you get an Exception, download https://github.com/hansalemaos/a_pandas_ex_memorydump_to_df/blob/main/winappdbg.zip
# and overwrite all files in Lib\site-packages\winappdbg

$pip install a-pandas-ex-memorydump-to-df

import pandas as pd
from a_pandas_ex_memorydump_to_df import pd_add_memorydf
pd_add_memorydf()

df = pd.Q_df_from_memory(
    pid=9132, procdumppath=r"C:\Program Files\procdump.exe", with_utf8_bytes=False
)  # with_utf8_bytes=True takes much more time!


The method will convert all bytes to every possible format which means, the DataFrame 
might get huge. 



# Notepad.exe
#       aa_address1_hex aa_address2_hex  ...  aa_ascii_int_63  aa_ascii_int_66
# 0            00000000        00010000  ...               46               46
# 1            00000000        00010010  ...               46               46
# 2            00000000        00010020  ...               46               46
# 3            00000000        00010030  ...               46               46
# 4            00000000        00010040  ...               46               46
#                ...             ...  ...              ...              ...
# 64014        00007ff5        fffb0fc0  ...               46               46
# 64015        00007ff5        fffb0fd0  ...               46               46
# 64016        00007ff5        fffb0fe0  ...               46               46
# 64017        00007ff5        fffb0ff0  ...               46               46
# 64018        00007ff5        fffb1000  ...                0                0
# [64019 rows x 304 columns]

# df.size
# Out[16]: 19461776

# explorer.exe
# df
# Out[10]:
#         aa_address1_hex aa_address2_hex  ...  aa_ascii_int_63  aa_ascii_int_66
# 0              00000000        00010000  ...               46               46
# 1              00000000        00010010  ...               46               46
# 2              00000000        00010020  ...               46               46
# 3              00000000        00010030  ...               46               46
# 4              00000000        00010040  ...               46               46
#                  ...             ...  ...              ...              ...
# 3234712        00007ff5        fffb0fc0  ...               46               46
# 3234713        00007ff5        fffb0fd0  ...               46               46
# 3234714        00007ff5        fffb0fe0  ...               46               46
# 3234715        00007ff5        fffb0ff0  ...               46               46
# 3234716        00007ff5        fffb1000  ...                0                0
#
# [3234717 rows x 304 columns]
#
# df.size
# Out[11]: 983353968

# Location of the temp file (procdump)
# df.tmp_file_path
# Out[14]: 'C:\\Users\\Gamer\\AppData\\Local\\Temp\\tmpsypcc1g5.dmp'
# df.tmp_delete_file()  $ file must be closed before

```

### Let's compare the converted values with the ones from CheatEngine

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000001.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000002.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000003.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000004.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000005.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000006.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000007.png" alt="">

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/debugdf/debugdf_00000008.png" alt="">