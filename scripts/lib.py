"""
Shared palette + the isometric contribution-skyline builder.
Used both for one-off generation and by generate.py in CI.
Stdlib only (plus the caller passing in datetime.date objects) so it
runs on a bare Actions runner with no pip installs.
"""

BG0 = "#060A12"; BG1 = "#0A1120"; PANEL = "#0A1120"
BLUE_DEEP = "#2E86FF"; BLUE_TEAL = "#22B8CF"; CYAN = "#3DDCF0"
GREEN_TEAL = "#17C3B2"; GREEN = "#2FD180"; MINT = "#56E39F"
RED = "#D7263D"  # blood red — single accent, use sparingly
TEXT = "#E6EDF6"; MUTED = "#8AA0C2"; DIM = "#7C93B8"; FAINT = "#4C6182"
GRID = "#1B2740"; BORDER = "#1E2C46"
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgbhex(rgb):
    return "#%02X%02X%02X" % rgb


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def darken(hexcol, f=0.62):
    r, g, b = hexrgb(hexcol)
    return rgbhex((int(r * f), int(g * f), int(b * f)))


def lighten(hexcol, f=0.28):
    r, g, b = hexrgb(hexcol)
    return rgbhex((min(255, int(r + (255 - r) * f)),
                    min(255, int(g + (255 - g) * f)),
                    min(255, int(b + (255 - b) * f))))


def build_isometric_skyline_svg(daily):
    """
    daily: sorted list of (datetime.date, contribution_count) covering
    the last ~53 weeks, starting on a Sunday (GitHub's own calendar
    convention). Returns a self-contained SVG string: an isometric
    contribution skyline with a stats chip and a streak chip, styled
    to sit on a light or dark page (no full-bleed background fill).
    """
    start = daily[0][0]
    ROWS = 7
    grid = {}
    for d, c in daily:
        col = (d - start).days // 7
        row = (d.weekday() + 1) % 7  # Sunday = 0
        grid[(col, row)] = c
    COLS = max(col for col, _ in grid.keys()) + 1

    total = sum(c for _, c in daily)
    last_date = daily[-1][0]
    this_week_total = sum(c for _, c in daily[-7:])
    best_date, best_val = max(daily, key=lambda x: x[1])

    longest = cur = 0
    longest_range = None
    streak_start = None
    for d, c in daily:
        if c > 0:
            if streak_start is None:
                streak_start = d
            cur += 1
            if cur > longest:
                longest = cur
                longest_range = (streak_start, d)
        else:
            streak_start = None
            cur = 0
    current = 0
    current_start = None
    for d, c in reversed(daily):
        if c > 0:
            current += 1
            current_start = d
        else:
            break
    avg = total / len(daily)

    HW, HH = 8.6, 4.3
    maxc = max(grid.values()) if grid else 1

    def h_for(c):
        return 0 if c == 0 else 10 + 46 * (c / maxc) ** 0.62

    GREEN_DARK = hexrgb("#0E3B2A")
    GREEN_MID = hexrgb("#1E8E5A")
    GREEN_HOT = hexrgb("#3DDC84")
    GREEN_PEAK = hexrgb("#7CFFB2")

    def col_for(c):
        if c == 0:
            return "#141B29"
        t = min(1.0, c / maxc)
        if t < 0.34:
            col = lerp(GREEN_DARK, GREEN_MID, t / 0.34)
        elif t < 0.7:
            col = lerp(GREEN_MID, GREEN_HOT, (t - 0.34) / 0.36)
        else:
            col = lerp(GREEN_HOT, GREEN_PEAK, (t - 0.7) / 0.3)
        return rgbhex(col)

    def iso(col, row):
        return (col - row) * HW, (col + row) * HH

    xs, ys = [], []
    for col in range(COLS):
        for row in range(ROWS):
            x, y = iso(col, row)
            xs += [x - HW, x + HW]
            ys += [y - HH, y + HH]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    top_pad = 60
    GW = maxx - minx + 40
    GH = maxy - miny + top_pad + 20
    OX = -minx + 20
    OY = -miny + top_pad

    tiles = []
    peak_key = max(grid, key=grid.get) if grid else None
    for (col, row) in sorted(grid.keys(), key=lambda k: (k[0] + k[1], k[0])):
        c = grid[(col, row)]
        x, y = iso(col, row)
        x += OX
        y += OY
        h = h_for(c)
        fill = col_for(c)
        if h == 0:
            pts = f"{x:.1f},{y-HH:.1f} {x+HW:.1f},{y:.1f} {x:.1f},{y+HH:.1f} {x-HW:.1f},{y:.1f}"
            tiles.append(f'<polygon points="{pts}" fill="{fill}" opacity="0.9"/>')
            continue
        topy = y - h
        top_pts = f"{x:.1f},{topy-HH:.1f} {x+HW:.1f},{topy:.1f} {x:.1f},{topy+HH:.1f} {x-HW:.1f},{topy:.1f}"
        left_pts = f"{x-HW:.1f},{y:.1f} {x:.1f},{y+HH:.1f} {x:.1f},{topy+HH:.1f} {x-HW:.1f},{topy:.1f}"
        right_pts = f"{x:.1f},{y+HH:.1f} {x+HW:.1f},{y:.1f} {x+HW:.1f},{topy:.1f} {x:.1f},{topy+HH:.1f}"
        tiles.append(f'<polygon points="{left_pts}" fill="{darken(fill,0.55)}"/>')
        tiles.append(f'<polygon points="{right_pts}" fill="{darken(fill,0.78)}"/>')
        tiles.append(f'<polygon points="{top_pts}" fill="{lighten(fill,0.30)}"/>')
        if (col, row) == peak_key:
            bx, by = x, topy - HH
            tiles.append(f'<circle cx="{bx:.1f}" cy="{by-8:.1f}" r="3" fill="{RED}"><animate attributeName="opacity" values="1;0.3;1" dur="1.4s" repeatCount="indefinite"/></circle>')
            tiles.append(f'<line x1="{bx:.1f}" y1="{by-8:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{RED}" stroke-width="1"/>')

    W, H = GW, GH

    def fmt_range(d0, d1):
        return f"{d0.strftime('%b %-d')} \u2192 {d1.strftime('%b %-d')}"

    card_w, card_h = 268, 122
    cx0, cy0 = W - card_w - 6, 6
    col_gap = 90
    stat_card = f'''
<g>
 <rect x="{cx0}" y="{cy0}" width="{card_w}" height="{card_h}" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>
 <text x="{cx0+18}" y="{cy0+26}" font-size="12" letter-spacing="1.6" fill="{DIM}">CONTRIBUTIONS</text>
 <text x="{cx0+18}" y="{cy0+58}" font-size="25" font-weight="700" fill="#3DDC84">{total}</text>
 <text x="{cx0+18}" y="{cy0+75}" font-size="9" letter-spacing="0.6" fill="{DIM}">TOTAL</text>
 <text x="{cx0+18}" y="{cy0+90}" font-size="9" fill="{FAINT}">past year</text>
 <text x="{cx0+18+col_gap}" y="{cy0+58}" font-size="25" font-weight="700" fill="{TEXT}">{this_week_total}</text>
 <text x="{cx0+18+col_gap}" y="{cy0+75}" font-size="9" letter-spacing="0.6" fill="{DIM}">THIS WEEK</text>
 <text x="{cx0+18+col_gap}" y="{cy0+90}" font-size="9" fill="{FAINT}">{last_date.strftime('%b %-d')}</text>
 <text x="{cx0+18+2*col_gap}" y="{cy0+58}" font-size="25" font-weight="700" fill="{TEXT}">{best_val}</text>
 <text x="{cx0+18+2*col_gap}" y="{cy0+75}" font-size="9" letter-spacing="0.6" fill="{DIM}">BEST DAY</text>
 <text x="{cx0+18+2*col_gap}" y="{cy0+90}" font-size="9" fill="{FAINT}">{best_date.strftime('%b %-d')}</text>
 <line x1="{cx0+18}" y1="{cy0+102}" x2="{cx0+card_w-18}" y2="{cy0+102}" stroke="{BORDER}" stroke-width="1"/>
 <text x="{cx0+18}" y="{cy0+116}" font-size="9.5" fill="{MUTED}">Average {avg:.1f} contributions / day</text>
</g>'''

    sw, sh = 224, 90
    sx0, sy0 = 6, H - sh - 6
    streak_col_gap = 112
    streak_card = f'''
<g>
 <rect x="{sx0}" y="{sy0}" width="{sw}" height="{sh}" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="1"/>
 <text x="{sx0+16}" y="{sy0+24}" font-size="12" letter-spacing="1.6" fill="{DIM}">STREAKS</text>
 <text x="{sx0+16}" y="{sy0+54}" font-size="22" font-weight="700" fill="#3DDC84">{longest}d</text>
 <text x="{sx0+16}" y="{sy0+70}" font-size="9" letter-spacing="0.6" fill="{DIM}">LONGEST</text>
 <text x="{sx0+16}" y="{sy0+83}" font-size="8.5" fill="{FAINT}">{fmt_range(*longest_range) if longest_range else "—"}</text>
 <text x="{sx0+16+streak_col_gap}" y="{sy0+54}" font-size="22" font-weight="700" fill="{TEXT}">{current}d</text>
 <text x="{sx0+16+streak_col_gap}" y="{sy0+70}" font-size="9" letter-spacing="0.6" fill="{DIM}">CURRENT</text>
 <text x="{sx0+16+streak_col_gap}" y="{sy0+83}" font-size="8.5" fill="{FAINT}">{(current_start.strftime('%b %-d') if current_start else '—')} \u2192 {last_date.strftime('%b %-d')}</text>
</g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" font-family="{FONT}">
<g>{chr(10)+chr(10).join(tiles)}</g>
{stat_card}
{streak_card}
</svg>'''
