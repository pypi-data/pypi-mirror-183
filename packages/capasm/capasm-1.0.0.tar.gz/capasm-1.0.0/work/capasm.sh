#!/bin/bash
version=$(python -V 2>&1 | grep -Po '(?<=Python )(.)')
if test -z "${version}"; then
   echo "no python interpreter found"
   exit 1
fi
if test "${version}" != "3"; then
   version=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.)')
   if test -z "${version}"; then
      echo "no python3 interpreter found"
      exit  1
   fi
   python_command="python3"
else
   python_command="python"
fi
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
${python_command} $DIR/capasm/capasm.py $*
