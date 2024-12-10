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
    dimensions=[Dimension(name="sessionSource")],
    metrics=[Metric(name="activeUsers")],
    date_ranges=[DateRange(start_date="2022-01-01", end_date="today")],
)

response = client.run_report(request)

print("Resultado do Relatório:")
for row in response.rows:
    session_source = row.dimension_values[0].value
    active_users = row.metric_values[0].value
    print(f"Origem da Sessão: {session_source}, Usuários Ativos: {active_users}")

