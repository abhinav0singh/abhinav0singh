"""
Shared palette + SVG builders for the profile README.
Used both for one-off generation and by generate.py in CI.
Deliberately dependency-free (stdlib only) so it runs on a bare Actions runner.
"""
import math

BG0 = "#060A12"; BG1 = "#0A1120"; PANEL = "#080D18"
BLUE_DEEP = "#2E86FF"; BLUE_TEAL = "#22B8CF"; CYAN = "#3DDCF0"
GREEN_TEAL = "#17C3B2"; GREEN = "#2FD180"; MINT = "#56E39F"
RED = "#D7263D"  # blood red — single accent, use sparingly
TEXT = "#E6EDF6"; MUTED = "#8AA0C2"; DIM = "#7C93B8"; FAINT = "#42546F"
GRID = "#1B2740"; BORDER = "#1E2C46"
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

RAMP_HEX = [BLUE_DEEP, BLUE_TEAL, GREEN_TEAL, GREEN, MINT]


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgbhex(rgb):
    return "#%02X%02X%02X" % rgb


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


_RAMP = [hexrgb(c) for c in RAMP_HEX]


def ramp(t):
    t = max(0.0, min(1.0, t))
    n = len(_RAMP) - 1
    seg = min(int(t * n), n - 1)
    local = t * n - seg
    return rgbhex(lerp(_RAMP[seg], _RAMP[seg + 1], local))


def darken(hexcol, f=0.62):
    r, g, b = hexrgb(hexcol)
    return rgbhex((int(r * f), int(g * f), int(b * f)))


def lighten(hexcol, f=0.28):
    r, g, b = hexrgb(hexcol)
    return rgbhex((min(255, int(r + (255 - r) * f)),
                    min(255, int(g + (255 - g) * f)),
                    min(255, int(b + (255 - b) * f))))


def build_skyline_svg(weekly, total):
    """weekly: list of per-week contribution totals (oldest -> newest). total: int, contributions in the window."""
    N = len(weekly)
    peak_i = max(range(N), key=lambda i: weekly[i])
    peak_v = max(1, weekly[peak_i])

    W, H = 1200, 340
    base = H - 96
    pitch = (1200 - 120) / N
    fw = pitch * 0.52
    depth = 9
    maxH = 150

    def height_for(v):
        return 3 if v == 0 else 10 + (maxH - 10) * (v / peak_v)

    def col_for(v):
        return "#111C30" if v == 0 else ramp(v / peak_v)

    buildings = []
    for i, v in enumerate(weekly):
        x = 60 + i * pitch + (pitch - fw) / 2
        h = height_for(v)
        top = base - h
        c = col_for(v)
        op = 0.92 if v else 0.4
        b = [f'<rect x="{x:.1f}" y="{top:.1f}" width="{fw:.1f}" height="{h:.1f}" fill="{c}" opacity="{op}"/>']
        x2 = x + fw
        b.append(f'<polygon points="{x2:.1f},{top:.1f} {x2+depth:.1f},{top-depth*0.7:.1f} {x2+depth:.1f},{base-depth*0.7:.1f} {x2:.1f},{base:.1f}" fill="{darken(c)}" opacity="{op}"/>')
        b.append(f'<polygon points="{x:.1f},{top:.1f} {x2:.1f},{top:.1f} {x2+depth:.1f},{top-depth*0.7:.1f} {x+depth:.1f},{top-depth*0.7:.1f}" fill="{lighten(c)}" opacity="{min(1,op+0.05)}"/>')
        if i == peak_i and v > 0:
            bx = x + fw / 2
            b.append(f'<circle cx="{bx:.1f}" cy="{top-depth*0.7-9:.1f}" r="3.4" fill="{RED}"><animate attributeName="opacity" values="1;0.25;1" dur="1.3s" repeatCount="indefinite"/></circle>')
            b.append(f'<line x1="{bx:.1f}" y1="{top-depth*0.7-9:.1f}" x2="{bx:.1f}" y2="{top-depth*0.7:.1f}" stroke="{RED}" stroke-width="1.2"/>')
        buildings.append("".join(b))

    STEPS = 240
    pathpts = []
    for i in range(STEPS + 1):
        t = i / STEPS
        tri = 1 - abs(2 * t - 1)
        x = 60 + tri * (W - 180)
        y = base + 22 + 9 * math.sin(t * 26)
        pathpts.append((x, y))
    L = len(pathpts)
    OFFSET = 60

    nseg = 12
    radii = [9, 8.3, 7.6, 6.9, 6.2, 5.5, 4.8, 4.1, 3.5, 3.0, 2.5, 2.1]
    phase = 6
    snake = []
    for s in range(nseg):
        vals = [pathpts[(k + OFFSET - s * phase) % L] for k in range(L)]
        cx0, cy0 = vals[0]
        xs = ";".join(f"{p[0]:.1f}" for p in vals)
        ys = ";".join(f"{p[1]:.1f}" for p in vals)
        t = s / (nseg - 1)
        col = rgbhex(lerp(hexrgb(MINT), hexrgb(BLUE_DEEP), t))
        snake.append(f'<circle cx="{cx0:.1f}" cy="{cy0:.1f}" r="{radii[s]}" fill="{col}" opacity="{0.96-0.35*t}">'
                     f'<animate attributeName="cx" values="{xs}" dur="16s" repeatCount="indefinite" calcMode="linear"/>'
                     f'<animate attributeName="cy" values="{ys}" dur="16s" repeatCount="indefinite" calcMode="linear"/></circle>')
    eyevals = [pathpts[(k + OFFSET) % L] for k in range(L)]
    hx, hy = eyevals[0]
    exs = ";".join(f"{p[0]-2.2:.1f}" for p in eyevals)
    eys = ";".join(f"{p[1]-2.4:.1f}" for p in eyevals)
    snake.append(f'<circle cx="{hx-2.2:.1f}" cy="{hy-2.4:.1f}" r="1" fill="{RED}"><animate attributeName="cx" values="{exs}" dur="16s" repeatCount="indefinite" calcMode="linear"/><animate attributeName="cy" values="{eys}" dur="16s" repeatCount="indefinite" calcMode="linear"/></circle>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">
<defs>
 <linearGradient id="skybg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="#0B0F1C"/></linearGradient>
 <pattern id="sgrid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{GRID}" stroke-width="0.6"/></pattern>
 <clipPath id="skf"><rect width="{W}" height="{H}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#skf)">
 <rect width="{W}" height="{H}" fill="url(#skybg)"/>
 <rect width="{W}" height="{H}" fill="url(#sgrid)" opacity="0.4"/>
 <text x="30" y="34" font-size="12" letter-spacing="3.2" fill="{DIM}">CONTRIBUTIONS — LAST 12 MONTHS</text>
 <text x="{W-30}" y="34" text-anchor="end" font-size="12" letter-spacing="1.6" fill="{MUTED}">{total} total · peak week {peak_v}</text>
 <line x1="30" y1="{base+1.5}" x2="{W-30}" y2="{base+1.5}" stroke="{BORDER}" stroke-width="1"/>
 <g>{chr(10)+chr(10).join(buildings)}</g>
 <g>{chr(10)+chr(10).join(snake)}</g>
 <rect width="{W}" height="{H}" rx="16" fill="none" stroke="{BORDER}" stroke-width="1.5"/>
</g></svg>'''


def build_stats_svg(stats):
    """stats: list of (value_str, label, color_hex) tuples, 3 or 4 items."""
    W, H = 880, 150
    n = len(stats)
    cw = W / n
    cells = []
    for i, (val, label, col) in enumerate(stats):
        cx = cw * i + cw / 2
        cells.append(f'''<text x="{cx:.1f}" y="70" text-anchor="middle" font-size="40" font-weight="700" fill="{col}">{val}</text>
<text x="{cx:.1f}" y="98" text-anchor="middle" font-size="11.5" letter-spacing="1.4" fill="{DIM}">{label.upper()}</text>
<rect x="{cx-22:.1f}" y="112" width="44" height="2.4" rx="1.2" fill="{col}" opacity="0.75">
<animate attributeName="width" values="0;44" dur="1s" begin="{i*0.12:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
<animate attributeName="x" values="{cx:.1f};{cx-22:.1f}" dur="1s" begin="{i*0.12:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></rect>''')
    dividers = "".join(f'<line x1="{cw*i:.1f}" y1="30" x2="{cw*i:.1f}" y2="120" stroke="{BORDER}" stroke-width="1"/>' for i in range(1, n))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">
<defs><clipPath id="stf"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>
<g clip-path="url(#stf)">
<rect width="{W}" height="{H}" fill="{PANEL}"/>
<text x="26" y="26" font-size="11" letter-spacing="3" fill="{DIM}">GITHUB — LIVE NUMBERS</text>
{dividers}
{chr(10).join(cells)}
<rect width="{W}" height="{H}" rx="14" fill="none" stroke="{BORDER}" stroke-width="1.5"/>
</g></svg>'''
