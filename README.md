# File-Sync

Run script like this: `python main.py <source_folder> <replica_folder> <time_interval_in_seconds> <log_file>`

Assumptions made: 
- log file can be rewritten on every start of the script
- new file creation is the same as just copying the file from the source folder to the replica folder 
- the exercise sheet specifies the need to log only for files, not for directories, therefore, logs about directory removal or copy are not included

You can run the tests by running `pytest` in the command line.
If the `pytest` module is not installed, run `pip install -r requirements.txt`
