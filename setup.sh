#!/bin/bash
# Setup script for Gmail Search Tool
# Run this on your local Mac to set up the email search tool

set -e  # Exit on any error

echo "=================================="
echo "Gmail Search Tool - Setup"
echo "=================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet google-auth-oauthlib google-auth-httplib2 google-api-python-client
echo "✓ Dependencies installed"
echo ""

# Check for credentials file
if [ ! -f "gmail-credentials.json" ]; then
    echo "⚠️  Gmail credentials file not found!"
    echo ""
    echo "Please do the following:"
    echo "1. Go to: https://console.cloud.google.com/apis/credentials?project=sailing-charter-tools"
    echo "2. Find 'Email Search CLI' in the OAuth 2.0 Client IDs section"
    echo "3. Click the download button (⬇️) on the right"
    echo "4. Save the file as 'gmail-credentials.json' in this directory"
    echo ""
    echo "Then run this setup script again:"
    echo "   ./setup.sh"
    echo ""
    exit 1
fi

echo "✓ Credentials file found"
echo ""

# Check if already authenticated
if [ -f "gmail-token.json" ]; then
    echo "✓ Already authenticated!"
    echo ""
    echo "You're all set! Try searching your email:"
    echo "   ./search-email \"Dream Yacht\""
    echo ""
    exit 0
fi

# Run authentication
echo "Starting authentication process..."
echo ""
echo "This will open your browser to authorize Gmail access."
echo "Make sure to log in with your SAILING BUSINESS email."
echo ""
read -p "Press Enter to continue..."
echo ""

python3 gmail-auth.py

# If authentication helper was used, provide instructions
if [ ! -f "gmail-token.json" ]; then
    echo ""
    echo "Authentication not yet complete."
    echo "Follow the instructions above to complete the OAuth flow."
    exit 1
fi

echo ""
echo "=================================="
echo "✓ Setup Complete!"
echo "=================================="
echo ""
echo "You can now search your email:"
echo "   ./search-email \"Dream Yacht\""
echo "   ./search-email \"from:brokercare@dreamyachtcharter.com\""
echo "   ./search-email \"subject:charter\" 20"
echo ""
echo "For more examples, see: docs/gmail-search-tool.md"
echo ""
