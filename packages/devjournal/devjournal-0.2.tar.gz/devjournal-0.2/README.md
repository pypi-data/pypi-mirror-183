# devjournal

Terminal-based journal for developers.

**Table of Contents**

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Developing](#developing)
- [Roadmap](#roadmap)

## Installation

```sh
pip install devjournal
```

## Configuration

Optionally, run `dj setup` to specify a Git repo and branch to be used for syncing. Currently, it
is required that the repo has at least one commit already.

The default directory for storing configuration and journal entries is `~/.devjournal`.
This can be overridden with the `DEVJOURNAL_DIR` environment variable.

If running on Windows, consider setting the environment variable `EDITOR` to an editor
of your choice, to make devjournal use that editor when editing journal entries.

## Usage

### Adding new journal entry

```sh
$ dj add
```

This command will open the entry in the editor specified by the environment variable 
`EDITOR`. If that variable is not set, it will use the `start` command instead, which 
on Windows opens the editor for .txt files (by default Notepad).

Alternatively, you can add the text of the entry directly on the command line:

```sh
$ dj add This is my journal entry
```
### Showing all entries

```sh
$ dj log
2022-12-25 16:15:56.536078

add hello world
```

### Show only entries containing any of the search terms

```sh
$ dj find hello
2022-12-25 16:15:56.536078

add hello world
```


## Developing

```sh
# Setup pre-commit and pre-push hooks
hatch run pre-commit install -t pre-commit
hatch run pre-commit install -t pre-push
```

### Running tests

```sh
hatch run cov
```

## Roadmap

- Remove requirement for having the remote repo having at least one commit
- Speed up by not syncing with Git all the time
- Replace find and log with a browser
   - Features: 
     - filtering entries by text
     - filtering entries by 
     - options for selecting a certain entry 
     - editing the selected entry
   - Can textual be used?
     - textual does not work very well in the vscode terminal, so perhaps not.
- Investigate if multiple entries from the same day should be combined under the same
  heading, and if so if they should only show the date and not the time.
