#!/usr/bin/env python3
"""
Gmail Authentication Helper
Handles the OAuth flow for Gmail API access
"""

import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlparse, parse_qs

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    if len(sys.argv) == 1:
        # Step 1: Generate auth URL
        print("\n=== Gmail Authentication Setup ===\n")
        print("Step 1: Get the authorization URL\n")

        flow = InstalledAppFlow.from_client_secrets_file(
            'gmail-credentials.json', SCOPES)

        auth_url, _ = flow.authorization_url(prompt='consent')

        print("Open this URL in your browser:")
        print()
        print(auth_url)
        print()
        print("After you authorize:")
        print("1. You'll be redirected to a localhost URL (the page won't load, that's OK)")
        print("2. Copy the ENTIRE URL from your browser's address bar")
        print("3. Run this command:")
        print()
        print("   ./venv/bin/python gmail-auth.py \"<paste-the-url-here>\"")
        print()

    elif len(sys.argv) == 2:
        # Step 2: Complete auth with redirect URL
        redirect_url = sys.argv[1]

        flow = InstalledAppFlow.from_client_secrets_file(
            'gmail-credentials.json', SCOPES)

        # Extract code from URL
        parsed = urlparse(redirect_url)
        code = parse_qs(parsed.query).get('code', [None])[0]

        if not code:
            print("Error: Could not extract authorization code from URL")
            print("Make sure you pasted the complete redirect URL")
            sys.exit(1)

        print("\nCompleting authentication...")
        flow.fetch_token(code=code)
        creds = flow.credentials

        # Save the credentials
        with open('gmail-token.json', 'w') as token:
            token.write(creds.to_json())

        print("\n✓ Authentication successful!")
        print("You can now use the email search tool:")
        print()
        print('   ./search-email "Dream Yacht"')
        print()

    else:
        print("Usage:")
        print("  Step 1: ./venv/bin/python gmail-auth.py")
        print('  Step 2: ./venv/bin/python gmail-auth.py "<redirect-url>"')

if __name__ == '__main__':
    main()
