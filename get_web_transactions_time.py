#!/usr/bin/env python3
from get_metrics_wrapper import get_metrics_wrapper

query = "SELECT average(apm.service.overview.web) * 1000 FROM Metric WHERE (entity.guid = 'ENTITY_GUID') FACET `segmentName` LIMIT MAX SINCE SINCE_EPOCH TIMESERIES"
get_metrics_wrapper('web_transactions_time', query)
