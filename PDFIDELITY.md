# Maintaining PDFidelity Engine

## Provenance and license

- Repository: <https://github.com/andygeek/pdfidelity-engine>
- Upstream: <https://github.com/funstory-ai/BabelDOC>
- Starting commit: `38d3896dcde9b5a940c62cf5563cadea673a64d3` (BabelDOC 0.6.4).
- Fork established: **2026-10-10**.
- Original authors, history, copyright notices, and `LICENSE` are retained. This fork and its modifications use **AGPL-3.0**.

The repository is named `pdfidelity-engine`; the distribution remains `BabelDOC`, the import remains `babeldoc`, and the CLI remains `babeldoc`. Upstream PyPI packages and hosted images do not contain this fork's changes. Install from this checkout or a pinned commit in this repository.

## Development

Clone the two repositories as siblings:

```bash
git clone https://github.com/andygeek/pdfidelity-engine.git
git clone https://github.com/andygeek/pdfidelity-translator.git
```

`pdfidelity-translator` uses the sibling `../pdfidelity-engine` as an editable dependency with `uv sync`. Its Dockerfile installs a specific engine commit. See [the translator maintenance guide](https://github.com/andygeek/pdfidelity-translator/blob/main/PDFIDELITY.md) for the combined installation.

For engine-only development, from this checkout:

```bash
uv sync --python 3.12
```

Parsing, document structure, formula handling, font handling, and PDF reconstruction changes belong here. Provider integration and application configuration belong in `pdfidelity-translator`. BabelDOC's internal Python APIs can change; keep the translator adapter compatible when modifying them.

## Incorporating upstream changes

The local project checkout already has `origin` pointing here and `upstream` pointing to funstory-ai/BabelDOC. For a fresh clone, configure:

```bash
git remote add upstream https://github.com/funstory-ai/BabelDOC.git
git remote set-url --push upstream https://example.invalid/upstream-read-only
git config remote.pushDefault origin
```

Bring upstream changes into our history:

```bash
git switch main
git fetch upstream --tags
git merge upstream/main
```

Resolve and review conflicts while retaining our modifications. Commit the resulting changes and push to `origin`. Record each imported upstream revision and behavioral change here. The invalid push URL prevents accidental pushes to upstream; fetching still uses the original GitHub URL.

## Releases and network use

Keep fork changes identifiable and retain AGPL and copyright notices. For a modified version offered over a network, prominently offer users free access to its corresponding source, including required build/install/run scripts. The source must match the deployed revision; a public repository alone does not identify that revision. See `LICENSE`, especially sections 1, 4, 5, and 13.

GitHub Actions are disabled for the initial setup. Inherited workflows and upstream release/package identifiers remain available for later adaptation. No fork package or container has been published, and this setup has not changed PDFidelity's production deployment.

## Modification record

### 2026-10-10

- Established the public PDFidelity fork with upstream history intact.
- Added fork identity, provenance, maintenance instructions, and modification notices.
- Updated package maintainer and repository URLs while preserving the original authors, package name, version, CLI, license, and engine implementation.
