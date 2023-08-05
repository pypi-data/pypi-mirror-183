from datetime import date

import numpy as np
import pandas as pd
import pytest
from sklearn.ensemble import HistGradientBoostingRegressor

from cluster_experiments.cupac import TargetAggregation
from cluster_experiments.experiment_analysis import GeeExperimentAnalysis
from cluster_experiments.perturbator import UniformPerturbator
from cluster_experiments.power_analysis import PowerAnalysis
from cluster_experiments.power_config import PowerConfig
from cluster_experiments.random_splitter import (
    ClusteredSplitter,
    NonClusteredSplitter,
    StratifiedSwitchbackSplitter,
)
from tests.examples import generate_random_data

N = 1_000


@pytest.fixture
def clusters():
    return [f"Cluster {i}" for i in range(100)]


@pytest.fixture
def dates():
    return [f"{date(2022, 1, i):%Y-%m-%d}" for i in range(1, 32)]


@pytest.fixture
def experiment_dates():
    return [f"{date(2022, 1, i):%Y-%m-%d}" for i in range(15, 32)]


@pytest.fixture
def df(clusters, dates):
    return generate_random_data(clusters, dates, N)


@pytest.fixture
def df_feats(clusters, dates):
    df = generate_random_data(clusters, dates, N)
    df["x1"] = np.random.normal(0, 1, N)
    df["x2"] = np.random.normal(0, 1, N)
    return df


@pytest.fixture
def perturbator():
    return UniformPerturbator(average_effect=0.1)


@pytest.fixture
def analysis_gee_vainilla():
    return GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )


@pytest.fixture
def analysis_gee():
    return GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
        covariates=["estimate_target"],
    )


@pytest.fixture
def cupac_power_analysis(perturbator, analysis_gee):
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    target_agg = TargetAggregation(
        agg_col="cluster",
    )

    return PowerAnalysis(
        perturbator=perturbator,
        splitter=sw,
        analysis=analysis_gee,
        cupac_model=target_agg,
        n_simulations=3,
    )


@pytest.fixture
def switchback_power_analysis(perturbator, analysis_gee_vainilla):
    sw = StratifiedSwitchbackSplitter(
        time_col="date",
        switch_frequency="1D",
        strata_cols=["cluster"],
        cluster_cols=["cluster", "date"],
    )

    return PowerAnalysis(
        perturbator=perturbator,
        splitter=sw,
        analysis=analysis_gee_vainilla,
        n_simulations=3,
    )


@pytest.fixture
def switchback_power_analysis_hourly(perturbator, analysis_gee_vainilla):
    sw = StratifiedSwitchbackSplitter(
        time_col="date",
        switch_frequency="1H",
        strata_cols=["cluster"],
        cluster_cols=["cluster", "date"],
    )

    return PowerAnalysis(
        perturbator=perturbator,
        splitter=sw,
        analysis=analysis_gee_vainilla,
        n_simulations=3,
    )


def test_power_analysis(df, perturbator, analysis_gee_vainilla):
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    pw = PowerAnalysis(
        perturbator=perturbator,
        splitter=sw,
        analysis=analysis_gee_vainilla,
        n_simulations=3,
    )

    power = pw.power_analysis(df)
    assert power >= 0
    assert power <= 1


def test_power_analyis_aggregate(df, experiment_dates, cupac_power_analysis):
    df_analysis = df.query(f"date.isin({experiment_dates})")
    df_pre = df.query(f"~date.isin({experiment_dates})")
    power = cupac_power_analysis.power_analysis(df_analysis, df_pre)
    assert power >= 0
    assert power <= 1


def test_add_covariates(df, experiment_dates, cupac_power_analysis):
    df_analysis = df.query(f"date.isin({experiment_dates})")
    df_pre = df.query(f"~date.isin({experiment_dates})")
    estimated_target = cupac_power_analysis.cupac_handler.add_covariates(
        df_analysis, df_pre
    )["estimate_target"]
    assert estimated_target.isnull().sum() == 0
    assert (estimated_target <= df_pre["target"].max()).all()
    assert (estimated_target >= df_pre["target"].min()).all()
    assert "estimate_target" in cupac_power_analysis.analysis.covariates


def test_prep_data(df_feats, experiment_dates, cupac_power_analysis):
    df = df_feats.copy()
    df_analysis = df.query(f"date.isin({experiment_dates})")
    df_pre = df.query(f"~date.isin({experiment_dates})")
    cupac_power_analysis.cupac_handler.features_cupac_model = ["x1", "x2"]
    (
        df_predict,
        pre_experiment_x,
        pre_experiment_y,
    ) = cupac_power_analysis.cupac_handler._prep_data_cupac(df_analysis, df_pre)
    assert list(df_predict.columns) == ["x1", "x2"]
    assert list(pre_experiment_x.columns) == ["x1", "x2"]
    assert (df_predict["x1"] == df_analysis["x1"]).all()
    assert (pre_experiment_x["x1"] == df_pre["x1"]).all()
    assert (pre_experiment_y == df_pre["target"]).all()


def test_cupac_gbm(df_feats, experiment_dates, cupac_power_analysis):
    df = df_feats.copy()
    df_analysis = df.query(f"date.isin({experiment_dates})")
    df_pre = df.query(f"~date.isin({experiment_dates})")
    cupac_power_analysis.features_cupac_model = ["x1", "x2"]
    cupac_power_analysis.cupac_model = HistGradientBoostingRegressor()
    power = cupac_power_analysis.power_analysis(df_analysis, df_pre)
    assert power >= 0
    assert power <= 1


def test_power_analysis_config(df):
    config = PowerConfig(
        cluster_cols=["cluster", "date"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
        average_effect=0.0,
    )
    pw = PowerAnalysis.from_config(config)
    power = pw.power_analysis(df)
    assert power >= 0
    assert power <= 1


def test_power_analysis_config_avg_effect(df):
    config = PowerConfig(
        cluster_cols=["cluster", "date"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
    )
    pw = PowerAnalysis.from_config(config)
    power = pw.power_analysis(df, average_effect=0.0)
    assert power >= 0
    assert power <= 1


def test_power_analysis_dict(df):
    config = dict(
        cluster_cols=["cluster", "date"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
    )
    pw = PowerAnalysis.from_dict(config)
    power = pw.power_analysis(df, average_effect=0.0)
    assert power >= 0
    assert power <= 1

    power_verbose = pw.power_analysis(df, verbose=True, average_effect=0.0)
    assert power_verbose >= 0
    assert power_verbose <= 1


def test_different_names(df):
    df = df.rename(
        columns={
            "cluster": "cluster_0",
            "target": "target_0",
            "date": "date_0",
        }
    )
    config = dict(
        cluster_cols=["cluster_0", "date_0"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
        treatment_col="treatment_0",
        target_col="target_0",
    )
    pw = PowerAnalysis.from_dict(config)
    power = pw.power_analysis(df, average_effect=0.0)
    assert power >= 0
    assert power <= 1

    power_verbose = pw.power_analysis(df, verbose=True, average_effect=0.0)
    assert power_verbose >= 0
    assert power_verbose <= 1


def test_ttest(df):
    config = dict(
        cluster_cols=["cluster", "date"],
        analysis="ttest_clustered",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
    )
    pw = PowerAnalysis.from_dict(config)
    power = pw.power_analysis(df, average_effect=0.0)
    assert power >= 0
    assert power <= 1

    power_verbose = pw.power_analysis(df, verbose=True, average_effect=0.0)
    assert power_verbose >= 0
    assert power_verbose <= 1


def test_raises_cupac():
    config = dict(
        cluster_cols=["cluster", "date"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        cupac_model="mean_cupac_model",
        n_simulations=4,
    )
    with pytest.raises(AssertionError):
        PowerAnalysis.from_dict(config)


def test_data_checks(df):
    config = dict(
        cluster_cols=["cluster", "date"],
        analysis="gee",
        perturbator="uniform",
        splitter="clustered",
        n_simulations=4,
    )
    pw = PowerAnalysis.from_dict(config)
    df["target"] = df["target"] == 1
    with pytest.raises(ValueError):
        pw.power_analysis(df, average_effect=0.0)


def test_raise_target():
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    perturbator = UniformPerturbator(
        average_effect=0.1,
        target_col="another_target",
    )

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_raise_treatment():
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    perturbator = UniformPerturbator(average_effect=0.1, treatment="C")

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_raise_treatment_col():
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    perturbator = UniformPerturbator(
        average_effect=0.1,
        treatment_col="another_treatment",
    )

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_raise_treatment_col_2():
    sw = ClusteredSplitter(
        cluster_cols=["cluster", "date"],
    )

    perturbator = UniformPerturbator(
        average_effect=0.1,
    )

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
        treatment_col="another_treatment",
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_raise_cluster_cols():
    sw = ClusteredSplitter(
        cluster_cols=["cluster"],
    )

    perturbator = UniformPerturbator(
        average_effect=0.1,
        target_col="another_target",
    )

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_raise_clustering_mismatch():
    sw = NonClusteredSplitter()

    perturbator = UniformPerturbator(
        average_effect=0.1,
        target_col="another_target",
    )

    analysis = GeeExperimentAnalysis(
        cluster_cols=["cluster", "date"],
    )

    with pytest.raises(AssertionError):
        PowerAnalysis(
            perturbator=perturbator,
            splitter=sw,
            analysis=analysis,
            n_simulations=3,
        )


def test_switchback(switchback_power_analysis, df):
    power = switchback_power_analysis.power_analysis(
        df,
        average_effect=0.0,
        verbose=True,
    )
    assert power >= 0
    assert power <= 1


def test_switchback_hour(switchback_power_analysis, df):
    # Random dates in 2022-06-26 00:00:00 - 2022-06-26 23:00:00
    df["date"] = pd.to_datetime(
        np.random.randint(
            1624646400,
            1624732800,
            size=len(df),
        ),
        unit="s",
    )
    power = switchback_power_analysis.power_analysis(
        df,
        average_effect=0.0,
        verbose=True,
    )
    assert power >= 0
    assert power <= 1


def test_switchback_strata():

    # Define bihourly switchback splitter
    config = {
        "time_col": "time",
        "switch_frequency": "30min",
        "perturbator": "uniform",
        "analysis": "ols_clustered",
        "splitter": "switchback_stratified",
        "cluster_cols": ["time", "city"],
        "strata_cols": ["day_of_week", "hour_of_day", "city"],
        "target_col": "y",
        "n_simulations": 3,
    }

    power = PowerAnalysis.from_dict(config)
    np.random.seed(42)
    df_raw = pd.DataFrame(
        {
            "time": pd.date_range("2021-01-01", "2021-01-10 23:59", freq="1T"),
            "y": np.random.randn(10 * 24 * 60),
        }
    ).assign(
        day_of_week=lambda df: df.time.dt.dayofweek,
        hour_of_day=lambda df: df.time.dt.hour,
    )
    df = pd.concat([df_raw.assign(city=city) for city in ("TGN", "NYC", "LON")])
    pw = power.power_analysis(df, average_effect=0.1)
    assert pw >= 0
    assert pw <= 1
