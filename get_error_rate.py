#!/usr/bin/env python3
from get_metrics_wrapper import get_metrics_wrapper

query = "SELECT count(apm.service.error.count) / count(apm.service.transaction.duration) as 'Web errors' FROM Metric WHERE (entity.guid = 'ENTITY_GUID') AND (transactionType = 'Web') LIMIT MAX SINCE SINCE_EPOCH TIMESERIES"
get_metrics_wrapper('error_rate', query)
