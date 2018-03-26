# nessus_merger
Quickly merge multiple .nessus files into a single .nessus file that can then be uploaded back to a Nessus client or parsed.

This script is a modified and extended version of the merger.py tool found here: https://gist.github.com/mastahyeti/2720173

Usage: ./nessus_merger.py -d <target_directory>

-d - This should be the target directory where all of the .nessus files you'd like to merge will live.

Output file will be placed into a new directory ("nss_report") and will be called "report.nessus".

Future Updates:
- Allow for a custom output file to be specified via command line argument.
- Allow for output to be automatically parsed using the Nessus parser here http://www.melcara.com/
- Recursively search a given directory's sub-directories for all .nessus files to merge.
