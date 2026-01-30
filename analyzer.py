#!/usr/bin/env python3

import os
import sys

print("Running log analyzer...")

def read_logs(filepath):
  with open(filepath, "r") as file:
    return file.readlines()


def analyze_logs(lines):
  counts = {"INFO": 0, "WARN": 0, "ERROR": 0}

  for line in lines:
    for level in counts:
      if level in line:
        counts[level] += 1

  return counts

def generate_report(counts, filter_level=None):

  print("Log Analysis Summary")
  print("---------------------")

  total = sum(counts.values())

  if filter_level:
    if filter_level not in counts:
      print(f"Invalid log level : {filter_level}")
      return

    count = counts[filter_level]
    percent = (count / total) * 100 if total > 0 else 0
    print(f"{filter_level}: {count} ({percent:.1f}%)")
    return

  if total == 0:
    print("No log entries found.")
    return

  for level, count in counts.items():
    percent = (count/ total) * 100
    print(f"{level}: {count} ({percent:.1f}%)")

LOG_FILE = sys.argv[1] if len(sys.argv) > 1 else "system.log"
FILTER_LEVEL= sys.argv[2].upper() if len(sys.argv) > 2 else None

if not os.path.exists(LOG_FILE):
  print(f"Error: {LOG_FILE} does not exist.")
  exit(1)

lines = read_logs(LOG_FILE)
counts = analyze_logs(lines)
generate_report(counts, FILTER_LEVEL)

if counts["ERROR"] > 0:
  exit(2)
else:
  exit(0)

