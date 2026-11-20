#!/usr/bin/env python3
import argparse
import json
import struct
import sys
import zipfile

MARK = {'\x01': '‹1›', '\x02': '‹2›'}


def to_display(s):
    for raw, shown in MARK.items():
        s = s.replace(raw, shown)
    return s


def from_display(s):
    for raw, shown in MARK.items():
        s = s.replace(shown, raw)
    return s


def decode_mutf8(b):
    out = []
    i = 0
    n = len(b)
    while i < n:
        c = b[i]
        if c < 0x80:
            out.append(c)
            i += 1
        elif c >> 5 == 0b110:
            out.append(((c & 0x1F) << 6) | (b[i + 1] & 0x3F))
            i += 2
        else:
            out.append(((c & 0x0F) << 12) | ((b[i + 1] & 0x3F) << 6) | (b[i + 2] & 0x3F))
            i += 3
    return ''.join(chr(x) for x in out).encode('utf-16', 'surrogatepass').decode('utf-16', 'replace')


def encode_mutf8(s):
    units = s.encode('utf-16-le', 'surrogatepass')
    out = bytearray()
    for i in range(0, len(units), 2):
        u = units[i] | (units[i + 1] << 8)
        if u == 0:
            out += b'\xc0\x80'
        elif u < 0x80:
            out.append(u)
        elif u < 0x800:
            out += bytes([0xC0 | (u >> 6), 0x80 | (u & 0x3F)])
        else:
            out += bytes([0xE0 | (u >> 12), 0x80 | ((u >> 6) & 0x3F), 0x80 | (u & 0x3F)])
    return bytes(out)


def patch_class(data, table, used):
    if data[:4] != b'\xca\xfe\xba\xbe':
        return data, 0
    count = struct.unpack('>H', data[8:10])[0]
    pos = 10
    idx = 1
    parts = [data[:10]]
    changed = 0
    while idx < count:
        tag = data[pos]
        if tag == 1:
            length = struct.unpack('>H', data[pos + 1:pos + 3])[0]
            raw = data[pos + 3:pos + 3 + length]
            end = pos + 3 + length
            try:
                shown = to_display(decode_mutf8(raw))
            except Exception:
                shown = None
            if shown is not None and shown in table:
                new = encode_mutf8(from_display(table[shown]))
                if len(new) > 65535:
                    raise SystemExit('constant too long: ' + shown[:60])
                parts.append(b'\x01' + struct.pack('>H', len(new)) + new)
                used.add(shown)
                changed += 1
            else:
                parts.append(data[pos:end])
            pos = end
        else:
            size = {3: 5, 4: 5, 9: 5, 10: 5, 11: 5, 12: 5, 17: 5, 18: 5, 5: 9, 6: 9, 7: 3, 8: 3, 16: 3, 19: 3, 20: 3, 15: 4}[tag]
            parts.append(data[pos:pos + size])
            pos += size
            if tag in (5, 6):
                idx += 1
        idx += 1
    parts.append(data[pos:])
    return b''.join(parts), changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--jar', required=True)
    ap.add_argument('--table', default='')
    ap.add_argument('--out', required=True)
    ap.add_argument('--prefix', default='')
    ap.add_argument('--resource', action='append', default=[])
    a = ap.parse_args()
    table = json.load(open(a.table, encoding='utf-8')) if a.table else {}
    resources = {}
    for item in a.resource:
        name, path = item.split('=', 1)
        resources[name] = open(path, 'rb').read()
    for k, v in table.items():
        if k.count('‹') != v.count('‹'):
            raise SystemExit('marker mismatch: ' + k[:60])
    used = set()
    total = 0
    src = zipfile.ZipFile(a.jar)
    with zipfile.ZipFile(a.out, 'w', zipfile.ZIP_DEFLATED) as dst:
        for info in src.infolist():
            data = resources.pop(info.filename, None)
            if data is None:
                data = src.read(info.filename)
            if info.filename.endswith('.class') and info.filename.startswith(a.prefix):
                data, n = patch_class(data, table, used)
                total += n
            zi = zipfile.ZipInfo(info.filename, info.date_time)
            zi.compress_type = info.compress_type
            zi.external_attr = info.external_attr
            dst.writestr(zi, data)
    if resources:
        raise SystemExit('resources not found in jar: ' + ', '.join(resources))
    missing = [k for k in table if k not in used]
    print('patched constants:', total, 'unused table entries:', len(missing))
    for k in missing[:20]:
        print('  unused:', k[:100])
    return 0


if __name__ == '__main__':
    sys.exit(main())
