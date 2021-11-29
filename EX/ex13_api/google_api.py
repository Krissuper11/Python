"""EX 13 Google API."""
from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
        get_links_from_spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'YOUR_CLIENT_SECRET_FILE.json')

    Returns
        ['Student Name', 'Alexandra', 'Andrew', 'Anna', 'Becky', ... and so on from the first column]
    """
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = Credentials.from_authorized_user_file(token, scopes)

    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range="A:A").execute()
    values = result.get('values', [])
    return [row[0] for row in values]


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    result_list = []
    import googleapiclient.discovery

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = developer_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    index = link.index("=")
    playlist_id = link[index + 1:]

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50,
    )
    response = request.execute()
    for dictionary in response["items"]:
        result_list.append(f"www.youtube.com/watch?v={dictionary['contentDetails']['videoId']}")
    if "nextPageToken" in response:
        next_page_token = response.get("nextPageToken")
    else:
        return result_list

    while "nextPageToken" in response:
        request1 = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response1 = request1.execute()

        for dictionary in response1["items"]:
            result_list.append(f"www.youtube.com/watch?v={dictionary['contentDetails']['videoId']}")
        if "nextPageToken" in response1:
            next_page_token = response1['nextPageToken']
        else:
            return result_list
print(get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'AIzaSyB5db-2e2k6AbOjZ3dRLPCKKMV1eMYsRzA'))
