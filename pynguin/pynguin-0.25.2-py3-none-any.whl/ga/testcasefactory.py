#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2022 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
"""Provides a factories for generating different kind of test cases."""
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

import pynguin.configuration as config
import pynguin.testcase.defaulttestcase as dtc
from pynguin.analyses.seeding import InitialPopulationProvider
from pynguin.utils import randomness

if TYPE_CHECKING:
    import pynguin.testcase.testcase as tc
    import pynguin.testcase.testfactory as tf


# pylint:disable=too-few-public-methods
class TestCaseFactory:
    """Abstract class for test case factories."""

    def __init__(self, test_factory: tf.TestFactory):
        """Instantiates the factory.

        Args:
            test_factory: The used test factory
        """
        self._test_factory = test_factory

    @abstractmethod
    def get_test_case(self) -> tc.TestCase:
        """Retrieve a test case.

        Returns:
            A test case  # noqa: DAR202
        """


class RandomLengthTestCaseFactory(TestCaseFactory):
    """Create random test cases with random length."""

    def get_test_case(self) -> tc.TestCase:
        test_case = dtc.DefaultTestCase()
        attempts = 0
        size = randomness.next_int(
            1, config.configuration.search_algorithm.chromosome_length + 1
        )

        while (
            test_case.size() < size
            and attempts < config.configuration.test_creation.max_attempts
        ):
            self._test_factory.insert_random_statement(test_case, test_case.size())
            attempts += 1
        return test_case


class SeededTestCaseFactory(TestCaseFactory):
    """Factory for getting seeded test cases.

    With a certain probability a seeded testcase is returned instead of a randomly
    generated one. If a seeded testcase is returned, it is taken randomly from the
    pool of seeded testcases. If a randomly generated testcase is returned, the
    generation is delegated to the RandomLengthTestCaseFactory.
    """

    def __init__(
        self, delegate: TestCaseFactory, population_provider: InitialPopulationProvider
    ):
        super().__init__(delegate._test_factory)
        self._delegate = delegate
        self._population_provider = population_provider

    def get_test_case(self) -> tc.TestCase:
        if (
            randomness.next_float()
            <= config.configuration.seeding.seeded_testcases_reuse_probability
        ):
            return self._population_provider.random_testcase()
        return self._delegate.get_test_case()
