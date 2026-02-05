#!/bin/bash

OUTPUT=$(docker run -v "$PWD:/app" log-analyzer system.log --json)
STATUS=$?

echo "Analyzer output:"
echo "$OUTPUT"

if [ $STATUS -ne 0 ]; then
  echo "❌  Pipeline failed: errors found in logs"
  exit 1
else
  echo "✅ Pipeline passed: logs are clean"
  exit 0
fi


ERRORS=$(echo "$OUTPUT" | jq 'ERROR // 0')
WARNS=$(echo "$OUTPUT" | jq '.WARN // 0')

if [ "$ERRORS" -gt 0 ]; then
  echo "🚨  Pipeline failed: ERROR count = $ERRORS"
  exit 1
fi

if [ "WARNS" -gt 5 ]; then
  echo "⚠️  Pipeline warning: high WARN count = $WARNS"
  exit 0
fi

echo "✅ Pipeline passed: logs are healthy."
exit 0
