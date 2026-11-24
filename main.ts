// news-image-20261124 entry: deterministically copies the bundled entry.png
// to /output/entry.png. Node 22, standard library only, no network.
// Running it twice writes identical bytes.
// Built under makefun anchor round 34253509 (kit init, 2026-11-24).
import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
