#!/usr/bin/env node
// Generate every brand asset from one geometry: the SVG sources in brand/assets/ and the
// raster sets (favicon, app icon, Tauri, social, README banner) rendered from them.
//
//   npm install                                   # once: sharp, opentype.js, Inter
//   node scripts/build-assets.mjs                 # write all assets
//   node scripts/build-assets.mjs --check         # exit 1 if an SVG is stale or a raster is missing
//   node scripts/build-assets.mjs --product "Control Center" --out ./brand
//                                                 # lockups, banners and OG image for one product
//
// Wordmark text is converted to outlines with Inter (SIL OFL 1.1), so the SVGs need no font.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";
import opentype from "opentype.js";
import sharp from "sharp";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const ASSETS = join(ROOT, "brand", "assets");
const tokens = JSON.parse(readFileSync(join(ROOT, "tokens", "tokens.json"), "utf8"));
const C = Object.fromEntries(
  ["brand", "light", "dark"].map((g) => [g, Object.fromEntries(
    Object.entries(tokens.color[g]).filter(([k]) => !k.startsWith("$")).map(([k, v]) => [k, v.$value]))]),
);

// Pass exactly the file's bytes: a Buffer's .buffer can be a larger shared pool with an offset.
const font = (weight) => {
  const b = readFileSync(join(ROOT, "node_modules", "@fontsource", "inter", "files", `inter-latin-${weight}-normal.woff`));
  return opentype.parse(b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength));
};
const INTER = { 400: font(400), 600: font(600), 700: font(700) };

// ------------------------------------------------------------------ geometry
// The mark on its 24-unit grid (see brand/brand.md, 2.1): an "A" whose crossbar is an orbit.
// Two legs meet under an apex node; a tilted elliptical orbit passes behind the legs at the
// top and in front of them at the bottom, carrying one satellite node. Where one stroke
// passes over another, the stroke underneath is cut by `gap` on each side, so the weave
// reads in one colour too (mono and currentColor versions).
// The favicon variant drops the satellite and thickens every stroke for 16 px.
const LEGS = "M4.2 21.6 12 4.5 19.8 21.6";
const APEX = [12, 3.9];
const ORBIT = { cx: 12, cy: 14.4, rx: 10.5, angle: -14 };
const GLYPH = {
  full: { legs: 3.3, orbit: 1.8, ry: 3.6, apex: 2.6, satellite: 1.6, gap: 0.9 },
  small: { legs: 4.2, orbit: 2.4, ry: 3.8, apex: 2.9, satellite: 0, gap: 1.2 },
};

const n = (x) => +x.toFixed(3);

/** Point on the orbit at parameter `t` degrees (0 = right end, 90 = front-most point). */
function orbitPoint(t, ry) {
  const a = (t * Math.PI) / 180, r = (ORBIT.angle * Math.PI) / 180;
  const x = ORBIT.rx * Math.cos(a), y = ry * Math.sin(a);
  return [ORBIT.cx + x * Math.cos(r) - y * Math.sin(r), ORBIT.cy + x * Math.sin(r) + y * Math.cos(r)];
}

// Masks need ids that are unique inside one SVG; a running counter keeps output deterministic.
let uid = 0;

function glyph(colour, variant = "full") {
  const g = GLYPH[variant];
  const k = ++uid;
  const frame = `transform="translate(${ORBIT.cx} ${ORBIT.cy}) rotate(${ORBIT.angle})"`;
  const back = `<path ${frame} d="M${ORBIT.rx} 0A${ORBIT.rx} ${g.ry} 0 0 0 -${ORBIT.rx} 0"/>`;
  const front = `<path ${frame} d="M-${ORBIT.rx} 0A${ORBIT.rx} ${g.ry} 0 0 0 ${ORBIT.rx} 0"/>`;
  const sat = g.satellite ? orbitPoint(30, g.ry).map(n) : null;
  const all = `<rect x="-2" y="-2" width="28" height="28" fill="#FFFFFF"/>`;
  const cut = (w, body) => `<g fill="none" stroke="#000000" stroke-width="${n(w)}" stroke-linecap="round">${body}</g>`;
  const masks = `<mask id="b${k}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="28" height="28">${all}`
      + cut(g.legs + 2 * g.gap, `<path d="${LEGS}" stroke-linejoin="round"/>`) + `</mask>`
    + `<mask id="l${k}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="28" height="28">${all}`
      + cut(g.orbit + 2 * g.gap, front) + `</mask>`
    + (sat ? `<mask id="f${k}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="28" height="28">${all}`
      + `<circle cx="${sat[0]}" cy="${sat[1]}" r="${n(g.satellite + g.gap)}" fill="#000000"/></mask>` : "");
  return `<defs>${masks}</defs>`
    + `<g fill="none" stroke="${colour}" stroke-linecap="round" stroke-linejoin="round">`
    + `<g stroke-width="${g.orbit}" mask="url(#b${k})">${back}</g>`
    + `<path stroke-width="${g.legs}" d="${LEGS}" mask="url(#l${k})"/>`
    + `<g stroke-width="${g.orbit}"${sat ? ` mask="url(#f${k})"` : ""}>${front}</g></g>`
    + `<circle cx="${APEX[0]}" cy="${APEX[1]}" r="${g.apex}" fill="${colour}"/>`
    + (sat ? `<circle cx="${sat[0]}" cy="${sat[1]}" r="${g.satellite}" fill="${colour}"/>` : "");
}

/** The glyph scaled so its 24-unit box is `box` px wide, centred at (cx, cy). */
function placedGlyph(colour, cx, cy, box, variant = "full") {
  const s = box / 24;
  return `<g transform="translate(${n(cx - box / 2)} ${n(cy - box / 2)}) scale(${n(s)})">${glyph(colour, variant)}</g>`;
}

// The glyph's gradient lives in the glyph's own 24-unit space, so every stroke and node
// shares one continuous 135° gradient instead of each shape getting its own.
const gradientDef = (id = "g") =>
  `<linearGradient id="${id}" gradientUnits="userSpaceOnUse" x1="2" y1="2" x2="22" y2="22">`
  + `<stop offset="0" stop-color="${C.brand["gradient-start"]}"/>`
  + `<stop offset="1" stop-color="${C.brand["gradient-end"]}"/></linearGradient>`;

/** Slate tile of side `size` at (x, y) with the gradient glyph; radius 22 % of the side,
 *  glyph box 56.25 % (36/64). A hairline keeps the tile's edge visible on black. */
function tile(x, y, size, { rounded = true, variant = "full", box = 0.5625, id = "g" } = {}) {
  const r = rounded ? ` rx="${n(size * 0.21875)}"` : "";
  const hairline = rounded
    ? `<rect x="${n(x + size / 128)}" y="${n(y + size / 128)}" width="${n(size - size / 64)}" height="${n(size - size / 64)}"`
      + ` rx="${n(size * 0.21875 - size / 128)}" fill="none" stroke="#FFFFFF" stroke-opacity="0.08" stroke-width="${n(size / 64)}"/>`
    : "";
  return `<rect x="${n(x)}" y="${n(y)}" width="${n(size)}" height="${n(size)}"${r} fill="${C.brand["slate-900"]}"/>`
    + hairline + placedGlyph(`url(#${id})`, x + size / 2, y + size / 2, size * box, variant);
}

function svg(w, h, title, body, defs = "") {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img">`
    + `<title>${title}</title>${defs ? `<defs>${defs}</defs>` : ""}${body}</svg>\n`;
}

// ------------------------------------------------------------------ text
/** Outline `text` in Inter at `size` px with tracking in em; baseline at y = 0. */
function outline(text, weight, size, tracking = 0) {
  const f = INTER[weight];
  const scale = size / f.unitsPerEm;
  const glyphs = f.stringToGlyphs(text);
  let x = 0;
  let d = "";
  glyphs.forEach((g, i) => {
    d += g.getPath(x, 0, size).toPathData(2);
    x += g.advanceWidth * scale;
    if (i < glyphs.length - 1) x += f.getKerningValue(g, glyphs[i + 1]) * scale + tracking * size;
  });
  return { d, width: x, capHeight: (f.tables.os2.sCapHeight || 1490) * scale };
}

/** "AnixOps" (600) plus an optional product word (400), cap height `cap` px; baseline y = 0. */
function nameRun(product, cap, colours) {
  const sizeFor = (w) => cap / (INTER[w].tables.os2.sCapHeight / INTER[w].unitsPerEm);
  const brand = outline("AnixOps", 600, sizeFor(600), -0.01);
  let width = brand.width;
  let body = `<path fill="${colours[0]}" d="${brand.d}"/>`;
  if (product) {
    const space = sizeFor(400) * 0.28;
    const word = outline(product, 400, sizeFor(400), -0.01);
    body += `<path fill="${colours[1]}" transform="translate(${n(width + space)} 0)" d="${word.d}"/>`;
    width += space + word.width;
  }
  return { body, width };
}

// ------------------------------------------------------------------ compositions
function lockup(product, theme) {
  const H = 48; // tile height; cap height H/2, gap H/3 (brand.md 2.4)
  const p = theme === "dark" ? C.dark : C.light;
  const run = nameRun(product, H / 2, [p["label-1"], p["label-2"]]);
  const w = Math.ceil(H + H / 3 + run.width + 1);
  const title = product ? `AnixOps ${product}` : "AnixOps";
  return svg(w, H, title, tile(0, 0, H)
    + `<g transform="translate(${n(H + H / 3)} ${n(H / 2 + H / 4)})">${run.body}</g>`, gradientDef());
}

function banner(product, theme) {
  const W = 1280, H = 320, T = 112;
  const p = theme === "dark" ? C.dark : C.light;
  const run = nameRun(product, 44, [p["label-1"], p["label-2"]]);
  const total = T + 40 + run.width;
  const x0 = (W - total) / 2;
  const title = product ? `AnixOps ${product}` : "AnixOps";
  return svg(W, H, title,
    `<rect width="${W}" height="${H}" fill="${p.bg}"/>` + tile(x0, (H - T) / 2, T)
    + `<g transform="translate(${n(x0 + T + 40)} ${n(H / 2 + 22)})">${run.body}</g>`, gradientDef());
}

function ogImage(product) {
  const W = 1200, H = 630, T = 176, GAP = 72, CAP = 60;
  const run = nameRun(product, CAP, [C.dark["label-1"], C.dark["label-2"]]);
  const top = (H - (T + GAP + CAP)) / 2;
  const defs = gradientDef() + `<radialGradient id="glow" cx="0.5" cy="0.42" r="0.5">`
    + `<stop offset="0" stop-color="${C.brand["gradient-end"]}" stop-opacity="0.35"/>`
    + `<stop offset="1" stop-color="${C.brand["gradient-end"]}" stop-opacity="0"/></radialGradient>`;
  const title = product ? `AnixOps ${product}` : "AnixOps";
  return svg(W, H, title,
    `<rect width="${W}" height="${H}" fill="#000000"/><rect width="${W}" height="${H}" fill="url(#glow)"/>`
    + tile((W - T) / 2, top, T)
    + `<g transform="translate(${n((W - run.width) / 2)} ${n(top + T + GAP + CAP)})">${run.body}</g>`, defs);
}

/** The organisation mark (brand.md 2.5): a bold A whose crossbar is a dot, the O of Ops.
 *  Full bleed, because hosts crop profile pictures to a rounded square or a circle. */
function orgAvatar() {
  const S = 1024, box = S * 0.7;
  return svg(S, S, "AnixOps", `<rect width="${S}" height="${S}" fill="${C.brand["slate-900"]}"/>`
    + `<g transform="translate(${n((S - box) / 2)} ${n((S - box) / 2)}) scale(${n(box / 24)})">`
    + `<path d="M3.6 20.1 12 3.7 20.4 20.1" fill="none" stroke="url(#g)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`
    + `<circle cx="12" cy="17.5" r="2.7" fill="${C.dark["label-1"]}"/></g>`, gradientDef());
}

// ------------------------------------------------------------------ SVG sources
const SOURCES = {
  "mark.svg": () => svg(64, 64, "AnixOps", tile(0, 0, 64), gradientDef()),
  "mark-mono-white.svg": () => svg(24, 24, "AnixOps", glyph("#FFFFFF")),
  "mark-mono-black.svg": () => svg(24, 24, "AnixOps", glyph("#000000")),
  "mark-glyph.svg": () => svg(24, 24, "AnixOps", glyph("currentColor")),
  "favicon.svg": () => svg(32, 32, "AnixOps", tile(0, 0, 32, { variant: "small", box: 27 / 32 }), gradientDef()),
  "wordmark.svg": () => lockup("", "light"),
  "wordmark-on-dark.svg": () => lockup("", "dark"),
  // Full-bleed squares for platforms that apply their own mask (iOS, PWA maskable, Android).
  "app-icon.svg": () => svg(1024, 1024, "AnixOps", tile(0, 0, 1024, { rounded: false }), gradientDef()),
  "app-icon-maskable.svg": () => svg(512, 512, "AnixOps", tile(0, 0, 512, { rounded: false, box: 0.5 }), gradientDef()),
  "app-icon-foreground.svg": () => svg(1024, 1024, "AnixOps", placedGlyph("url(#g)", 512, 512, 512), gradientDef()),
  "app-icon-background.svg": () => svg(1024, 1024, "AnixOps",
    `<rect width="1024" height="1024" fill="${C.brand["slate-900"]}"/>`),
  // Android 13 themed icons: one colour, the system tints it.
  "app-icon-monochrome.svg": () => svg(1024, 1024, "AnixOps", placedGlyph("#FFFFFF", 512, 512, 512)),
  "banner/readme-banner-light.svg": () => banner("", "light"),
  "banner/readme-banner-dark.svg": () => banner("", "dark"),
  "social/og-image.svg": () => ogImage(""),
  "social/org-avatar.svg": () => orgAvatar(),
};

// ------------------------------------------------------------------ rasters
async function png(svgText, w, h = w, { flatten } = {}) {
  const vb = svgText.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
  const density = Math.min(2400, Math.max(72, (72 * w) / parseFloat(vb[1])));
  let img = sharp(Buffer.from(svgText), { density }).resize(w, h, { fit: "fill" });
  if (flatten) img = img.flatten({ background: flatten });
  return img.png({ compressionLevel: 9 }).toBuffer();
}

function ico(images) { // [{size, data}] PNG-compressed ICO entries
  const header = Buffer.alloc(6 + 16 * images.length);
  header.writeUInt16LE(0, 0); header.writeUInt16LE(1, 2); header.writeUInt16LE(images.length, 4);
  let offset = header.length;
  images.forEach(({ size, data }, i) => {
    const e = 6 + 16 * i;
    header.writeUInt8(size >= 256 ? 0 : size, e); header.writeUInt8(size >= 256 ? 0 : size, e + 1);
    header.writeUInt16LE(1, e + 4); header.writeUInt16LE(32, e + 6);
    header.writeUInt32LE(data.length, e + 8); header.writeUInt32LE(offset, e + 12);
    offset += data.length;
  });
  return Buffer.concat([header, ...images.map((i) => i.data)]);
}

function icns(entries) { // [[type, pngData]]
  const parts = entries.map(([type, data]) => {
    const h = Buffer.alloc(8); h.write(type, 0, "ascii"); h.writeUInt32BE(data.length + 8, 4);
    return Buffer.concat([h, data]);
  });
  const h = Buffer.alloc(8); h.write("icns", 0, "ascii");
  h.writeUInt32BE(8 + parts.reduce((a, p) => a + p.length, 0), 4);
  return Buffer.concat([h, ...parts]);
}

async function rasters(src) {
  const out = {};
  const fav = src["favicon.svg"], mark = src["mark.svg"];
  const add = async (path, text, w, h, opts) => { out[path] = await png(text, w, h, opts); };

  // Web
  out["favicon/favicon.ico"] = ico(await Promise.all([16, 32, 48].map(async (s) => ({ size: s, data: await png(fav, s) }))));
  await add("favicon/apple-touch-icon.png", src["app-icon.svg"], 180);
  await add("favicon/icon-192.png", mark, 192);
  await add("favicon/icon-512.png", mark, 512);
  await add("favicon/icon-maskable-512.png", src["app-icon-maskable.svg"], 512);

  // Mobile (Flutter: flutter_launcher_icons) — iOS forbids alpha, so flatten onto the tile slate.
  await add("app-icon/app-icon-1024.png", src["app-icon.svg"], 1024, 1024, { flatten: C.brand["slate-900"] });
  await add("app-icon/app-icon-foreground-1024.png", src["app-icon-foreground.svg"], 1024);
  await add("app-icon/app-icon-background-1024.png", src["app-icon-background.svg"], 1024);
  await add("app-icon/app-icon-monochrome-1024.png", src["app-icon-monochrome.svg"], 1024);

  // Desktop (Tauri: src-tauri/icons)
  for (const [name, s] of [["32x32.png", 32], ["128x128.png", 128], ["128x128@2x.png", 256], ["icon.png", 512]]) {
    await add(`tauri/${name}`, s <= 32 ? fav : mark, s);
  }
  out["tauri/icon.ico"] = ico(await Promise.all([16, 24, 32, 48, 64, 256].map(async (s) =>
    ({ size: s, data: await png(s <= 32 ? fav : mark, s) }))));
  const icnsTypes = [["icp4", 16], ["icp5", 32], ["ic11", 32], ["ic12", 64], ["ic07", 128],
    ["ic13", 256], ["ic08", 256], ["ic14", 512], ["ic09", 512], ["ic10", 1024]];
  out["tauri/icon.icns"] = icns(await Promise.all(icnsTypes.map(async ([t, s]) => [t, await png(s <= 32 ? fav : mark, s)])));

  // Social and README
  await add("social/og-image.png", src["social/og-image.svg"], 1200, 630);
  await add("social/org-avatar.png", src["social/org-avatar.svg"], 1024, 1024, { flatten: C.brand["slate-900"] });
  await add("banner/readme-banner-light.png", src["banner/readme-banner-light.svg"], 2560, 640);
  await add("banner/readme-banner-dark.png", src["banner/readme-banner-dark.svg"], 2560, 640);
  return out;
}

// ------------------------------------------------------------------ main
function write(base, rel, data) {
  const path = join(base, rel);
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, data);
}

const { values: args } = parseArgs({
  options: { check: { type: "boolean" }, product: { type: "string" }, out: { type: "string" } },
});

if (args.product) {
  const out = resolve(args.out || ".");
  const slug = args.product.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  const files = {
    [`wordmark-${slug}.svg`]: lockup(args.product, "light"),
    [`wordmark-${slug}-on-dark.svg`]: lockup(args.product, "dark"),
    [`readme-banner-${slug}-light.svg`]: banner(args.product, "light"),
    [`readme-banner-${slug}-dark.svg`]: banner(args.product, "dark"),
    [`og-image-${slug}.svg`]: ogImage(args.product),
  };
  for (const [rel, text] of Object.entries(files)) write(out, rel, text);
  write(out, `og-image-${slug}.png`, await png(files[`og-image-${slug}.svg`], 1200, 630));
  write(out, `readme-banner-${slug}-light.png`, await png(files[`readme-banner-${slug}-light.svg`], 2560, 640));
  write(out, `readme-banner-${slug}-dark.png`, await png(files[`readme-banner-${slug}-dark.svg`], 2560, 640));
  console.log(`wrote AnixOps ${args.product} assets to ${out}`);
  process.exit(0);
}

const src = Object.fromEntries(Object.entries(SOURCES).map(([k, f]) => [k, f()]));
const RASTERS = ["favicon/favicon.ico", "favicon/apple-touch-icon.png", "favicon/icon-192.png", "favicon/icon-512.png",
  "favicon/icon-maskable-512.png", "app-icon/app-icon-1024.png", "app-icon/app-icon-foreground-1024.png",
  "app-icon/app-icon-background-1024.png", "app-icon/app-icon-monochrome-1024.png", "tauri/32x32.png",
  "tauri/128x128.png", "tauri/128x128@2x.png", "tauri/icon.png", "tauri/icon.ico", "tauri/icon.icns",
  "social/og-image.png", "social/org-avatar.png", "banner/readme-banner-light.png", "banner/readme-banner-dark.png"];

if (args.check) {
  let stale = 0;
  for (const [rel, text] of Object.entries(src)) {
    const path = join(ASSETS, rel);
    if (!existsSync(path) || readFileSync(path, "utf8") !== text) { console.error(`brand/assets/${rel} is stale`); stale = 1; }
  }
  for (const rel of RASTERS) {
    if (!existsSync(join(ASSETS, rel))) { console.error(`brand/assets/${rel} is missing`); stale = 1; }
  }
  if (stale) console.error("run: node scripts/build-assets.mjs");
  process.exit(stale);
}

for (const [rel, text] of Object.entries(src)) write(ASSETS, rel, text);
const raster = await rasters(src);
for (const [rel, data] of Object.entries(raster)) write(ASSETS, rel, data);
const missing = RASTERS.filter((r) => !(r in raster));
if (missing.length) throw new Error(`RASTERS lists files that were not built: ${missing}`);
console.log(`wrote ${Object.keys(src).length} SVG sources and ${Object.keys(raster).length} rasters to brand/assets/`);
