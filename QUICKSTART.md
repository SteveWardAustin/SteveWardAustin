# Quick Start Guide - Gmail Search Tool

Get your Gmail search tool running on your Mac in 5 minutes.

## Step 1: Clone the Repository

Open Terminal on your Mac and run:

```bash
git clone https://github.com/SteveWardAustin/SteveWardAustin.git
cd SteveWardAustin
```

## Step 2: Get Your Credentials File

You need to download the OAuth credentials from Google Cloud:

1. Go to: https://console.cloud.google.com/apis/credentials?project=sailing-charter-tools
2. Look for **"Email Search CLI"** in the OAuth 2.0 Client IDs section
3. Click the **download button (⬇️)** on the right side
4. Save the downloaded file as **`gmail-credentials.json`** in the `SteveWardAustin` directory

## Step 3: Run Setup

In Terminal, from the `SteveWardAustin` directory:

```bash
./setup.sh
```

This will:
- Check Python 3 is installed
- Create a virtual environment
- Install required packages
- Guide you through Gmail authentication

## Step 4: Authenticate

During setup, your browser will open to authorize Gmail access.

**Important:** Log in with your **sailing business Gmail account** (the one you want to search).

Click "Allow" to grant read access to your emails.

## Step 5: Start Searching!

```bash
# Search for emails from Dream Yacht broker care
./search-email "from:brokercare@dreamyachtcharter.com"

# Find charter-related emails
./search-email "subject:charter"

# Search with date range
./search-email "after:2024/12/01 booking"

# Get more results (default is 10)
./search-email "Dream Yacht" 25
```

## Troubleshooting

### "python3: command not found"
Install Python 3 from https://www.python.org/downloads/

### "Permission denied: ./setup.sh"
Run: `chmod +x setup.sh` then try again

### Need to re-authenticate?
Delete `gmail-token.json` and run `./setup.sh` again

### Want more search examples?
See `docs/gmail-search-tool.md` for comprehensive documentation

## What's Next?

This is just the beginning! Future features:
- Export search results to spreadsheet
- Track holds/options with expiration alerts
- Generate professional client proposals
- NauSYS API integration for live inventory search

## Need Help?

Check out the full documentation:
- **Broker Process Guide:** `docs/dream-yacht-broker-process.md`
- **Email Search Documentation:** `docs/gmail-search-tool.md`
