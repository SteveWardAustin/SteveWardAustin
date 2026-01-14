# Gmail Search Tool

Search your Gmail inbox from the command line.

## Setup

Already configured! The tool is ready to use.

## Usage

```bash
./search-email "search query" [max_results]
```

### First Run

The first time you run the tool, it will:
1. Open your browser
2. Ask you to log in to your sailing business Gmail account
3. Request permission to read your emails
4. Save the authorization for future use

After that, searches will run instantly without needing to log in again.

## Examples

### Search by sender:
```bash
./search-email "from:brokercare@dreamyachtcharter.com"
```

### Search by subject:
```bash
./search-email "subject:charter"
```

### Search by keyword:
```bash
./search-email "Navigare"
./search-email "Dream Yacht"
```

### Search with date range:
```bash
./search-email "after:2024/01/01 sailing"
./search-email "after:2024/12/01 before:2025/01/01"
```

### Search for emails with attachments:
```bash
./search-email "has:attachment charter"
```

### Combine multiple criteria:
```bash
./search-email "from:brokercare@dreamyachtcharter.com after:2024/01/01 subject:charter"
```

### Get more results (default is 10):
```bash
./search-email "Dream Yacht" 25
```

## Common Search Operators

- `from:email@example.com` - Emails from specific sender
- `to:email@example.com` - Emails to specific recipient
- `subject:keyword` - Search in subject line
- `has:attachment` - Has attachments
- `after:YYYY/MM/DD` - After specific date
- `before:YYYY/MM/DD` - Before specific date
- `is:unread` - Unread emails
- `is:starred` - Starred emails
- `is:important` - Important emails

You can combine multiple operators in one search!

## Tips

- Use quotes around your entire search query
- Searches are case-insensitive
- You can use the same syntax as Gmail's web interface
- Results show: From, Subject, Date, and Email ID

## Troubleshooting

If you need to re-authenticate with a different email account:
```bash
rm gmail-token.json
```

Then run a search again and log in with the desired account.
