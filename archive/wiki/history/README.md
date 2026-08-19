# Wiki history bundle

`numerical-mooc.wiki.bundle` is a self-contained Git bundle of the NumericalMOOC wiki at source revision `94c9549c11982ec53e8cd98318b34af73f6ce487`. It contains the `master` branch and all 62 reachable commits.

From the repository root, verify the bundle with:

```bash
git bundle verify archive/wiki/history/numerical-mooc.wiki.bundle
```

Restore it as a normal local repository with:

```bash
git clone -b master archive/wiki/history/numerical-mooc.wiki.bundle numerical-mooc-wiki
```

The restored checkout uses the original wiki filenames and content. The normalized, directly readable snapshot is in `archive/wiki/pages/`.
