import os
from app import google_sheets_connector
from app.export_to_github import upload_files
from config import Config


def replace_vars(variables):
    with open(Config.PATH_TEMPFILE) as f:
        templ = f.read()
    result = templ
    for key, value in variables.items():
        query_string = "{{ " + str(key) + " }}"
        result = result.replace(query_string, str(value))
    return result


def create_file(filename, content):
    if not os.path.exists("Projekte"):
        os.mkdir("Projekte")
    with open("Projekte" + os.sep + str(filename) + ".md", "w")as f:
        f.write(content)
    return True


def main():
    content = google_sheets_connector.main(
        spreadsheet_id=Config.SPREADSHEET_ID,
        range_name=Config.RANGE_NAME)

    headers = content[0]

    result = []
    for row in content[1:]:
        export = {}
        for key, column in zip(headers, row):
            export[key] = column
        result.append(export)

    filenames = [row["Name"] for row in result]
    content = [replace_vars(row) for row in result]

    upload_files(filenames=filenames, content=content)

    return "Dateien erstellt."


if __name__ == '__main__':
    main()
