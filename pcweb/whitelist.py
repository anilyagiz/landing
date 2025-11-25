WHITELISTED_PAGES = []

def _check_whitelisted_path(path: str) -> bool:
    """Check if a path should be included in the build."""
    return not WHITELISTED_PAGES or path in WHITELISTED_PAGES
