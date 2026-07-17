# -*- coding: utf-8 -*-
"""Tests for free Yahoo Finance-derived US market metrics."""

import pandas as pd

from data_provider.yfinance_fetcher import YfinanceFetcher


class _Ticker:
    def history(self, **_kwargs):
        return pd.DataFrame({"Volume": [100, 100, 100, 100, 100, 200]})


def test_us_quote_metrics_uses_recent_volume_and_float_shares() -> None:
    fetcher = YfinanceFetcher()

    volume_ratio, turnover_rate = fetcher._get_us_quote_metrics(
        _Ticker(), {"floatShares": 10_000_000}, 150
    )

    assert volume_ratio == 2.0
    assert turnover_rate == 0.002
