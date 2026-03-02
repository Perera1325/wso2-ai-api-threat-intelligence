\# AI-Powered API Behavioral Threat Intelligence Layer



\## Overview

This project introduces an AI-driven behavioral anomaly detection layer designed to enhance WSO2 API Manager security beyond traditional rate limiting and signature-based protection.



\## Problem

Modern API Gateways detect volumetric attacks but often fail to detect:

\- Business logic abuse

\- Intelligent scraping

\- Credential misuse

\- Behavioral drift



\## Solution

This system introduces:

\- Isolation Forest-based anomaly detection

\- Behavioral feature engineering

\- Risk scoring (0–100)

\- Confidence metrics

\- Suspicious user ranking

\- REST-based microservice architecture



\## Architecture

WSO2 API Manager → Log Collector → Feature Engine → AI Model → Risk Scoring → Threat Intelligence Dashboard



\## API Endpoints

GET /analyze/:user  

GET /analyze-all  

GET /health  



\## Future Improvements

\- Real-time log streaming

\- Kafka integration

\- WSO2 extension packaging

\- Model retraining pipeline

\- Kubernetes deployment



\## Author

Vinod Perera

GitHub: Perera1325

