# Email Triage OpenEnv Environment

## Overview

This project implements a **real-world email triage system** using the OpenEnv framework.  
It simulates how humans process inboxes by **classifying, prioritizing, and responding to emails**.

The environment is designed for training and evaluating AI agents on realistic productivity workflows such as:

- Email filtering (spam vs important)
- Priority assignment
- Automated response generation

---

## Motivation

Email overload is a real-world problem in:

- Corporate workflows
- Customer support systems
- Personal productivity tools

This environment models that task in a structured way so AI agents can learn to:

- Identify spam and phishing emails  
- Detect urgent or important messages  
- Handle ambiguous or mixed-content emails  

---

## OpenEnv Compliance

This project fully implements the OpenEnv specification:

- ✅ Typed `Observation`, `Action`, and `Reward` models (Pydantic)
- ✅ `step(action)` → returns `(observation, reward, done, info)`
- ✅ `reset()` → initializes environment
- ✅ `state()` → returns current state
- ✅ `openenv.yaml` included
- ✅ Successfully validated using `openenv validate`

---

## Observation Space

Each step provides:

| Field       | Description              |
|------------|--------------------------|
| email_text | Body of the email        |
| sender     | Sender email address     |
| subject    | Email subject line       |
| step_count | Current step number      |

---

## Action Space

Agent must return:

| Field      | Description                          |
|-----------|--------------------------------------|
| category  | `spam`, `normal`, `important`        |
| priority  | `low`, `high`                        |
| response  | Generated reply                      |
| mark_done | Whether task is completed            |

---

## Tasks

### 🟢 Easy
- Clear spam vs normal emails  
- Low ambiguity  

### 🟡 Medium
- Includes work emails  
- Requires keyword understanding  

### 🔴 Hard
- Mixed signals (e.g., promotion + urgency)  
- Requires reasoning and prioritization  

---

## Reward Function

| Condition                          | Reward |
|----------------------------------|--------|
| Correct classification + priority | 1.0    |
| Partially correct                 | 0.5    |
| Incorrect                         | 0.0    |

✔ Reward is deterministic and reproducible  
✔ Encourages correct reasoning and prioritization  

---

## Baseline Agent

A rule-based intelligent agent is implemented in `inference.py`:

- Detects spam using keyword matching  
- Identifies urgency (e.g., "urgent", "deadline")  
- Recognizes authority senders (boss, HR, professor)  
- Handles security emails (OTP, login alerts)  
- Resolves ambiguous cases intelligently  

---

## Baseline Performance

| Task   | Score |
|--------|------|
| Easy   | 1.0  |
| Medium | 1.0  |
| Hard   | 1.0  |

### Final Average Score: **1.0**

---

## Setup & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt

```
---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: server/app.py
pinned: false
---