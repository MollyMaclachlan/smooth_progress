### 0.2.0

**New**

- Added `ProgressBar.show()` method, which displays the current state of the bar. (@MurdoMaclachlan)

**Improvements**

- `ProgressBar.close()`, `ProgressBar.interrupt()` and `ProgressBar.open()` now return a boolean value indicating if they had any effect. (@MurdoMaclachlan)

**Documentation**

- Functions with no return value now use `None` type hinting instead of `NoReturn`, as per the standard. (@MurdoMaclachlan)
- Fixed a typo in the README. (@MurdoMaclachlan)
- Fixed `setup.py` URL pointing to a nonexistent repository. (@MurdoMaclachlan)
- Fixed incorrect type hinting for `ProgressBar.__enter__()`. (@MurdoMaclachlan)

### 0.1.0

- Added `models.ProgressBar`, the base class. (@MurdoMaclachlan)
- Added `exceptions.ProgressBarClosedError`; thrown if `ProgressBar.increment()` called on a closed ProgressBar instance. (@MurdoMaclachlan)
- Added basic documentation. (@MurdoMaclachlan)