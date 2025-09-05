#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

# Force Python/requests to use certifi CA bundle and disable telemetry
# BEFORE importing CrewAI/litellm to avoid SSL/analytics issues
try:
    from pathlib import Path
    from dotenv import load_dotenv
    # Resolve project root: src/stock_picker/main.py -> src -> project root
    _PROJECT_ROOT = Path(__file__).resolve().parents[2]
    load_dotenv(_PROJECT_ROOT / ".env")  # ensure .env keys are loaded explicitly
except Exception:
    pass
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
    os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
except Exception:
    pass

# Best-effort: disable analytics/telemetry that posts to PostHog
os.environ.setdefault("POSTHOG_DISABLED", "1")
os.environ.setdefault("DO_NOT_TRACK", "1")
os.environ.setdefault("LITELLM_DO_NOT_TRACK", "True")
os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")
os.environ.setdefault("CREWAI_TELEMETRY", "False")
os.environ.setdefault("OTEL_EXPORTER_OTLP_ENDPOINT", "")
os.environ.setdefault("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT", "")
os.environ.setdefault("OTEL_EXPORTER_OTLP_METRICS_ENDPOINT", "")

# Clear proxy env to avoid corporate MITM / bad root CAs
for k in [
    "HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy",
    "ALL_PROXY", "all_proxy"
]:
    os.environ.pop(k, None)
os.environ.setdefault("NO_PROXY", "*")
os.environ.setdefault("no_proxy", "*")

# Explicitly disable posthog client if present
try:
    import posthog  # type: ignore
    try:
        posthog.disabled = True  # noqa: F401
    except Exception:
        pass
except Exception:
    pass

from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the research crew.
    """
    inputs = {
        'sector': 'Technology',
        "current_date": str(datetime.now())
    }

    # Create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)


if __name__ == "__main__":
    run()
