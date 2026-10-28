"""Server-side helpers for Supabase Storage.

Keep SUPABASE_SERVICE_ROLE_KEY on the server only. Never expose it in templates,
JavaScript bundles, browser environment variables, or source control.
"""
from functools import lru_cache

from django.conf import settings
from supabase import create_client


@lru_cache(maxsize=1)
def _client():
    if not settings.SUPABASE_URL or not settings.SUPABASE_SERVICE_ROLE_KEY:
        raise RuntimeError(
            "Configure SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in the server environment."
        )
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)


def upload_private_document(file_obj, object_path: str, content_type: str):
    """Upload a file to the configured private HRMS bucket and return its path.

    The bucket must be created in Supabase Storage first. Store the returned path
    in a database field if the application later adds document attachments.
    """
    if not object_path or object_path.startswith("/") or ".." in object_path.split("/"):
        raise ValueError("Use a safe, relative object path.")
    payload = file_obj.read()
    if not payload:
        raise ValueError("Cannot upload an empty file.")
    response = (
        _client()
        .storage
        .from_(settings.SUPABASE_STORAGE_BUCKET)
        .upload(
            path=object_path,
            file=payload,
            file_options={
                "content-type": content_type or "application/octet-stream",
                "upsert": "false",
            },
        )
    )
    return object_path
