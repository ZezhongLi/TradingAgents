from __future__ import annotations

from pathlib import Path

from cli.main import default_report_save_path


def test_default_report_save_path_uses_configured_base_dir():
    path = default_report_save_path(
        {"report_save_dir": "/tmp/trading-reports"},
        "AAPL",
        timestamp="20260622_120000",
    )

    assert path == Path("/tmp/trading-reports/AAPL_20260622_120000")


def test_default_report_save_path_falls_back_to_cwd_reports(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    path = default_report_save_path(
        {"report_save_dir": None},
        "MSFT",
        timestamp="20260622_120000",
    )

    assert path == tmp_path / "reports" / "MSFT_20260622_120000"
