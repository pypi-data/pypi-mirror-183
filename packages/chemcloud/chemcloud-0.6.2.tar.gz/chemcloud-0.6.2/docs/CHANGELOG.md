# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

## [0.6.2] - 2022-12-27

### Changed

- Updated `qcelemental==0.24.0 -> 0.25.1`

## [0.6.1] - 2022-07-19

### Changed

- Pegged `qcelemental` to version `0.24.0` since `0.25.0` introduces breaking changes. Need to keep this version in sync with `ChemCloud` server version.

## [0.6.0] - 2022-07-19

### Changed

- Updated project name from `qccloud` to `chemcloud`

## [0.5.0] - 2022-07-15

### Changed

- Updated project name from `tccloud` to `qccloud`

## [0.4.1] - 2022-05-07

### Changed

- Upped the default timeout on http reads from 5.0s -> 20.0s.

## [0.4.0] - 2022-4-02

### Added

- `to_file()` and `from_file()` methods to easily save compute job ids for later retrieval.

### Changed

- Simplified management of task ids between client and server. Only need to send a single id to server even if a batch computation was initiated.

### Removed

- Support for Python3.6. Python3.6 end-of-lif'ed December 23, 2021.

## [0.3.1] - 2022-03-27

### Added

- Decode b64 encoded data returned from server in `AtomicResult.extra['tcfe:keywords']`

### Changed

- Updated `config.settings.tcfe_config_kwargs = "tcfe:config` -> `config.settings.tcfe_keywords = "tcfe:keywords`

## [0.3.0] - 2022-03-26

### Added

- Support for `AtomicInput.protocols.native_files`. User can now request QC package specific files generated during a computation.
- Added support for TeraChem-specific `native_files`. c0/ca0/cb0 bytes files (or any bytes data) placed in `AtomicInput.extras['tcfe:keywords']` will be automatically base64 encoded and sent to the server. The enables seeding computations with a wave function as an initial guess.
- Base64 encoded `native_files` returned from server will be automatically decoded to bytes.

## [0.2.4] - 2021-06-07

### Added

- Private compute queues to `compute()` and `compute_procedure()`

## [0.2.3] - 2021-06-04

### Added

- Batch compute for both `compute()` and `compute_procedure()` methods
- `FutureResultGroup` for batch computations

### Changed

- Added `pydantic` `BaseModel` as base for `FutureResult` objects.

## [0.2.2] - 2021-05-21

### Added

- Extended documentation to include a Code Reference section and much more comprehensive documentation of the main objects.
- Added `compute_procedure` to `TCClient` for geometry optimizations.
- Added `TCClient.version` property for quick version checks.

## [0.2.1] - 2021-03-05

### Added

- Changelog
- User documentation
- Website for documentation

## [0.2.0] - 2021-02-26

### Added

- Added `TaskStatus` enum to hold all task statuses.
- Basic documentation on main classes.
- [core_decisions.md] to document thinking behind architectural choices.

### Changed

- `FutureResult.get()` to return either an `AtomicResult` or a `FailedComputation`
- Simplified README.md overview to use dictionaries instead of classes. Results in simpler tutorial with fewer imports.

## [0.1.1] - 2021-01-22

### Added

- `TCClient` that can manage credentials, submit AtomicInput computations, and retrieve AtomicResult output from TeraChem Cloud.
- `_RequestsClient` class that handles all network requests to TeraChem Cloud server
- `FutureResults` object that is created from a `task_id` and can be used to retrieve a result once finished.

[unreleased]: https://github.com/mtzgroup/chemcloud-client/compare/0.6.2...HEAD
[0.6.2]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.6.2
[0.6.1]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.6.1
[0.6.0]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.6.0
[0.5.0]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.5.0
[0.4.1]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.4.1
[0.4.0]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.4.0
[0.3.1]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.3.1
[0.3.0]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.3.0
[0.2.4]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.2.4
[0.2.3]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.2.3
[0.2.2]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.2.2
[0.2.1]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.2.1
[0.2.0]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.2.0
[0.1.1]: https://github.com/mtzgroup/chemcloud-client/releases/tag/0.1.1
