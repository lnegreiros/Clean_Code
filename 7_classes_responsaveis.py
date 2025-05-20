class Report:
    def __init__(self, content):
        self.content = content

    def format_html(self):
        return f"<html><body>{self.content}</body></html>"

class ReportPrinter:
    def print(self, formatted_content):
        print(formatted_content)