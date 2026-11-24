# Riemann Proof Compression

Compress the Lean proof referenced in Robert's proposal.

## Goal

Submit a Lean proof package that proves the exact protected Riemann hypothesis statement from the baseline repository while making the proof smaller.

The default score is total submitted source bytes, including any new helper code. Lower is better.

## Protected statement

The Riemann hypothesis theorem statement and any protected definitions from the baseline are fixed. A valid submission must not weaken, rename, wrap, replace, or otherwise change the protected statement being proved.

Before launch, the organizers must pin the baseline repository and commit, record the exact protected theorem name/path, and publish the baseline byte count.

## Validity requirements

A submission is valid only if all of the following hold:

1. It rebuilds independently against the pinned Lean and library versions.
2. It proves the protected Riemann hypothesis theorem exactly as stated in the baseline.
3. It introduces no new axioms and does not rely on `sorry`, `admit`, unsound options, opaque external trust, or verifier changes.
4. Its axiom dependency report is no stronger than the allowed baseline assumptions.
5. It includes enough source for the verifier to reproduce the proof and byte count deterministically.

## Scoring

Among valid submissions, rank by `source_bytes` ascending. The byte count should include all submitted Lean source files and helper files needed by the proof, using a deterministic counting rule pinned before launch. Invalid submissions receive no score.

## Launch checklist

This draft intentionally leaves these launch details unpinned until the organizers provide them:

- baseline repository URL and commit;
- exact protected Lean theorem path/name;
- Lean and library versions;
- deterministic byte-count command;
- deterministic axiom-dependency check;
- baseline byte count.
