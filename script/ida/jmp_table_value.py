from idc import *
from idaapi import *
from idautils import *

test_sig = "48 8B CB E8 ? ? ? ? B0 ? 48 8B 5C 24 ? 48 8B 74 24 ? 48 83 C4 ? " \
           "5F C3 48 8B CB E8 ? ? ? ? B0 ? 48 8B 5C 24 ? 48 8B 74 24 ? 48 83 C4 ? 5F C3 0F B6 43 ?"
min_ea = inf_get_min_ea()
max_ea = inf_get_max_ea()


def sig_search(sig: str, max_search_cnt: int = 10):
    addr = min_ea
    while max_search_cnt > 0:
        addr = find_binary(addr, max_ea, sig, 16, SEARCH_DOWN | SEARCH_NEXT)
        if addr == BADADDR: break
        yield addr
        max_search_cnt -= 1


def find_xrefs(ea: int) -> dict:
    xrefs = {}
    for xref in XrefsTo(ea, 0):
        xrefs.setdefault(xref.type, []).append(xref.frm)
    return xrefs


def _find_switch_values(_si: int, ea: int):
    si = ida_nalt.switch_info_t()
    if ida_nalt.get_switch_info(si, _si):
        results = calc_switch_cases(_si, si)
        for idx in range(len(results.cases)):
            if results.targets[idx] == ea:
                cases = results.cases[idx]
                return [cases[idx] for idx in range(len(cases))]
    return None


def find_switch_values(ea: int):
    xrefs = find_xrefs(ea)
    while True:
        if 19 in xrefs:
            res = _find_switch_values(xrefs[19][0], ea)
            if res is not None:
                return res
        if 21 in xrefs:
            ea = xrefs[21][0]
            xrefs = find_xrefs(ea)
        else:
            raise Exception('not found')


for addr in sig_search(test_sig):
    values = find_switch_values(addr)
    print(hex(addr), values)
print('done')