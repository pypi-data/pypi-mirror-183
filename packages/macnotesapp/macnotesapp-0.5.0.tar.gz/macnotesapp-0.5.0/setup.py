# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['macnotesapp', 'macnotesapp.cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.2,<9.0.0',
 'markdown2>=2.4.3,<3.0.0',
 'markdownify>=0.11.6,<0.12.0',
 'py-applescript>=1.0.3,<2.0.0',
 'pyobjc-framework-ScriptingBridge>=9.0.1,<10.0.0',
 'questionary>=1.10.0,<2.0.0',
 'readability-lxml>=0.8.1,<0.9.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.4.4,<13.0.0',
 'textual>=0.8.1,<0.9.0',
 'toml>=0.10.2,<0.11.0',
 'validators>=0.20.0,<0.21.0',
 'wheel>=0.37.1,<0.38.0']

entry_points = \
{'console_scripts': ['notes = macnotesapp.__main__:cli_main']}

setup_kwargs = {
    'name': 'macnotesapp',
    'version': '0.5.0',
    'description': 'Work with Apple MacOS Notes.app from the command line. Also includes python interface for scripting Notes.app from your own python code.',
    'long_description': '# MacNotesApp\n\nWork with Apple MacOS Notes.app from the command line. Also includes python interface for scripting Notes.app from your own python code. Interactive browsing of notes in a TUI (Terminal User Interface? Textual User Interface?) coming soon!\n\n## Installation\n\nIf you just want to use the command line tool, the easiest option is to install via [pipx](https://pypa.github.io/pipx/).\n\nIf you use `pipx`, you will not need to create a python virtual environment as `pipx` takes care of this. The easiest way to do this on a Mac is to use [homebrew](https://brew.sh/):\n\n* Open `Terminal` (search for `Terminal` in Spotlight or look in `Applications/Utilities`)\n* Install `homebrew` according to instructions at [https://brew.sh/](https://brew.sh/)\n* Type the following into Terminal: `brew install pipx`\n* Then type this: `pipx install macnotesapp`\n* `pipx` will install the `macnotesapp` command line interface (CLI) as an executable named `notes`\n* Now you should be able to run `notes` by typing: `notes`\n\nOnce you\'ve installed macnotesapp with pipx, to upgrade to the latest version:\n\n    pipx upgrade macnotesapp\n\n**Note**: Currently tested on MacOS 10.15.7/Catalina and 13.1/Ventura.\n\n## Documentation\n\nFull documentation available at [https://RhetTbull.github.io/macnotesapp/](https://RhetTbull.github.io/macnotesapp/)\n\n## Command Line Usage\n\n<!-- [[[cog\nimport cog\nfrom macnotesapp.cli import cli_main\nfrom click.testing import CliRunner\nrunner = CliRunner()\nresult = runner.invoke(cli_main, ["--help"])\nhelp = result.output.replace("Usage: cli-main", "Usage: notes")\ncog.out(\n    "```\\n{}\\n```".format(help)\n)\n]]] -->\n```\nUsage: notes [OPTIONS] COMMAND [ARGS]...\n\n  notes: work with Apple Notes on the command line.\n\nOptions:\n  -v, --version  Show the version and exit.\n  -h, --help     Show this message and exit.\n\nCommands:\n  accounts  Print information about Notes accounts.\n  add       Add new note.\n  cat       Print one or more notes to STDOUT\n  config    Configure default settings for account, editor, etc.\n  dump      Dump all notes or selection of notes for debugging\n  help      Print help; for help on commands: help <command>.\n  list      List notes, optionally filtering by account or text.\n\n```\n<!-- [[[end]]] -->\n\nUse `notes help COMMAND` to get help on a specific command. For example, `notes help add`:\n\n<!-- [[[cog\nimport cog\nfrom macnotesapp.cli import cli_main\nfrom click.testing import CliRunner\nrunner = CliRunner()\nresult = runner.invoke(cli_main, ["help", "add", "--no-markup"])\nhelp = result.output.replace("Usage: cli-main", "Usage: notes")\ncog.out(\n    "```\\n{}\\n```".format(help)\n)\n]]] -->\n```\nUsage: notes add [OPTIONS] NOTE\n\n  Add new note.\n\n  There are multiple ways to add a new note:\n\n  Add a new note from standard input (STDIN):\n\n  notes add\n\n  cat file.txt | notes add\n\n  notes add < file.txt\n\n  Add a new note by passing string on command line:\n\n  notes add NOTE\n\n  Add a new note by opening default editor (defined in $EDITOR or via `notes\n  config`):\n\n  notes add --edit\n\n  notes add -e\n\n  Add a new note from URL (downloads URL, creates a cleaned readable version\n  to store in new Note):\n\n  notes add --url URL\n\n  notes add -u URL\n\n  If NOTE is a single line, adds new note with name NOTE and no body. If NOTE is\n  more than one line, adds new note where name is first line of NOTE and body is\n  remainder.\n\n  Body of note must be plain text unless --html/-h or --markdown/-m\n  flag is set in which case body should be HTML or Markdown, respectively. If\n  --edit/-e flag is set, note will be opened in default editor before\n  being added. If --show/-s flag is set, note will be shown in Notes.app\n  after being added.\n\n  Account and top level folder may be specified with --account/-a and\n  --folder/-f, respectively. If not provided, default account and folder\n  are used.\n\nOptions:\n  -s, --show             Show note in Notes after adding.\n  -F, --file FILENAME\n  -u, --url URL\n  -h, --html             Use HTML for body of note.\n  -m, --markdown         Use Markdown for body of note.\n  -p, --plaintext        Use plaintext for body of note (default unless changed\n                         in `notes config`).\n  -e, --edit             Edit note text before adding in default editor.\n  -a, --account ACCOUNT  Add note to account ACCOUNT.\n  -f, --folder FOLDER    Add note to folder FOLDER.\n  --help                 Show this message and exit.\n\n```\n<!-- [[[end]]] -->\n\n## Python Usage\n\n<!-- [[[cog\nimport cog\nwith open("examples/example.py") as f:\n    example = f.read()\ncog.out(\n    "```python\\n{}\\n```".format(example)\n)\n]]] -->\n```python\n"""Example code for working with macnotesapp"""\n\nfrom macnotesapp import NotesApp\n\n# NotesApp() provides interface to Notes.app\nnotesapp = NotesApp()\n\n# Get list of notes (Note objects for each note)\nnotes = notesapp.notes()\nnote = notes[0]\nprint(\n    note.id,\n    note.account,\n    note.folder,\n    note.name,\n    note.body,\n    note.plaintext,\n    note.password_protected,\n)\n\nprint(note.asdict())\n\n# Get list of notes for one or more specific accounts\nnotes = notesapp.notes(accounts=["iCloud"])\n\n# Create a new note in default folder of default account\nnew_note = notesapp.make_note(\n    name="New Note", body="This is a new note created with #macnotesapp"\n)\n\n# Create a new note in a specific folder of a specific account\naccount = notesapp.account("iCloud")\naccount.make_note(\n    "My New Note", "This is a new note created with #macnotesapp", folder="Notes"\n)\n\n# If working with many notes, it is far more efficient to use the NotesList object\n# Find all notes with "#macnotesapp" in the body\nnoteslist = notesapp.noteslist(body=["#macnotesapp"])\n\nprint(f"There are {len(noteslist)} notes with #macnotesapp in the body")\n\n# List of names of notes in noteslist\nnote_names = noteslist.name\nprint(note_names)\n\n```\n<!-- [[[end]]] -->\n\n## Known Issues\n\n* Currently, only notes in top-level folders are accessible to `macnotesapp` (#4)\n* Attachments are not currently handled and will be ignored (#15)\n* The title style is not correctly set (#13)\n',
    'author': 'Rhet Turnbull',
    'author_email': 'rturnbull@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/RhetTbull/macnotesapp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<=3.11',
}


setup(**setup_kwargs)
