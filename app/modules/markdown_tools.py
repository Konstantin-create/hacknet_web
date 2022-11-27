import markdown
from markdown.extensions.tables import TableExtension


def markdown_to_html(markdown_text) -> str:
    """Function to generate from markdown to html"""

    return markdown.markdown(
        markdown_text,
        extensions=[TableExtension(use_align_attribute=True)]
    )
