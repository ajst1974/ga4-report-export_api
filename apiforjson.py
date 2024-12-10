import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'topsolution-63302fbe747f.json'
property_id = "333476340"
client = BetaAnalyticsDataClient()

request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[
        Dimension(name="date"),
    ],
    metrics=[
        Metric(name="activeUsers"),
        Metric(name="newUsers"),
        Metric(name="sessions"),
        Metric(name="screenPageViews"),
    ],
    date_ranges=[DateRange(start_date="2022-01-01", end_date="today")],
)

response = client.run_report(request)
results = []
for row in response.rows:
    result = {
        "date": row.dimension_values[0].value,
        "active_users": row.metric_values[0].value,
        "new_users": row.metric_values[1].value,
        "sessions": row.metric_values[2].value,
        "page_views": row.metric_values[3].value,
    }
    results.append(result)

output_file = "ga4_report.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Resultados exportados para o arquivo: {output_file}")
