#!/usr/bin/env python3
from get_metrics_wrapper import get_metrics_wrapper

query = "SELECT rate(count(apm.service.transaction.duration), 1 minute) as 'Web throughput' FROM Metric WHERE (entity.guid = 'ENTITY_GUID') AND (transactionType = 'Web') LIMIT MAX SINCE SINCE_EPOCH TIMESERIES"
get_metrics_wrapper('throughput', query)
