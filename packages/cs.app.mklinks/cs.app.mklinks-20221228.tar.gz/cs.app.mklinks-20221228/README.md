mklinks: tool for finding and hardlinking identical files

*Latest release 20221228*:
* Modernise command, pass a RunState to the merge methods.
* merge: check runstate more frequently, tweak progress bar.
* assimilate: plumb runstate.

Mklinks walks supplied paths looking for files with the same content,
based on a cryptographic checksum of their content. It hardlinks
all such files found, keeping the newest version.

Unlike some rather naive tools out there, mklinks only compares
files with other files of the same size, and is hardlink aware - a
partially hardlinked tree is processed efficiently and correctly.

## Class `FileInfo`

Information about a particular inode.

*Method `FileInfo.__init__(self, dev, ino, size, mtime, paths=())`*:
pylint: disable=too-many-arguments

*Method `FileInfo.assimilate(self, other, dry_run=False, runstate=None)`*:
Link our primary path to all the paths from `other`. Return success.

*Method `FileInfo.same_dev(self, other)`*:
Test whether two FileInfos are on the same filesystem.

*Method `FileInfo.same_file(self, other)`*:
Test whether two FileInfos refer to the same file.

*Method `FileInfo.stat_key(S)`*:
Compute the key `(dev,ino)` from the stat object `S`.

## Class `Linker`

The class which links files with identical content.

*Method `Linker.addpath(self, path)`*:
Add a new path to the data structures.

*Method `Linker.merge(self, dry_run=False, runstate=None)`*:
Merge files with equivalent content.

*Method `Linker.scan(self, path, runstate=None)`*:
Scan the file tree.

## Function `main(argv=None)`

Main command line programme.

## Class `MKLinksCmd(cs.cmdutils.BaseCommand)`

Main programme command line class.

Command line usage:

    Usage: mklinkscmd paths...
              Hard link files with identical contents.
              -n    No action. Report proposed actions.

*Method `MKLinksCmd.apply_opt(self, opt, val)`*:
Apply command line option.

*Method `MKLinksCmd.main(self, argv)`*:
Usage: mklinks [-n] paths...
Hard link files with identical contents.
-n    No action. Report proposed actions.

# Release Log



*Release 20221228*:
* Modernise command, pass a RunState to the merge methods.
* merge: check runstate more frequently, tweak progress bar.
* assimilate: plumb runstate.

*Release 20210404*:
* FileInfo.checksum: bump read size to 1MiB.
* Requirements bump to match cs.cmdutils change.

*Release 20210401*:
Major bugfix: subdirectory file paths were computed incorrectly.

*Release 20210306*:
Use cs.cmdutils.BaseCommand for main programme, add better progress reporting.

*Release 20171228*:
Initial PyPI release of cs.app.mklinks.
