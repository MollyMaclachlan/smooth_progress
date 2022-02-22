### Unreleased

- `ProgressBar.close()`, `ProgressBar.interrupt()` and `ProgressBar.open()` now return a boolean value indicating if they had any effect. (@MurdoMaclachlan)

### 0.1.0

- Added `models.ProgressBar`, the base class. (@MurdoMaclachlan)
- Added `exceptions.ProgressBarClosedError`; thrown if `ProgressBar.increment()` called on a closed ProgressBar instance. (@MurdoMaclachlan)
- Added basic documentation. (@MurdoMaclachlan)