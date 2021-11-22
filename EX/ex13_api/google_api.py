from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.
    Example input with https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
        get_links_from_spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'token.json')

    Returns
        ['Student Name', 'Alexandra', 'Andrew', 'Anna', 'Becky', ... and so on from the first column]
    """
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = Credentials.from_authorized_user_file(token, scopes)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range="Class Data!A1:A").execute()
    values = result.get('values', [])
    return [row[0] for row in values]
