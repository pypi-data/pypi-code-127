"""
   Descp: Strategy pattern to create approval proposal rate.

   Created on: 05-nov-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui
        <f.r.youssef@hotmail.com>
"""
import pandas as pd
from typing import List

from dao_analyzer.apps.common.data_access.daos.metric.strategy import IMetricStrategy
from dao_analyzer.apps.common.business.transfers.stacked_serie import StackedSerie
from dao_analyzer.apps.common.business.transfers.serie import Serie 
import dao_analyzer.apps.common.data_access.pandas_utils as pd_utl
import dao_analyzer.apps.daohaus.data_access.daos.metric.strategy.st_proposal_outcome \
    as proposal_outcome


class StApprovalProposalRate(IMetricStrategy):

    def clean_df(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


    def process_data(self, df: pd.DataFrame) -> StackedSerie:
        if pd_utl.is_an_empty_df(df):
            return StackedSerie()
        
        outcome: StackedSerie = proposal_outcome.StProposalOutcome()\
            .process_data(df=df)

        rate: List[float] = self.__calculate_rate(outcome)

        metric: StackedSerie = StackedSerie(
            serie = Serie(x=outcome.get_serie()), 
            y_stack = [rate])

        return metric


    def __calculate_rate(self, outcome: StackedSerie) -> List[float]:
        rates: List[float] = []

        approves: List[int] = outcome.get_i_stack(1)
        rejects: List[int] = outcome.get_i_stack(0)

        for i, _ in enumerate(approves):
            numerator: int = approves[i]
            denominator: int = approves[i] + rejects[i]
            rates.append(numerator / denominator if denominator else None)

        return rates
