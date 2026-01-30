# Log Analyzer CLI Tool

A simple Linux-style command-line tool written in Python to analyze log files
and summarize INFO, WARN, and ERROR messages.

## Features
- Analyze log files for INFO, WARN, and ERROR levels
- Show percentage distribution
- Filter by log level (e.g. ERROR only)
- Safe handling of missing or empty log files
- Proper exit codes for automation use

## Requirements
- Python 3.10+

## Usage

Analyze a log file:
```bash
./analyzer.py system.log
