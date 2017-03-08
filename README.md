# README #

UxAPI Translator for LAK Hackathon

It takes TSV (tab seperated files), converts to xAPI according to a template, and sends to a learning records store.

# Prerequisites #
Either from apt or pip or similar, you will need
- requests
- dateutil
- pytz

# Running #

This uses Python 2.6+  (may work on older)

# Running #

Configuring

- cp demo.config to <shortname>.config, e.g. lak.config. There can be multiple such files should interacting with different stores be necessary
- create a file uxapi.config containing one <shortname>=<shortname>.config line per config file from the previous step 

Change:

xapiusername and password and uddusername and password to appropriate LRW values
(note udd isn't used in LAK)

change:

uxapilocation= to the location for incoming files.

# Oveview #

Templates are stored in the /template directory

fields for substitution are marked \*\*LIKETHIS\*\*

TSV files for conversion go in the /incoming folder
if the TSV file had a field heading called LIKETHIS then this would replace the \*\*LIKETHIS\*\* values in the template, before being sent to the LRW.

# Example #

A sample attendance.json and attendance.tsv file is provided.

# Timestamps and last record run #

UxAPI uses a very simple mechanism to record the last sent record - a file with the name of the organisation, as set in uxaipi.config, with the time of the last message.  This is updated after the converter is run.  

Incoming data with a data earlier than the data in /timestamps/lak-attendance.txt etc won't be sent, as it is asssumed it has already been processed.

To reset the timing, delete the .txt file.

