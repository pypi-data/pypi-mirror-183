# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bayesian_testing',
 'bayesian_testing.experiments',
 'bayesian_testing.metrics',
 'bayesian_testing.utilities']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'bayesian-testing',
    'version': '0.5.2',
    'description': 'Bayesian A/B testing with simple probabilities.',
    'long_description': '[![Tests](https://github.com/Matt52/bayesian-testing/workflows/Tests/badge.svg)](https://github.com/Matt52/bayesian-testing/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/Matt52/bayesian-testing/branch/main/graph/badge.svg)](https://codecov.io/gh/Matt52/bayesian-testing)\n[![PyPI](https://img.shields.io/pypi/v/bayesian-testing.svg)](https://pypi.org/project/bayesian-testing/)\n# Bayesian A/B testing\n`bayesian_testing` is a small package for a quick evaluation of A/B (or A/B/C/...) tests using Bayesian approach.\n\n**Implemented tests:**\n- [BinaryDataTest](bayesian_testing/experiments/binary.py)\n  - **_input data_** - binary data (`[0, 1, 0, ...]`)\n  - designed for conversion-like A/B testing\n- [NormalDataTest](bayesian_testing/experiments/normal.py)\n  - **_input data_** - normal data with unknown variance\n  - designed for normal data A/B testing\n- [DeltaLognormalDataTest](bayesian_testing/experiments/delta_lognormal.py)\n  - **_input data_** - lognormal data with zeros\n  - designed for revenue-like A/B testing\n- [DiscreteDataTest](bayesian_testing/experiments/discrete.py)\n  - **_input data_** - categorical data with numerical categories\n  - designed for discrete data A/B testing (e.g. dice rolls, star ratings, 1-10 ratings)\n- [PoissonDataTest](bayesian_testing/experiments/poisson.py)\n  - **_input data_** - observations of non-negative integers (`[1, 0, 3, ...]`)\n  - designed for poisson data A/B testing\n\n**Implemented evaluation metrics:**\n- `Probability of Being Best`\n  - probability that a given variant is best among all variants\n  - by default, `best` is equivalent to `greatest` (from a data/metric point of view),\nhowever it is possible to change it using `min_is_best=True` in the evaluation method\n(this can be useful if we try to find the variant while minimizing tested measure)\n- `Expected Loss`\n  - "risk" of choosing particular variant over other variants in the test\n  - measured in the same units as a tested measure (e.g. positive rate or average value)\n\nEvaluation metrics are calculated using simulations from posterior distributions (considering given data).\n\n\n## Installation\n`bayesian_testing` can be installed using pip:\n```console\npip install bayesian_testing\n```\nAlternatively, you can clone the repository and use `poetry` manually:\n```console\ncd bayesian_testing\npip install poetry\npoetry install\npoetry shell\n```\n\n## Basic Usage\nThe primary features are classes:\n- `BinaryDataTest`\n- `NormalDataTest`\n- `DeltaLognormalDataTest`\n- `DiscreteDataTest`\n- `PoissonDataTest`\n\nAll test classes support two methods to insert the data:\n- `add_variant_data` - adding raw data for a variant as a list of observations (or numpy 1-D array)\n- `add_variant_data_agg` - adding aggregated variant data (this can be practical for a large data, as the\naggregation can be done already on a database level)\n\nBoth methods for adding data allow specification of prior distributions\n(see details in respective docstrings). Default prior setup should be sufficient for most of the cases\n(e.g. cases with unknown priors or large amounts of data).\n\nTo get the results of the test, simply call method `evaluate`.\n\nProbabilities of being best and expected loss are approximated using simulations, hence `evaluate` can return\nslightly different values for different runs. To stabilize it, you can set `sim_count` parameter of `evaluate`\nto higher value (default value is 20K), or even use `seed` parameter to fix it completely.\n\n\n### BinaryDataTest\nClass for Bayesian A/B test for binary-like data (e.g. conversions, successes, etc.).\n\n**Example:**\n```python\nimport numpy as np\nfrom bayesian_testing.experiments import BinaryDataTest\n\n# generating some random data\nrng = np.random.default_rng(52)\n# random 1x1500 array of 0/1 data with 5.2% probability for 1:\ndata_a = rng.binomial(n=1, p=0.052, size=1500)\n# random 1x1200 array of 0/1 data with 6.7% probability for 1:\ndata_b = rng.binomial(n=1, p=0.067, size=1200)\n\n# initialize a test:\ntest = BinaryDataTest()\n\n# add variant using raw data (arrays of zeros and ones):\ntest.add_variant_data("A", data_a)\ntest.add_variant_data("B", data_b)\n# priors can be specified like this (default for this test is a=b=1/2):\n# test.add_variant_data("B", data_b, a_prior=1, b_prior=20)\n\n# add variant using aggregated data (same as raw data with 950 zeros and 50 ones):\ntest.add_variant_data_agg("C", totals=1000, positives=50)\n\n# evaluate test:\nresults = test.evaluate()\nresults # print(pd.DataFrame(results).to_markdown(tablefmt="grid", index=False))\n```\n\n    +---------+--------+-----------+---------------+----------------+-----------------+---------------+\n    | variant | totals | positives | positive_rate | posterior_mean | prob_being_best | expected_loss |\n    +=========+========+===========+===============+================+=================+===============+\n    | A       |   1500 |        80 |       0.05333 |        0.05363 |         0.067   |     0.0138102 |\n    +---------+--------+-----------+---------------+----------------+-----------------+---------------+\n    | B       |   1200 |        80 |       0.06667 |        0.06703 |         0.88975 |     0.0004622 |\n    +---------+--------+-----------+---------------+----------------+-----------------+---------------+\n    | C       |   1000 |        50 |       0.05    |        0.05045 |         0.04325 |     0.0169686 |\n    +---------+--------+-----------+---------------+----------------+-----------------+---------------+\n\n### NormalDataTest\nClass for Bayesian A/B test for normal data.\n\n**Example:**\n```python\nimport numpy as np\nfrom bayesian_testing.experiments import NormalDataTest\n\n# generating some random data\nrng = np.random.default_rng(21)\ndata_a = rng.normal(7.2, 2, 1000)\ndata_b = rng.normal(7.1, 2, 800)\ndata_c = rng.normal(7.0, 4, 500)\n\n# initialize a test:\ntest = NormalDataTest()\n\n# add variant using raw data:\ntest.add_variant_data("A", data_a)\ntest.add_variant_data("B", data_b)\n# test.add_variant_data("C", data_c)\n\n# add variant using aggregated data:\ntest.add_variant_data_agg("C", len(data_c), sum(data_c), sum(np.square(data_c)))\n\n# evaluate test:\nresults = test.evaluate(sim_count=20000, seed=52, min_is_best=False)\nresults # print(pd.DataFrame(results).to_markdown(tablefmt="grid", index=False))\n```\n\n    +---------+--------+------------+------------+----------------+-----------------+---------------+\n    | variant | totals | sum_values | avg_values | posterior_mean | prob_being_best | expected_loss |\n    +=========+========+============+============+================+=================+===============+\n    | A       |   1000 |    7294.68 |    7.29468 |        7.29562 |         0.1707  |     0.196874  |\n    +---------+--------+------------+------------+----------------+-----------------+---------------+\n    | B       |    800 |    5685.86 |    7.10733 |        7.1085  |         0.00125 |     0.385112  |\n    +---------+--------+------------+------------+----------------+-----------------+---------------+\n    | C       |    500 |    3736.92 |    7.47383 |        7.4757  |         0.82805 |     0.0169998 |\n    +---------+--------+------------+------------+----------------+-----------------+---------------+\n\n### DeltaLognormalDataTest\nClass for Bayesian A/B test for delta-lognormal data (log-normal with zeros).\nDelta-lognormal data is typical case of revenue per session data where many sessions have 0 revenue\nbut non-zero values are positive numbers with possible log-normal distribution.\nTo handle this data, the calculation is combining binary Bayes model for zero vs non-zero\n"conversions" and log-normal model for non-zero values.\n\n**Example:**\n```python\nimport numpy as np\nfrom bayesian_testing.experiments import DeltaLognormalDataTest\n\ntest = DeltaLognormalDataTest()\n\ndata_a = [7.1, 0.3, 5.9, 0, 1.3, 0.3, 0, 1.2, 0, 3.6, 0, 1.5, 2.2, 0, 4.9, 0, 0, 1.1, 0, 0, 7.1, 0, 6.9, 0]\ndata_b = [4.0, 0, 3.3, 19.3, 18.5, 0, 0, 0, 12.9, 0, 0, 0, 10.2, 0, 0, 23.1, 0, 3.7, 0, 0, 11.3, 10.0, 0, 18.3, 12.1]\n\n# adding variant using raw data:\ntest.add_variant_data("A", data_a)\n# test.add_variant_data("B", data_b)\n\n# alternatively, variant can be also added using aggregated data\n# (looks more complicated, but it can be quite handy for a large data):\ntest.add_variant_data_agg(\n    name="B",\n    totals=len(data_b),\n    positives=sum(x > 0 for x in data_b),\n    sum_values=sum(data_b),\n    sum_logs=sum([np.log(x) for x in data_b if x > 0]),\n    sum_logs_2=sum([np.square(np.log(x)) for x in data_b if x > 0])\n)\n\n# evaluate test:\nresults = test.evaluate(seed=21)\nresults # print(pd.DataFrame(results).to_markdown(tablefmt="grid", index=False))\n```\n\n    +---------+--------+-----------+------------+------------+---------------------+-----------------+---------------+\n    | variant | totals | positives | sum_values | avg_values | avg_positive_values | prob_being_best | expected_loss |\n    +=========+========+===========+============+============+=====================+=================+===============+\n    | A       |     24 |        13 |       43.4 |    1.80833 |             3.33846 |         0.04815 |      4.09411  |\n    +---------+--------+-----------+------------+------------+---------------------+-----------------+---------------+\n    | B       |     25 |        12 |      146.7 |    5.868   |            12.225   |         0.95185 |      0.158863 |\n    +---------+--------+-----------+------------+------------+---------------------+-----------------+---------------+\n\n### DiscreteDataTest\nClass for Bayesian A/B test for discrete data with finite number of numerical categories (states),\nrepresenting some value.\nThis test can be used for instance for dice rolls data (when looking for the "best" of multiple dice) or rating data\n(e.g. 1-5 stars or 1-10 scale).\n\n**Example:**\n```python\nfrom bayesian_testing.experiments import DiscreteDataTest\n\n# dice rolls data for 3 dice - A, B, C\ndata_a = [2, 5, 1, 4, 6, 2, 2, 6, 3, 2, 6, 3, 4, 6, 3, 1, 6, 3, 5, 6]\ndata_b = [1, 2, 2, 2, 2, 3, 2, 3, 4, 2]\ndata_c = [1, 3, 6, 5, 4]\n\n# initialize a test with all possible states (i.e. numerical categories):\ntest = DiscreteDataTest(states=[1, 2, 3, 4, 5, 6])\n\n# add variant using raw data:\ntest.add_variant_data("A", data_a)\ntest.add_variant_data("B", data_b)\ntest.add_variant_data("C", data_c)\n\n# add variant using aggregated data:\n# test.add_variant_data_agg("C", [1, 0, 1, 1, 1, 1]) # equivalent to rolls in data_c\n\n# evaluate test:\nresults = test.evaluate(sim_count=20000, seed=52, min_is_best=False)\nresults # print(pd.DataFrame(results).to_markdown(tablefmt="grid", index=False))\n```\n\n    +---------+--------------------------------------------------+---------------+-----------------+---------------+\n    | variant | concentration                                    | average_value | prob_being_best | expected_loss |\n    +=========+==================================================+===============+=================+===============+\n    | A       | {1: 2.0, 2: 4.0, 3: 4.0, 4: 2.0, 5: 2.0, 6: 6.0} |           3.8 |         0.54685 |      0.199953 |\n    +---------+--------------------------------------------------+---------------+-----------------+---------------+\n    | B       | {1: 1.0, 2: 6.0, 3: 2.0, 4: 1.0, 5: 0.0, 6: 0.0} |           2.3 |         0.008   |      1.18268  |\n    +---------+--------------------------------------------------+---------------+-----------------+---------------+\n    | C       | {1: 1.0, 2: 0.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0} |           3.8 |         0.44515 |      0.287025 |\n    +---------+--------------------------------------------------+---------------+-----------------+---------------+\n\n### PoissonDataTest\nClass for Bayesian A/B test for poisson data.\n\n**Example:**\n```python\nfrom bayesian_testing.experiments import PoissonDataTest\n\n# goals received - so less is better (duh...)\npsg_goals_against = [0, 2, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 0]\ncity_goals_against = [0, 0, 3, 2, 0, 1, 0, 3, 0, 1, 1, 0, 1, 2]\nbayern_goals_against = [1, 0, 0, 1, 1, 2, 1, 0, 2, 0, 0, 2, 2, 1, 0]\n\n# initialize a test:\ntest = PoissonDataTest()\n\n# add variant using raw data:\ntest.add_variant_data(\'psg\', psg_goals_against)\n\n# example with specific priors\n# ("b_prior" as an effective sample size, and "a_prior/b_prior" as a prior mean):\ntest.add_variant_data(\'city\', city_goals_against, a_prior=3, b_prior=1)\n# test.add_variant_data(\'bayern\', bayern_goals_against)\n\n# add variant using aggregated data:\ntest.add_variant_data_agg("bayern", len(bayern_goals_against), sum(bayern_goals_against))\n\n# evaluate test (since fewer goals is better, we explicitly set min_is_best to True)\nresults = test.evaluate(sim_count=20000, seed=52, min_is_best=True)\nresults # print(pd.DataFrame(results).to_markdown(tablefmt="grid", index=False))\n```\n\n    +---------+--------+------------+------------------+----------------+-----------------+---------------+\n    | variant | totals | sum_values | observed_average | posterior_mean | prob_being_best | expected_loss |\n    +=========+========+============+==================+================+=================+===============+\n    | psg     |     15 |          9 |          0.6     |        0.60265 |         0.78175 |     0.0369998 |\n    +---------+--------+------------+------------------+----------------+-----------------+---------------+\n    | city    |     14 |         14 |          1       |        1.13333 |         0.0344  |     0.562055  |\n    +---------+--------+------------+------------------+----------------+-----------------+---------------+\n    | bayern  |     15 |         13 |          0.86667 |        0.86755 |         0.18385 |     0.300335  |\n    +---------+--------+------------+------------------+----------------+-----------------+---------------+\n\n_note: Since we set `min_is_best=True` (because received goals are "bad"), probability and loss are in a favor of variants with lower posterior means._\n\n## Development\nTo set up a development environment, use [Poetry](https://python-poetry.org/) and [pre-commit](https://pre-commit.com):\n```console\npip install poetry\npoetry install\npoetry run pre-commit install\n```\n\n## Roadmap\n\nTest classes to be added:\n- `ExponentialDataTest`\n\nMetrics to be added:\n- `Potential Value Remaining`\n\n## References\n- `bayesian_testing` package itself depends only on [numpy](https://numpy.org) package.\n- Work on this package (including default priors selection) was inspired mainly by a Coursera\ncourse [Bayesian Statistics: From Concept to Data Analysis](https://www.coursera.org/learn/bayesian-statistics).\n',
    'author': 'Matus Baniar',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Matt52/bayesian-testing',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
