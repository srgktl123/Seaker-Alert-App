# 🚨 Seaker-Alert-App

Seaker-Alert-App is a real-time system monitoring and alerting application that tracks CPU, RAM, Disk usage, and system uptime using a lightweight Python collector, stores data in InfluxDB, and visualizes it through an interactive Grafana dashboard with onscreen and email alerting capabilities.

---

## 📌 Features

- 📈 **Real-Time Monitoring** of:
  - CPU Usage
  - RAM Usage & Total
  - Disk Usage & Total
  - System Uptime
- 📊 **Grafana Dashboard** with:
  - Gauge, Stat & TimeSeries Panels
  - Percentage Usage Views
  - Clean & Interactive UI
- 🔔 **Alerting**:
  - On-screen Alerts in Grafana
  - Trigger Simulation Support
- 💾 **Historical Data Storage** using InfluxDB
- 🧪 **Stress Test Scripts** to simulate load conditions

---

## 🚀 Tech Stack

- Python 3.12 + psutil
- InfluxDB 1.11 (local)
- Grafana (latest)

---


## 💡 How It Works

1. `main.py` collects system stats using `psutil`
2. Pushes metrics to local InfluxDB
3. Grafana queries InfluxDB and displays them live
4. Alert rules monitor thresholds (e.g., CPU > 80%)
5. Alerts trigger onscreen

---

## 🧪 Alert Simulation

To simulate alert conditions and test behavior:

### Trigger High CPU Usage
```bash
python collector/cpu_stress.py
```


You can also lower thresholds temporarily in alert rules to trigger them.

---

## 📊 Grafana Dashboard

> Includes RAM %, Disk %, CPU %, and uptime panels with alert indicators.

### ✅ Live Preview / Demo
🔗 [Grafana Snapshot (Static)](http://localhost:3000/dashboard/snapshot/LMdBCPzzlIuylTg89YntP6RwV9NK4z1R)
> or run locally at: `http://localhost:3000` (after setup)

---

## ⚙️ Installation

### Requirements
- Python 3.11+
- InfluxDB 1.11 (installed manually)
- Grafana (installed manually)
- Optionally: Docker Desktop (if containerizing)

### Setup Instructions (Manual on Windows)

#### 1. Set Up InfluxDB

- Download InfluxDB 1.11 for Windows
- Extract and run:
```bash
influxd
```

#### 2. Run Collector Script

Install Python deps:
```bash
pip install -r collector/requirements.txt
```

Run script:
```bash
python collector/main.py
```

#### 3. Launch Grafana

- Open Grafana in browser: `http://localhost:3000`
- Import `grafana/Seaker-dashboard.json`
- Add InfluxDB as data source:
  - URL: `http://localhost:8086`
  - DB name: `system_metrics`

#### 4. Setup Alerts (in Grafana)

- Create alert rules for CPU, RAM, Disk panels
- Optionally: simulate usage to trigger alerts

---

## 🐳 Optional: Docker Deployment

> If Docker is installed and working:

```bash
docker-compose up --build
```

> Includes InfluxDB, Grafana, and collector script in isolated containers

---

## 📧 Contact / Maintainer

**Author:** Sarang K  
**GitHub:** [srgktl123](https://github.com/srgktl123)  
**Email:** srgktl123@gmail.com

---

## 📃 License

This project is for educational/demo purposes. No official license applied.
