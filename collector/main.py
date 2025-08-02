import psutil
import time
from datetime import datetime, timezone
from influxdb import InfluxDBClient
import platform

def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram_used": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "ram_total": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "disk_used": round(psutil.disk_usage('C:\\').used / (1024 ** 3), 2),
        "disk_total": round(psutil.disk_usage('C:\\').total / (1024 ** 3), 2),
        "uptime": round((time.time() - psutil.boot_time()) / 3600, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

def push_to_influx(metrics):
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('system_metrics')

    json_body = [{
        "measurement": "system_metrics",
        "tags": {
            "host": platform.node(),
            "os": platform.system()
        },
        "time": metrics["timestamp"],
        "fields": {
            "cpu": metrics["cpu"],
            "ram_used": metrics["ram_used"],
            "ram_total": metrics["ram_total"],
            "disk_used": metrics["disk_used"],
            "disk_total": metrics["disk_total"],
            "uptime": metrics["uptime"]
        }
    }]

    client.write_points(json_body)

if __name__ == "__main__":
    while True:
        metrics = get_metrics()
        print("Collected:", metrics)
        try:
            push_to_influx(metrics)
            print("→ Pushed to InfluxDB")
        except Exception as e:
            print("⚠️ Failed to push:", e)
        time.sleep(10)
