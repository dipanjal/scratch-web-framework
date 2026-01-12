#!/bin/bash

# Exit on any error
set -e

if [ -d "build" ]; then
    echo "🗑️  Removing build"
    rm -rf "build"
fi

if [ -d "dist" ]; then
    echo "🗑️  Removing dist"
    rm -rf "dist"
fi

if [ -d "poridhiweb.egg-info" ]; then
    echo "🗑️  Removing poridhiweb.egg-info"
    rm -rf "poridhiweb.egg-info"
fi

