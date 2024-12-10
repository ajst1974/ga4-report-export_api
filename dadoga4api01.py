import os
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

print("Resultado do Relatório:")
print("Data       | Usuários Ativos | Novos Usuários | Sessões | Visualizações")
print("---------------------------------------------------------------")
for row in response.rows:
    report_date = row.dimension_values[0].value
    active_users = row.metric_values[0].value
    new_users = row.metric_values[1].value
    sessions = row.metric_values[2].value
    page_views = row.metric_values[3].value
    print(f"{report_date} | {active_users:>15} | {new_users:>14} | {sessions:>7} | {page_views:>12}")
