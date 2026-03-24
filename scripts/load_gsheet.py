import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_gsheet(data):

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )

    client = gspread.authorize(creds)
    sheet = client.open("Cricket Data").sheet1

    sheet.append_row(["Date", "Team1", "Team2", "Venue"])

    for match in data:
        sheet.append_row([
            match["date"],
            match["team1"],
            match["team2"],
            match["venue"]
        ])
