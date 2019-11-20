# Release Checklist

- [ ] Get master to the appropriate code release state.
      [Travis CI](https://travis-ci.org/SethMMorton/natsort) must be passing:
      [![Build Status](https://travis-ci.org/SethMMorton/natsort.svg?branch=master)](https://travis-ci.org/SethMMorton/natsort)

- [ ] Ensure that the `CHANGELOG.md` includes the changes made since last release.
      Please follow the style outlined in https://keepachangelog.com/.
      All new entries should be added into the "Unreleased" section.

- [ ] Bump the version number. Specify either "major", "minor", or "patch":

    ```bash
    tox -e bump patch
    ```

    This will take care of updating the `CHANGELOG.md` with the correct
    release information.

- [ ] Push the bumped commit and the tag:

    ```bash
    git push
    git push --tags
    ```

- [ ] Check the tagged [Travis CI build](https://travis-ci.org/SethMMorton/natsort) has
      deployed to [PyPI](https://pypi.org/project/natsort/#history).

- [ ] Check installation:

    ```bash
    python -m pip uninstall -y natsort && python -m pip install -U natsort
    ```