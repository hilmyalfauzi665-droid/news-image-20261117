// news-image-20261117 — entry program (Node 22, standard library only).
// The poster for Tuesday 17 November 2026 sits beside this file as
// entry.png. This program places an exact copy of it at /output/entry.png,
// or at $MAKEFUN_OUTPUT_DIR/entry.png when the grader sets that variable.
// It writes the same bytes on every run: a plain read followed by a write,
// with no timestamps, randomness or network involved, so both grader runs
// produce an identical /output/entry.png.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(targetDir, 'entry.png');

mkdirSync(targetDir, { recursive: true });
writeFileSync(target, readFileSync(source));
