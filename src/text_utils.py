"""Utilities for cleaning text."""


def clean_name(raw):
    """Clean a name by collapsing whitespace and converting to title case."""
    cleaned = " ".join(raw.split())
    return cleaned.title()
