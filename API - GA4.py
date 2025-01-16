import os
import json
from datetime import datetime
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'teste-api-431723-5752543dec0b.json'
property_id = "290845305"
client = BetaAnalyticsDataClient()

# Configuração da solicitação
request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[
        Dimension(name="date"),
        Dimension(name="pagePath"),
        Dimension(name="sessionSource"),
        Dimension(name="region"),
    ],
    metrics=[
        Metric(name="activeUsers"),
        Metric(name="newUsers"),
        Metric(name="totalUsers"),
        Metric(name="sessions"),
        Metric(name="screenPageViews"),
        Metric(name="averageSessionDuration"),
        Metric(name="engagementRate"),
        Metric(name="bounceRate"),
    ],
    date_ranges=[
        DateRange(start_date="2024-01-01", end_date="today")
    ],
)

def convert_to_duration(seconds):
    seconds = int(float(seconds))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def convert_to_percentage(value):
    return f"{float(value) * 100:.2f}%"

def convert_to_date(date_str):
    # Assumindo o formato original como YYYYMMDD
    return datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")

response = client.run_report(request)

results = []
for row in response.rows:
    result = {
        "date": convert_to_date(row.dimension_values[0].value),
        "page_path": row.dimension_values[1].value,
        "session_source": row.dimension_values[2].value,
        "region": row.dimension_values[3].value,
        "active_users": row.metric_values[0].value,
        "new_users": row.metric_values[1].value,
        "total_users": row.metric_values[2].value,
        "sessions": row.metric_values[3].value,
        "page_views": row.metric_values[4].value,
        "avg_session_duration": convert_to_duration(row.metric_values[5].value),
        "engagement_rate": convert_to_percentage(row.metric_values[6].value),
        "bounce_rate": convert_to_percentage(row.metric_values[7].value),
    }
    results.append(result)

output_file = "teste2_ga4_2024_portaltansp.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Resultados exportados para o arquivo: {output_file}")