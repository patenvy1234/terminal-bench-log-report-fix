import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_success_criterion_1_valid_json_object():
    """Success criterion 1: /app/report.json is a valid JSON object."""
    assert REPORT_PATH.is_file(), "no report.json found"

    try:
        report = load_report()
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AssertionError("report.json is not valid JSON") from error

    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_success_criterion_2_exact_keys():
    """Success criterion 2: the report has exactly the three required keys."""
    assert set(load_report()) == EXPECTED_KEYS


def test_success_criterion_3_total_requests():
    """Success criterion 3: total_requests counts the non-empty log entries."""
    assert load_report()["total_requests"] == 6


def test_success_criterion_4_unique_ips():
    """Success criterion 4: unique_ips counts distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_success_criterion_5_top_path():
    """Success criterion 5: top_path is the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
