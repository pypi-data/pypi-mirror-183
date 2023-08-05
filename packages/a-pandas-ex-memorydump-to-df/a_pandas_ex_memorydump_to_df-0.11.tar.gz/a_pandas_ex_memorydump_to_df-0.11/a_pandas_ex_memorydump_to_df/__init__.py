import os
import tempfile
from functools import partial
from pandas.core.frame import DataFrame
import pykd
import pandas as pd
import numpy as np
from PyPDump import ProcDump
from flatten_everything import flatten_everything
from winappdbg import win32, Process, HexDump

int_array = np.frompyfunc(int, 2, 1)
from touchtouch import touch

DataFrame.tmp_file_path = None
DataFrame.tmp_delete_file = None

splitlist_all = [
    8,
    9,
    17,
    18,
    19,
    21,
    22,
    24,
    25,
    27,
    28,
    30,
    31,
    33,
    34,
    36,
    37,
    39,
    40,
    42,
    43,
    45,
    46,
    48,
    49,
    51,
    52,
    54,
    55,
    57,
    58,
    60,
    61,
    63,
    64,
    66,
    67,
    68,
]

filterarray = np.array(
    [
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        97,
        98,
        99,
        100,
        101,
        102,
        65,
        66,
        67,
        68,
        69,
        70,
    ],
    dtype=np.uint8,
)


def get_tmpfile(suffix=".bin"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = filename.replace("/", os.sep).replace("\\", os.sep)
    tfp.close()
    return filename, partial(os.remove, tfp.name)


def replace_hex_with_real_numbers(onebytearray):
    condlist = [
        onebytearray == filterarray[0],
        onebytearray == filterarray[1],
        onebytearray == filterarray[2],
        onebytearray == filterarray[3],
        onebytearray == filterarray[4],
        onebytearray == filterarray[5],
        onebytearray == filterarray[6],
        onebytearray == filterarray[7],
        onebytearray == filterarray[8],
        onebytearray == filterarray[9],
        onebytearray == filterarray[10] | filterarray[16],
        onebytearray == filterarray[11] | filterarray[17],
        onebytearray == filterarray[12] | filterarray[18],
        onebytearray == filterarray[13] | filterarray[19],
        onebytearray == filterarray[14] | filterarray[20],
        onebytearray == filterarray[15] | filterarray[21],
    ]
    choicelist = np.array(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        dtype=np.uint8,
    )
    stan_val = np.uint8(0)
    bytevaluesarray = np.select(condlist, choicelist, stan_val)
    return bytevaluesarray


def splitarray(arr, splitlist_all):
    binarray = arr.view(("V", 1)).reshape(len(arr), -1)
    intarray = binarray.view(np.uint8)
    nparray = replace_hex_with_real_numbers(intarray)
    gesch = np.split(nparray.T, splitlist_all)
    gesch2 = np.split(binarray.T, splitlist_all)
    indexlist = splitlist_all.copy()
    indexlist.append(len(arr[0]))
    splittetresultsdict = {}
    splittetresultsdict_bytes = {}
    for ge, ge2, wholele in zip(gesch, gesch2, indexlist):
        splittetresultsdict[wholele] = ge.T.copy()
        splittetresultsdict_bytes[wholele] = ge2.T.copy()
    return splittetresultsdict, splittetresultsdict_bytes


def yield_utf(bytedict):
    alsstringut = bytedict.flatten().tobytes().decode("utf-8", "replace")
    looping = len(alsstringut) // 16
    for x in range(looping):
        yield alsstringut[x * 16 : 16 * x + 16]


def yield_utf_numbers(bytedict):
    alsstringut = bytearray(bytedict.flatten().tobytes())
    looping = len(alsstringut) // 16
    for x in range(looping):
        yield alsstringut[x * 16 : 16 * x + 16]


def get_dataframe(
    addressrange="00000000`06000000 00000000`07000000", with_utf8_bytes=False
):
    lmsm = pykd.dbgCommand(f"db {addressrange}")
    arr = np.array([ba for ba in flatten_everything(lmsm.splitlines())], dtype="S")
    splittetresultsdict, splittetresultsdict_bytes = splitarray(arr, splitlist_all)

    allindexchar = [21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66]

    allfields = {}
    allfields["aa_address1_hex"] = (
        splittetresultsdict_bytes[8].flatten().view("S8").astype("U").flatten()
    )
    allfields["aa_address2_hex"] = (
        splittetresultsdict_bytes[17].flatten().view("S8").astype("U").flatten()
    )
    allfields["aa_address1_int"] = int_array(allfields["aa_address1_hex"], 16).astype(
        np.uint64
    )
    allfields["aa_address2_int"] = int_array(allfields["aa_address2_hex"], 16).astype(
        np.uint64
    )

    for indichar in allindexchar:
        uni0_0_00 = np.ascontiguousarray(splittetresultsdict[indichar][..., 0])
        uni0_1_00 = np.ascontiguousarray(splittetresultsdict[indichar][..., 1])
        uni1_0_04 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint8
            ),
            4,
        )  # onebyte
        uni2_0_12 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint16
            ),
            12,
        )  # 2 bytes
        uni2_1_08 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint16
            ),
            8,
        )  # 2 bytes
        uni4_0_20 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint32
            ),
            20,
        )  # 4 bytes
        uni4_0_28 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint32
            ),
            28,
        )  # 4 bytes
        uni4_1_16 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint32
            ),
            16,
        )  # 4 bytes
        uni4_1_24 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint32
            ),
            24,
        )  # 4 bytes
        uni8_0_36 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint64
            ),
            36,
        )  # 8 bytes
        uni8_0_44 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint64
            ),
            44,
        )  # 8 bytes
        uni8_0_52 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint64
            ),
            52,
        )  # 8 bytes
        uni8_0_58 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 0]).astype(
                np.uint64
            ),
            58,
        )  # 8 bytes
        uni8_1_32 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint64
            ),
            32,
        )  # 8 bytes
        uni8_1_40 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint64
            ),
            40,
        )  # 8 bytes
        uni8_1_48 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint64
            ),
            48,
        )  # 8 bytes
        uni8_1_56 = np.left_shift(
            np.ascontiguousarray(splittetresultsdict[indichar][..., 1]).astype(
                np.uint64
            ),
            56,
        )  # 8 bytes
        # 4 bytes
        allfields[f"bb_{indichar}_uni0_0_00"] = np.ascontiguousarray(
            uni0_0_00.flatten()
        )
        allfields[f"bb_{indichar}_uni0_1_00"] = np.ascontiguousarray(
            uni0_1_00.flatten()
        )
        allfields[f"bb_{indichar}_uni1_0_04"] = np.ascontiguousarray(
            uni1_0_04.flatten()
        )
        allfields[f"bb_{indichar}_uni2_0_12"] = np.ascontiguousarray(
            uni2_0_12.flatten()
        )
        allfields[f"bb_{indichar}_uni2_1_08"] = np.ascontiguousarray(
            uni2_1_08.flatten()
        )
        allfields[f"bb_{indichar}_uni4_0_20"] = np.ascontiguousarray(
            uni4_0_20.flatten()
        )
        allfields[f"bb_{indichar}_uni4_0_28"] = np.ascontiguousarray(
            uni4_0_28.flatten()
        )
        allfields[f"bb_{indichar}_uni4_1_16"] = np.ascontiguousarray(
            uni4_1_16.flatten()
        )
        allfields[f"bb_{indichar}_uni4_1_24"] = np.ascontiguousarray(
            uni4_1_24.flatten()
        )
        allfields[f"bb_{indichar}_uni8_0_36"] = np.ascontiguousarray(
            uni8_0_36.flatten()
        )
        allfields[f"bb_{indichar}_uni8_0_44"] = np.ascontiguousarray(
            uni8_0_44.flatten()
        )
        allfields[f"bb_{indichar}_uni8_0_52"] = np.ascontiguousarray(
            uni8_0_52.flatten()
        )
        allfields[f"bb_{indichar}_uni8_0_58"] = np.ascontiguousarray(
            uni8_0_58.flatten()
        )
        allfields[f"bb_{indichar}_uni8_1_32"] = np.ascontiguousarray(
            uni8_1_32.flatten()
        )
        allfields[f"bb_{indichar}_uni8_1_40"] = np.ascontiguousarray(
            uni8_1_40.flatten()
        )
        allfields[f"bb_{indichar}_uni8_1_48"] = np.ascontiguousarray(
            uni8_1_48.flatten()
        )
        allfields[f"bb_{indichar}_uni8_1_56"] = np.ascontiguousarray(
            uni8_1_56.flatten()
        )

    df = pd.DataFrame(allfields)

    df["aa_Byte_int"] = df.bb_21_uni1_0_04.astype(np.uint8) + df.bb_21_uni0_1_00.astype(
        np.uint8
    )
    df["aa_Byte_hex"] = splittetresultsdict_bytes[21].view("a2").flatten().astype("U")
    df["aa_2Bytes_int"] = (
        df.bb_21_uni1_0_04
        + df.bb_21_uni0_1_00
        + df.bb_24_uni2_0_12
        + df.bb_24_uni2_1_08
    )
    df["aa_2Bytes_hex"] = (
        np.hstack([splittetresultsdict_bytes[24], splittetresultsdict_bytes[21]])
        .view("a4")
        .flatten()
        .astype("U")
    )
    df["aa_4Bytes_int"] = (
        df.bb_30_uni4_0_28
        + df.bb_30_uni4_1_24
        + df.bb_27_uni4_0_20
        + df.bb_27_uni4_1_16
        + df["aa_2Bytes_int"].astype(np.uint64)
    )
    df["aa_4Bytes_float"] = (
        np.ascontiguousarray(df["aa_4Bytes_int"]).view("b").view(np.float32)[::2]
    )
    df["aa_4Bytes_and_float_hex"] = (
        np.hstack(
            [
                splittetresultsdict_bytes[30],
                splittetresultsdict_bytes[27],
                splittetresultsdict_bytes[24],
                splittetresultsdict_bytes[21],
            ]
        )
        .view("a8")
        .flatten()
        .astype("U")
    )
    df["aa_8Bytes_int"] = (
        df.bb_42_uni8_0_58
        + df.bb_42_uni8_1_56
        + df.bb_39_uni8_0_52
        + df.bb_39_uni8_1_48
        + df.bb_36_uni8_0_44
        + df.bb_36_uni8_1_40
        + df.bb_33_uni8_0_36
        + df.bb_33_uni8_1_32
        + df["aa_4Bytes_int"].astype(np.uint64)
    )
    df["aa_8Bytes_float"] = df["aa_8Bytes_int"].view("V8").view(np.float64)
    df["aa_8Bytes_and_double_hex"] = (
        np.hstack(
            [
                splittetresultsdict_bytes[42],
                splittetresultsdict_bytes[39],
                splittetresultsdict_bytes[36],
                splittetresultsdict_bytes[33],
                splittetresultsdict_bytes[30],
                splittetresultsdict_bytes[27],
                splittetresultsdict_bytes[24],
                splittetresultsdict_bytes[21],
            ]
        )
        .view("a16")
        .flatten()
        .astype("U")
    )

    allindexchar = [21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66]

    if with_utf8_bytes:
        df["aa_utf8_str_all"] = np.fromiter(
            yield_utf(splittetresultsdict_bytes[84]), dtype="U16"
        ).copy()
        bytesutf = pd.DataFrame(
            np.array(list(yield_utf_numbers(splittetresultsdict_bytes[84]))),
            columns=[f"aa_utf8_int_{x}" for x in allindexchar],
        )
        df = pd.concat([df, bytesutf], axis=1)
    else:
        df["aa_utf8_str_all"] = pd.NA

    df["aa_ascii_str_all"] = (
        pd.Series(splittetresultsdict_bytes[84].view("a16").flatten())
        .astype("string")
        .str.slice(start=2, stop=-1)
        .copy()
    )
    ascii = pd.DataFrame(
        splittetresultsdict_bytes[84].view(np.int8),
        columns=[f"aa_ascii_int_{x}" for x in allindexchar],
    )
    df = pd.concat([df, ascii], axis=1)

    for x in df.columns:
        if str(df[x].dtype) == "object":
            df[x] = df[x].astype("string")

    importantcols_ = [
        "aa_address1_hex",
        "aa_address2_hex",
        "aa_address1_int",
        "aa_address2_int",
        "aa_Byte_int",
        "aa_Byte_hex",
        "aa_2Bytes_int",
        "aa_2Bytes_hex",
        "aa_4Bytes_int",
        "aa_4Bytes_float",
        "aa_4Bytes_and_float_hex",
        "aa_8Bytes_float",
        "aa_8Bytes_int",
        "aa_8Bytes_and_double_hex",
        "aa_utf8_str_all",
        "aa_ascii_str_all",
    ]
    importantcols2 = []
    allindexchar = [21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66]
    for chari in allindexchar:
        importantcols2.extend(
            [
                f"aa_utf8_int_{chari}",
                f"aa_utf8_str_{chari}",
                f"aa_ascii_int_{chari}",
                f"aa_ascii_str_{chari}",
            ]
        )
    importantcols2.sort()
    importantcols2 = (
        [
            x
            for x in df.columns.to_list()
            if not "utf8_str" in x and not "ascii_str" in x
        ]
        + [x for x in df.columns.to_list() if "_str_all" in x]
        + [x for x in df.columns.to_list() if "utf8_str" in x and not "_str_all" in x]
        + [x for x in df.columns.to_list() if "ascii_str" in x and not "_str_all" in x]
    )
    importantcols = importantcols_ + importantcols2
    importantcols = list(dict.fromkeys(importantcols))

    yield df[importantcols].copy()


def print_memory_map(pid):

    alle = []
    process = Process(pid)
    bits = process.get_bits()
    memoryMap = process.get_memory_map()
    for mbi in memoryMap:

        # Address and size of memory block.
        BaseAddress = HexDump.address(mbi.BaseAddress, bits)
        RegionSize = HexDump.address(mbi.RegionSize, bits)

        # State (free or allocated).
        if mbi.State == win32.MEM_RESERVE:
            State = "Reserved  "
        elif mbi.State == win32.MEM_COMMIT:
            State = "Commited  "
        elif mbi.State == win32.MEM_FREE:
            State = "Free      "
        else:
            State = "Unknown   "

        # Page protection bits (R/W/X/G).
        if mbi.State != win32.MEM_COMMIT:
            Protect = "          "
        else:
            if mbi.Protect & win32.PAGE_NOACCESS:
                Protect = "--- "
            elif mbi.Protect & win32.PAGE_READONLY:
                Protect = "R-- "
            elif mbi.Protect & win32.PAGE_READWRITE:
                Protect = "RW- "
            elif mbi.Protect & win32.PAGE_WRITECOPY:
                Protect = "RC- "
            elif mbi.Protect & win32.PAGE_EXECUTE:
                Protect = "--X "
            elif mbi.Protect & win32.PAGE_EXECUTE_READ:
                Protect = "R-X "
            elif mbi.Protect & win32.PAGE_EXECUTE_READWRITE:
                Protect = "RWX "
            elif mbi.Protect & win32.PAGE_EXECUTE_WRITECOPY:
                Protect = "RCX "
            else:
                Protect = "??? "
            if mbi.Protect & win32.PAGE_GUARD:
                Protect += "G"
            else:
                Protect += "-"
            if mbi.Protect & win32.PAGE_NOCACHE:
                Protect += "N"
            else:
                Protect += "-"
            if mbi.Protect & win32.PAGE_WRITECOMBINE:
                Protect += "W"
            else:
                Protect += "-"
            Protect += "   "

        # Type (file mapping, executable image, or private memory).
        if mbi.Type == win32.MEM_IMAGE:
            Type = "Image     "
        elif mbi.Type == win32.MEM_MAPPED:
            Type = "Mapped    "
        elif mbi.Type == win32.MEM_PRIVATE:
            Type = "Private   "
        elif mbi.Type == 0:
            Type = "Free      "
        else:
            Type = "Unknown   "

        alle.append((BaseAddress, RegionSize, State, Protect, Type))

    columnsmemmap = [
        "aa_base_address",
        "aa_region_size",
        "aa_state",
        "aa_protect",
        "aa_type",
    ]
    memmapdf = pd.DataFrame(alle)
    memmapdf.columns = columnsmemmap
    memmapdf["aa_region_size_int"] = memmapdf.aa_region_size.map(lambda x: int(x, 16))
    memmapdf["aa_start_address_int"] = memmapdf.aa_base_address.map(
        lambda x: int(x, 16)
    )
    memmapdf["aa_start_address_hex"] = (
        memmapdf.aa_base_address.str.slice(0, 8).str.lower()
        + "`"
        + memmapdf.aa_base_address.str.slice(
            8,
        ).str.lower()
    )
    memmapdf["aa_end_address_int"] = (
        memmapdf["aa_start_address_int"] + memmapdf["aa_region_size_int"]
    )
    memmapdf["aa_end_address_int"] = memmapdf["aa_end_address_int"].astype(np.uint64)
    memmapdf["aa_end_address_hex"] = memmapdf["aa_end_address_int"].map(
        lambda x: hex(x).lstrip("0x").zfill(16)
    )
    memmapdf["aa_end_address_hex"] = (
        memmapdf.aa_end_address_hex.str.slice(0, 8).str.lower()
        + "`"
        + memmapdf.aa_end_address_hex.str.slice(
            8,
        ).str.lower()
    )
    memmapdf = memmapdf.drop(columns=["aa_base_address", "aa_region_size"]).reset_index(
        drop=True
    )
    return memmapdf


def get_memorydf(pid, procdumppath, with_utf8_bytes=False):
    dumpfile, deltemp = get_tmpfile(suffix=".dmp")
    touch(dumpfile)
    createdump = True
    if createdump:
        erg = (
            ProcDump(procdumppath)
            .o()
            .ma()
            .add_own_parameter_or_option(f"{pid}")
            .add_target_file_or_folder([dumpfile])
            .run()
        )

    pykd.loadDump(dumpfile)
    memmapdf = print_memory_map(pid)
    filtereddf = memmapdf.loc[
        memmapdf.aa_protect.str.contains("^RW")
        & ~memmapdf.aa_type.str.contains("^Image")
    ]

    memreadresults = {}
    for key, item in filtereddf.iterrows():
        try:
            memreadresults[
                f"{item.aa_start_address_hex} {item.aa_end_address_hex}"
            ] = get_dataframe(
                addressrange=f"{item.aa_start_address_hex} {item.aa_end_address_hex}",
                with_utf8_bytes=with_utf8_bytes,
            )
        except Exception as Fehler:
            print(Fehler)
    dafa = pd.concat([next(x[-1]) for x in memreadresults.items()]).reset_index(
        drop=True
    )
    DataFrame.tmp_file_path = dumpfile
    DataFrame.tmp_delete_file = deltemp
    return dafa


def pd_add_memorydf():
    pd.Q_df_from_memory = get_memorydf
