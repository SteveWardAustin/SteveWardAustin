#!/usr/bin/env python3
"""
Gmail Search Tool - Search your Gmail from the command line
"""

import os
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Authenticate and return Gmail API service."""
    creds = None

    # Token file stores the user's access and refresh tokens
    if os.path.exists('gmail-token.json'):
        creds = Credentials.from_authorized_user_file('gmail-token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'gmail-credentials.json', SCOPES)

            # Try to run local server, but handle no browser case
            try:
                creds = flow.run_local_server(port=0)
            except:
                # Fallback to console-based auth if no browser available
                print("\nNo browser detected. Please authenticate manually:")
                print("1. Open this URL in your browser:")
                print()
                auth_url, _ = flow.authorization_url(prompt='consent')
                print(auth_url)
                print()
                print("2. After authorizing, you'll be redirected to a localhost URL")
                print("3. Copy the ENTIRE URL from your browser and paste it here:")
                print()
                code_url = input("Paste the redirect URL here: ").strip()

                # Extract code from URL
                from urllib.parse import urlparse, parse_qs
                parsed = urlparse(code_url)
                code = parse_qs(parsed.query).get('code', [None])[0]

                if not code:
                    print("Error: Could not extract authorization code from URL")
                    sys.exit(1)

                flow.fetch_token(code=code)
                creds = flow.credentials

        # Save the credentials for the next run
        with open('gmail-token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def search_emails(service, query, max_results=10):
    """Search emails using Gmail query syntax."""
    try:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_results
        ).execute()

        messages = results.get('messages', [])

        if not messages:
            print(f'\nNo emails found matching: {query}')
            return

        print(f'\nFound {len(messages)} email(s) matching: {query}\n')
        print('=' * 80)

        for msg in messages:
            # Get full message details
            message = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='metadata',
                metadataHeaders=['From', 'Subject', 'Date']
            ).execute()

            headers = message['payload']['headers']

            # Extract header info
            from_header = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')

            # Print message info
            print(f'\nFrom: {from_header}')
            print(f'Subject: {subject}')
            print(f'Date: {date}')
            print(f'ID: {msg["id"]}')
            print('-' * 80)

    except HttpError as error:
        print(f'An error occurred: {error}')

def print_usage():
    """Print usage instructions."""
    print("""
Gmail Search Tool - Usage:

python email_search.py "search query" [max_results]

Examples:
  python email_search.py "from:broker@example.com"
  python email_search.py "subject:charter" 20
  python email_search.py "Dream Yacht"
  python email_search.py "after:2024/01/01 sailing"

Common Gmail search operators:
  from:email@example.com     - Emails from specific sender
  to:email@example.com       - Emails to specific recipient
  subject:keyword            - Search in subject line
  has:attachment             - Has attachments
  after:YYYY/MM/DD           - After specific date
  before:YYYY/MM/DD          - Before specific date
  is:unread                  - Unread emails
  is:starred                 - Starred emails

You can combine operators:
  from:broker@example.com after:2024/01/01 subject:charter
    """)

def main():
    """Main function."""
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)

    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    print('\nAuthenticating with Gmail...')
    service = get_gmail_service()

    search_emails(service, query, max_results)

if __name__ == '__main__':
    main()
